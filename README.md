# Django Authentication Microservice

This repository contains the implementation of a microservice for user authentication using Django with JWT. The microservice provides username-password authentication for various front-end Single Page Applications (SPAs), currently tested with Nuxt 3.js.

## Features

- User Registration
- User Login
- JWT Token Generation
- Token-based Authentication

## Technologies Used

- Django
- JWT (JSON Web Tokens)

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3
- Django 4.2.11 or higher


## Installation

  1. **Clone the repository:**
  
      ```bash  
  
      git clone https://github.com/yourusername/django-authentication.git
      cd django-authentication
      ```
  2. **Install dependencies:**
  
      ```bash
      pip install -r requirements.txt
      ```
  3. **Configure the database:**
  
      - Open the `settings.py` file in the `project_name` directory.
      - Update the `DATABASES` setting to match your database configuration. Example using SQLite:
      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.sqlite3',
              'NAME': BASE_DIR / "db.sqlite3",
          }
      }
      ```
      
      Or, if using PostgreSQL:
  
      ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.postgresql',
              'NAME': 'your_db_name',
              'USER': 'your_db_user',
              'PASSWORD': 'your_db_password',
              'HOST': 'localhost',
              'PORT': '5432',
          }
      }
      ```
  
      
      Or, if using MySQL:
  
     
     ```python
      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'your_db_name',
              'USER': 'your_db_user',
              'PASSWORD': 'your_db_password',
              'HOST': 'localhost',
              'PORT': '5432',
          }
      }
      ```
  4. **Make migrations and migrate the database:**
  
      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```
  6. **Run the development server:**
  
      ```bash
      python manage.py runserver
    ```

### Usage

  ## Registration
  
  Send a POST request to `<your-host>/authentication/register/` with the following payload in body reqeust:
  
    ```json
    {
      "username": "yourusername",
      "fullname": "Your Full Name",
      "email": "youremail@example.com",
      "password": "yourpassword"
    }
    ```
  
  Response:
  
    ```json
    {
      "data":{
        "message": "user registered successfully",
      },
      "status": 200
    }
    ```
  
  exemple for registration 

  
  ![image](https://github.com/user-attachments/assets/f72c98b4-01e4-45b2-aaee-f70ae424b4c5)



  
  ### Login
  
  Send a POST request to `<your-host>/authentication/login/` with the following payload in body reqeust:
  
    ```json
    {
      "username": "yourusername",
      "password": "yourpassword"
    }
    ```
  
  Response:
  
    ```json
    {
      "data":{
        "message": "login succes",
        "token": xxxx
      },
      "status": 200
    }
    ```
    
  Storing the Token:
  
  After a successful login, store the JWT token in local storage or any other storage method to use it for subsequent authorization features.
  Example using local storage:
    
  ![image](https://github.com/user-attachments/assets/30f977bc-73bc-408d-8714-7d17695e2f38)


  ### Update Password
  
  Send a POST request to `<your-host>/authentication/changepassword/` with the following payload in body reqeust:
  
    ```json
    {
        newpassword: newpassword.value,
    },
    ```
  
  Response:
  
    ```json
    {
      "status": 200
    }
    ```
  exemple of updating password
  
  make sure to use token you stored before
  
  ![image](https://github.com/user-attachments/assets/10819b44-6b01-4964-944b-073b2d68bd91)


