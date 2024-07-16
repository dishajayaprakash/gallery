
# Gallery Project

This is a dynamic gallery application built with Django. It allows users to view, upload, and manage images in a web-based interface. This README outlines the steps to set up and run the project locally.

## Prerequisites

Before you start, ensure you have the following installed:
- Python 3.8 or newer
- pip (Python package manager)

## Installation

### Clone the Repository

First, clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/dishajayaprakash/gallery.git
cd gallery
```

### Install Dependencies

Install the required packages using pip:

```bash
pip install django pillow
```

## Configuration

### Database Setup

By default, Django uses SQLite. If you want to use another database, configure your database in the `settings.py` file, and then perform migrations:

```bash
python manage.py migrate
```

### Create an Admin User

Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to create the superuser account.

## Running the Application

Start the Django development server:

```bash
python manage.py runserver
```

The gallery will be available at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Admin Interface

Access the admin interface at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin). Use the superuser credentials you created earlier to log in and manage the gallery images.
