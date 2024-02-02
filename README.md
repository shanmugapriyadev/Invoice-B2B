# InvoiceB2B Project
### Description

The InvoiceB2B project is a web application designed for managing business-to-business invoices. It allows company to create, manage, and track invoices of their clients efficiently.
Installation

### To install and set up the project locally, follow these steps:

    - Clone the repository from GitHub.
    - Install dependencies using pip install -r requirements.txt.
    - Configure the database settings in settings.py.
    - Run migrations using python manage.py migrate.
    - Start the development server using python manage.py runserver.

### Usage

Once the project is set up, users can navigate to the provided URL and interact with the web interface to create and manage invoices. Use the admin interface to manage users, companies, clients, and other data.
Technologies Used

    - Django
    - Django REST Framework
    - SQLite (or any other supported database)
    - Git

### Folder Structure

    - core: Contains models and views related to core functionalities like states and currencies.
    - company: Contains models and views for managing company information and addresses.
    - client: Contains models and views for managing client information.
    - invoice: Contains models, views, and API endpoints for managing invoices.

### API Endpoints

The project provides API endpoints for managing invoices. These include:

    api/company/companies/
    api/company/company-addresses/
    api/company/company-gst-numbers/
    api/company/company-payment-modes/

### Authentication and Authorization

Authentication is implemented using Django's built-in authentication system. Users need to log in with valid credentials to access certain features like creating or modifying invoices.
