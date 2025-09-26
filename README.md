PROJECT TITLE : Appointment Booking System

This is a Django-based web application for managing appointment bookings.  
It includes two modules.
1.Admin Module: Manage slots, view bookings, and cancel appointments.
2.User Module: View available slots, book appointments, view personal bookings, and cancel bookings.

Features

User Features
- Register and login as a user.
- Browse available appointment slots.
- Book a slot.
- View personal bookings.
- Cancel bookings dynamically (AJAX).
- Secure session-based authentication.

Admin Features
- Login as admin.
- Create slots.
- View all bookings in the system.
- Cancel bookings if needed.

Tech Stack

Technology            Purpose            
Django         -     Backend framework 
HTML5, CSS3    -     Frontend design   
Bootstrap 5   -     Styling and layout
JavaScript (Fetch API) - AJAX cancel feature 
SQLite        -    Database          


Installation and Setup

1. Create Virtual Environment

python -m venv venv

Activate it:

venv\Scripts\activate
 

2. Run Migrations

python manage.py makemigrations
python manage.py migrate

3. Create Superuser (Admin Login)

python manage.py createsuperuser

4. Start Development Server**

python manage.py runserver

Open your browser and visit:

http://127.0.0.1:8000/

Default Credentials

Role   Email                                            Password 

 Admin  [admin123@gmail.com](mailto:admin123@gmail.com)  admin123 

Usage Guide

For Users:

1. Register a new account.
2. Login with your credentials.
3. Browse available slots and book one.
4. View your bookings under "My Bookings".
5. Cancel bookings using the Cancel button.

For Admin:

1. Login with admin credentials (`admin123@gmail.com` / `admin123`).
2. Create slots for booking.
3. View all bookings.
4. Cancel any booking when needed.

