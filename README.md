# Django Blog

A simple blog application built with Django, showcasing how to create and manage blog posts.

## Requirements

- Python: 3.13.2
- Django: 5.0
- SQLite3: Built-in with Django

## Project Structure
```
django_blog/
│
├── manage.py
├── django_blog/
│   ├── init.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── blog/
│   ├── migrations/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── templates/
├── base.html
├── home.html
└── post_detail.html
├── static/
│     ├──css/
```

## Features

- **Model**:
    - `Post`: Represents a blog post with the following fields:
        - `pk`: Primary key (auto-generated)
        - `title`: Title of the post
        - `body`: Content of the post
        - `author`: Many-to-one relationship with `auth.User`

- **Views**:
    - **Home Page**: Displays a list of all blog posts.
    - **Post Detail View**: Displays detailed information about a specific post. Accessible via the URL: `/post/{pk}`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django_blog.git
   cd django_blog
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   
3. Install required packages:
    ```bash
   pip install -r requirements.txt

4. Run migrations to set up the database:
    ```bash
   pip install -r requirements.txt

5. Create a superuser (optional):
    ```bash
   python manage.py createsuperuser

6. Run the development server:
    ```bash
   python manage.py runserver

Usage

    Navigate to the home page to view a list of posts.
    Click on any post title to access the detail view.
