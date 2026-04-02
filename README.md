# My Blog

A full-featured blog web application built with Django, featuring user authentication, blog post management, comments, search, and a REST API.

---

## Features

- User registration, login, and logout
- Create, edit, and delete blog posts (authors only)
- Image uploads for blog posts
- Comments on posts with edit and delete (comment authors only)
- Search posts by keyword
- Paginated blog list
- REST API with full CRUD and custom permissions
- Responsive editorial design with Bootstrap 5

---

## Tech Stack

- **Backend** — Django 5.x, Django REST Framework
- **Database** — SQLite (development)
- **Frontend** — Bootstrap 5, Custom CSS (Playfair Display + DM Sans)
- **Auth** — Django built-in authentication

---

## Project Structure

```
my_blog/
├── accounts/                  # User registration and auth
│   ├── templates/accounts/
│   │   ├── registration.html
│   │   └── registration/
│   │       └── login.html
│   ├── views.py
│   └── urls.py
├── blog/                      # Core blog app
│   ├── templates/blog/
│   │   ├── base.html
│   │   ├── blog_list.html
│   │   ├── blog_details.html
│   │   ├── create_post.html
│   │   ├── edit_post.html
│   │   ├── delete_post.html
│   │   ├── edit_comment.html
│   │   └── delete_comment.html
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── serializers.py
│   ├── apiviews.py
│   ├── permissions.py
│   └── urls.py
├── static/
│   └── css/
│       └── style.css
├── media/                     # User uploaded images
├── my_blog/                   # Project settings
│   ├── settings.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/my_blog.git
cd my_blog
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## Environment Variables

No `.env` file is required for development. For production, set the following in your environment:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Set to `False` in production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts |

---

## REST API

Base URL: `/api/`

| Method | Endpoint | Description | Auth Required |
|---|---|---|---|
| GET | `/api/blogs/` | List all posts | No |
| POST | `/api/blogs/` | Create a post | Yes |
| GET | `/api/blogs/<id>/` | Retrieve a post | No |
| PUT | `/api/blogs/<id>/` | Update a post | Author only |
| DELETE | `/api/blogs/<id>/` | Delete a post | Author only |

### Permissions

- **Read** — open to everyone
- **Create** — requires login
- **Edit / Delete** — restricted to the post author

---

## Key URLs

| URL | Description |
|---|---|
| `/` | Blog list (home) |
| `/blog/post/<id>/` | Blog detail |
| `/blog/post/create/` | Create a post |
| `/blog/post/<id>/edit/` | Edit a post |
| `/blog/post/<id>/delete/` | Delete a post |
| `/accounts/register/` | Register |
| `/login/` | Login |
| `/logout/` | Logout |
| `/admin/` | Django admin |

---

## Media Files

Uploaded images are stored in the `media/` folder. In `settings.py`:

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

In development, media files are served automatically when `DEBUG = True`.

---

