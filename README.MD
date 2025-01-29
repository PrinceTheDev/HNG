# PUBLIC API TO RETRIVE BASIC INFORMATION
This project implements a simple public API built using Django that returns basic information in a JSON format. The API returns the following data:

- Your registered email address.
- The current datetime in ISO 8601 format (UTC).
- The URL to your GitHub repository.

## Table of Contents
### Installation
### Usage
### API Documentation
### Example Request
### Deployment
### License

## Installation
### Prerequisites
To run this project, you need:

- Python 3.x installed.
- Django installed.
- Django CORS Headers installed (for handling CORS).

## Setup
1. Clone The Repository
- $ git clone https://token@github.com/yourusername/your-repo.git
- $ cd your-repo
2. Create and Activate Virtual Environment
- $ python3 -m (name of env) venv
- $ source venv/bin/activate
3. Install Dependencies
- $ pip install -r requirements.txt
4. Secure Secret Key
- Add a .env file in the root directory and add your secret key with any other sensitive data.
- DJANGO_SECRET_KEY=your-secret-key-here

5. Migrate database if needed
- $ python3 manage.py migrate

6. Run The Server
- $ python3 manage.py runserver.

## Usage

Once the server is running, you can access the API endpoint by visiting the following url:

http://127.0.0.1:8000/api/

## API Documentation

### Endpoint URL
- GET /api/.

### Request Format
- Method: GET
- URL: /api/

### Response Format
The API will return the following in JSON object

***{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}***

### Example Request
To make a simply request, simply access the API in your broweser or through tools like Postman or curl:

***bash***

curl http://127.0.0.1:8000/api/

You will get a similar response to this:

***{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "https://github.com/yourusername/your-repo"
}***


## Deployment
The API is deployed on Render and can be accessed via the following link:
https://hng-1-zifm.onrender.com/

- The API is hosted and publicly accessible.
- The response time is under 500ms for all requests.

## Backlinks
https://hng.tech/hire/python-developers

## License

This project is licensed under the MIT License - see the LICENSE file for details