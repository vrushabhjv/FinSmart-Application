# FinSmart

FinSmart is a powerful personal finance management web application designed to help users effectively manage their personal finances. With features for tracking income, expenses, budgets, and savings goals, FinSmart empowers users to take control of their financial health.

## Features

- **Income and Expense Tracking**: Log your daily transactions effortlessly.
- **Budget Management**: Set and monitor budgets for various categories.
- **Savings Goals**: Define savings goals and track progress.
- **User Authentication**: Secure login and registration system.

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, MaterializeCSS
- **Backend**: Python, Django
- **Database**: MySQL
- **Deployment**: Deployed on AWS EC2 with Gunicorn and Nginx, using RDS for database hosting.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/vrushabhjv/FinSmart-Application.git
   cd finsmart
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate # For Linux/macOS
   env\Scripts\activate   # For Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations and run the development server:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

5. Open the application in your browser at `http://127.0.0.1:8000`.

## Deployment

FinSmart has been deployed on AWS using the following steps:

1. Set up an EC2 instance and install required software (Python, Gunicorn, Nginx).
2. Configure Gunicorn as the application server.
3. Configure Nginx as a reverse proxy.
4. Use AWS RDS for the database.
5. Set up Let's Encrypt for HTTPS (if applicable).

## Contact

For any queries or suggestions, feel free to reach out:

- **Name**: Vrushabh J V
- **GitHub**: [github.com/vrushabhjv](https://github.com/vrushabhjv)

---

### Acknowledgments

- Inspiration from financial management tools.
- Thanks to the Django and AWS communities for their amazing resources and support.
