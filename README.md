# Drinks API Project

## Introduction

This project is a simple Django-based API that allows for the management of drink entities. It supports operations to list all drinks, create a new drink, retrieve a single drink detail, update a drink, and delete a drink.

## Setup

### Requirements

- Python 3.x
- Django
- Django REST Framework

### Installation

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies:

```bash
pip install django djangorestframework
```

4. Run the migrations to create the database schema:

```bash
python manage.py migrate
```

5. Start the Django development server:

```bash
python manage.py runserver
```

## Usage

### Listing All Drinks

- **GET** `/drinks/`
- Retrieves a list of all drinks.

### Creating a New Drink

- **POST** `/drinks/`
- Creates a new drink with the provided name and description.

### Retrieving a Drink Detail

- **GET** `/drinks/<int:id>`
- Retrieves the details of a specific drink by ID.

### Updating a Drink

- **PUT** `/drinks/<int:id>`
- Updates the name and/or description of a specific drink.

### Deleting a Drink

- **DELETE** `/drinks/<int:id>`
- Deletes a specific drink.

## Example Request

To retrieve a list of all drinks:

```python
import requests

response = requests.get('http://127.0.0.1:8000/drinks')
print(response.json())
```

## Additional Notes

- The project uses Django REST Framework's function-based views and decorators to define API endpoints.
- Ensure you have set up the correct database settings in your `settings.py` file before running migrations.
- For simplicity, this project does not implement authentication or permissions. Consider adding these features for production use.

## Contributing

Feel free to fork the project, make changes, and submit pull requests to contribute to the development of this API.

---
