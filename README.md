# Aurafits

Aurafits is a Django based fashion website project for displaying fashion products in a simple and organized way.

## Overview

Aurafits is designed as a basic fashion website where users can browse products, search items, filter products by category, and view products with pagination. The project also includes user login/signup functionality and a contact enquiry form.

This project was created for learning, practice, and project submission purposes.

## Features

- Home page with carousel and product preview
- Product listing page
- Product search functionality
- Category filtering
- Pagination for product browsing
- User signup and login
- Contact enquiry form
- About page
- Responsive layout using Bootstrap
- Product cards with image, description, category, and product ID

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite

## Main Pages

- **Home Page**: Displays carousel and selected products
- **Products Page**: Shows products with pagination and category filtering
- **About Page**: Provides project and brand information
- **Contact Page**: Allows users to submit enquiries
- **Login Page**: Allows existing users to sign in
- **Signup Page**: Allows new users to register

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/TavishaBudhiraja/Aurafits.git
```

### 2. Go to the project folder

```bash
cd Aurafits
```

### 3. Create a virtual environment

```bash
python -m venv env
```

### 4. Activate the virtual environment

For Windows:

```bash
.\env\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available, install Django manually:

```bash
pip install django
```

### 6. Run migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

### 8. Open the website

```text
http://127.0.0.1:8000/
```

## Project Purpose

The purpose of this project is to practice core Django concepts, including:

- Models and database handling
- Views and URL routing
- Django templates
- Static and media files
- User authentication
- Search functionality
- Category filtering
- Pagination
- Form submission

## Future Improvements

- Add product detail pages
- Add product price and size options
- Improve UI design and responsiveness
- Add cart or wishlist functionality
- Add order or enquiry-based product selection

## Status

This project is currently created for learning, practice, and project submission purposes.

## Author

Created by **Tavisha Budhiraja**
