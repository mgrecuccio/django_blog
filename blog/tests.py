from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth import get_user_model

# Create your tests here.
class BlogPost(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username = "testUser",
            email = "test@email.com",
            password = "secret"
        )

        cls.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=cls.user
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testUser")
        self.assertEqual(str(self.post), "A good title")
        self.assertEqual(self.post.get_absolute_path(), "/post/1")


    def test_url_exists_at_correct_location_list_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)


    def test_url_exists_at_correct_location_detail_view(self):
        response = self.client.get("/post/1")
        self.assertEqual(response.status_code,200)


    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Nice body content")


    def test_post_detail_view(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/99999")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_detail.html")
        self.assertContains(response, "A good title")
        self.assertEqual(no_response.status_code, 404)