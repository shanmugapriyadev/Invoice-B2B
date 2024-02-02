# InvoiceB2B Project
### Description

The InvoiceB2B project is a web application designed for managing business-to-business invoices. It allows company to create, manage, and track invoices of their clients efficiently.
Installation

### Installation

To install and set up the InvoiceB2B project locally, follow these steps:

Clone the project repository from GitHub:

bash

    git clone https://github.com/yourusername/InvoiceB2B.git

Navigate to the project directory:

bash

    cd InvoiceB2B

Install project dependencies using pip:

    pip install -r requirements.txt

Set up the database and migrate the necessary tables:

    python manage.py makemigrations
    python manage.py migrate

Run the development server:

    python manage.py runserver

Access the application in your web browser at http://localhost:8000.

### Usage

Once the InvoiceB2B project is set up, you can perform the following actions:

Create invoices for transactions between companies and clients.
View, edit, and delete existing invoices.

### Technologies Used

The InvoiceB2B project utilizes the following technologies, frameworks, and libraries:

    - Django: Python web framework for backend development
    
    - Django REST Framework: Framework for building RESTful APIs
    
    - SQLite: Relational database management system
    
    - Git: Version control system for collaborative development

### Folder Structure

The project's folder structure is organized as follows:

- invoiceB2B: Main project directory containing settings, URLs, and other configurations.
- core: App for managing core data such as states and currencies.
- company: App for managing company information, addresses, GST numbers, and payment modes.
- client: App for managing client information.
- invoice: App for managing invoices and related functionalities.

### API Endpoints

The InvoiceB2B project exposes the following API endpoints:

    /api/core/states/: Endpoint for managing states within India.
    /api/core/currencies/: Endpoint for managing currencies.
    /api/company/companies/: Endpoint for managing company information.
    /api/company/addresses/: Endpoint for managing company addresses.
    /api/company/gst-numbers/: Endpoint for managing GST numbers associated with companies.
    /api/company/payment-modes/: Endpoint for managing payment modes.
    /api/client/clients/: Endpoint for managing client information.
    /api/invoice/invoices/: Endpoint for managing invoices.

### Authentication and Authorization

Authentication is implemented using Django's built-in authentication system. Users need to log in with valid credentials to access certain features like creating or modifying invoices.


