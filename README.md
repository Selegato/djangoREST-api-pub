# Customer and Benefits Management

##  Table of Contents

- [English](#english)

## English

This project is a Django application designed to manage customer information and their associated benefits. It utilizes a MongoDB database to store customer data and an SQLite database to manage customer benefits. The application also includes features for authentication and logging.

*Under Continuous Development*


- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contact](#contact)

## Features

- **API REST ENDPOINTS**: 
1. **`/customers/`**: Manage the CRUD operations for customers in MongoDB.
2. **`/benefits/`**: Manage the CRUD operations for benefits in SQLite.
3. **`/customer-benefits/`**: List all customers and their associated benefits.

- **AUTHENTICATION**: Basic authentication is required to access the API interface.

- **DIFFERENT DATABASES**: Uses MongoDB for customer data and SQLite for benefits.

- **LOGS**:  Local logs are saved in case of errors or critical failures.

- **RANDOM DATA GENERATION**:  Random data genarated by FAKER



## Environment Setup

### Initial Steps

1. **Start Docker Compose:**:
    ```sh
    cd inits
    docker-compose up
    ```
    This will install MongoDB and MongoExpress.

2. **Create a [`.env`] file**:
    ```env
    MONGO_URL='mongodb://admin:admin@localhost:27017/UniDataQA?authSource=admin'
    SECRET_KEY='sua_chave_secreta_django'
    ```

3. **Create and Activate a Virtual Environment:**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

4. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

### Django Setup

1. **Apply Migrations**:
    ```sh
    cd src
    python manage.py makemigrations
    python manage.py migrate
    ```

2. **Create a Superuser**:
    ```sh
    python manage.py createsuperuser
    ```
    It is recommended to use `admin/admin` as credentials.

3. **Start the Server:**:
    ```sh
    python manage.py runserver
    ```

### Database Initialization

1. **Run Random Data Insertion Script**:
    ```sh
    cd inits
    python random_insertions.py
    ```
    This script will make 50 API calls with random data to initialize the MongoDB customer database.

## Application Access

A aplicação estará disponível em: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

## Contact

Feel free to reach out to me through the contact form or connect with me on my social media profiles:

- [WEB](selegato.com)
- [LinkedIn](https://www.linkedin.com/in/paulo-selegato-a298012b6/)
- [Instagram](https://www.instagram.com/paulo.selegato)
- [GitHub](https://github.com/Selegato)

Thank you for visiting my page!
Glory to Ukraine!