# Room-Chat sample application

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/pratham5201/Room-chat.git
$ cd Room-Chat
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/chat/`.

## Walkthrough

# Room-chat

Certainly! A comprehensive project that incorporates various Django features and best practices.

### Django Rooom-Chat Project

1. **User Authentication and Authorization:**
   - Implement user registration and login functionality.
   - Use Django's built-in authentication system.

2. **Chat Models:**
   - Create models for Room and Chat.
   - Define relationships between models .

3. **Django Admin:**
   - Customize the Django admin interface to manage Rooms and Chat.
   - Apply ModelAdmin classes for better admin management.

4. **Django Views and Templates:**
   - Create views for displaying Chats and Room.
   - Use class-based views and function-based views.
   - Develop templates for rendering HTML dynamically.

5. **Django URL Patterns:**
   - Define URL patterns for accessing different views.
   - Utilize path converters and regular expressions.

6. **Django Static Files and Media:**
   - Organize and serve static files (CSS, JavaScript) using the `static` template tag.

7. **Django Middleware:**
   - Implement middleware for global request/response processing.
   - Handle authentication, security checks, or custom headers.

This project will allow you to explore and implement a wide range of Django features, making your understanding of Django more robust. As you progress, you can continue to enhance and expand the features of your Chats, adding more complexity and functionality.