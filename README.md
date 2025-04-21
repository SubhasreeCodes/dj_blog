# 📝 Django Blog App (Backend + Frontend)

This is a **Django-based blog application** that features a clean separation of concerns using two Django apps: a **backend** for data and APIs, and a **frontend** for rendering pages and UI. Users can read blog posts, view detailed entries, and manage content via the admin dashboard. Optionally, the backend supports **Django REST Framework (DRF)** for API access.

---

## 🚀 Features

- Create, edit, and delete blog posts via Django Admin.
- Homepage that lists all blog posts in reverse chronological order.
- Detail view for individual blog posts.
- Responsive HTML templates with Django templating engine.
- Optional REST API using Django REST Framework.

---

## 🛠️ Technologies Included

This project utilizes the following technologies:

- **Django** – Python web framework for full-stack development.
- **SQLite** – Default lightweight database.
- **Django REST Framework** – Optional API layer for blogs.
- **HTML/CSS** – For frontend structure and styling.
- **Bootstrap (optional)** – For UI enhancements.
- **Python 3.8+**

---

## 📋 Prerequisites

Before running this app, ensure the following are installed:

- Python 3.8 or higher  
- pip (Python package manager)  
- virtualenv *(optional but recommended)*

---

## 📁 Folder Structure Overview

```
blog_project/
├── blog_project/       # Django settings and root config
│   ├── settings.py
│   ├── urls.py
├── backend/            # Handles models, admin, APIs
│   ├── models.py
│   ├── admin.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
├── frontend/           # Handles templates, static, and UI logic
│   ├── templates/
│   │   └── frontend/
│   │       ├── base.html
│   │       ├── home.html
│   │       └── detail.html
│   ├── views.py
│   ├── urls.py
├── manage.py
└── db.sqlite3
```



Then open in your browser:

- 🌐 `http://127.0.0.1:8000/` → Blog homepage  
- 🔐 `http://127.0.0.1:8000/admin/` → Admin dashboard  
- 🔁 `http://127.0.0.1:8000/api/blogs/` → REST API (optional)


## 🖼️ Screenshots

### 1. Blog Home

![Home](screenshots/blog_home.png)

### 2. Blog Detail

![Detail](screenshots/blog_detail.png)

---

## 🔄 API Endpoints (if using DRF)

| Endpoint           | Method | Description              |
|--------------------|--------|--------------------------|
| `/api/blogs/`      | GET    | List all blog posts      |
| `/api/blogs/`      | POST   | Create a new blog post   |
| `/api/blogs/{id}/` | GET    | Retrieve single blog     |
| `/api/blogs/{id}/` | PUT    | Update a blog post       |
| `/api/blogs/{id}/` | DELETE | Delete a blog post       |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🤝 Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Bootstrap](https://getbootstrap.com/) – for optional UI styling
- [Unsplash](https://unsplash.com/) – for placeholder images


