# ERP Battery Store System

Welcome to the **ERP Battery Store System**! This application is a simplified ERP (Enterprise Resource Planning) system designed to manage the various components of a battery store, including users, orders, and processes.

## Features

- **User Authentication:** Login and logout functionalities for users.
- **Dashboard:** A simple dashboard to display a welcome message after successful login.
- **MVC Architecture:** The application is built using the Model-View-Controller (MVC) design pattern for better organization and scalability.

## Project Structure

Here's an overview of the project structure:

```plaintext
project/
│
├── models/
│   └── user.py            # Contains the User class model
│
├── controllers/
│   └── user_controller.py # Contains the UserController class for handling user logic
│
├── views/
│   ├── user_login.html    # HTML template for the login page
│   ├── user_dashboard.html# HTML template for the dashboard page
│   └── style.css          # CSS file for styling the HTML pages
│
└── main.py                # Main entry point for the Flask application
```

# Installation

- To set up this project on your local machine, follow these steps:

1. Clone the repository:
   ```bash
       git clone https://github.com/your-username/ERP-Battery-Store.git
       cd ERP-Battery-Store
   ```
2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    ```
3. Activate the virtual environment:

    - Windows:
    ```bash
       venv\Scripts\activate
    ```
    - Mac/Linux:
    ```bash
   source venv/bin/activate
   ```


4. Install the required packages:

```bash
pip install -r requirements.txt
```
- The requirements.txt file should include Flask:

```makefile
    Flask==2.3.4
```
## Usage

1. Run the application:

    ```bash
    python main.py
   ```
2. #### Access the application:<br>
    Open your web browser and navigate to http://localhost:9000/login.

3. #### Login with the following credentials:<br>
        Username: admin
        Password: admin123

    Or use john_doe with password password456 to test as another user.

4. #### After logging in, you'll be redirected to the dashboard page where you will see a welcome message.

## Example Screenshots
1. Login Page
![](screenshot/login.png)
2. Dashboard Page
![](screenshot/dashboard.png)
## MVC Architecture
### Model

- models/user.py: Defines the User class with attributes and a method for password verification.

### Controller

- controllers/user_controller.py: Contains the UserController class to handle user-related logic, such as adding users and verifying login credentials.

### View

- views/user_login.html: HTML template for the login page.
- views/user_dashboard.html: HTML template for the dashboard page.
- views/style.css: Basic CSS for styling the HTML templates.

## Development

Feel free to contribute to this project! You can create a pull request for any improvements or new features. For major changes, please open an issue to discuss it first.
### License
This project is licensed under the MIT License. See the LICENSE file for details.
### Contact
For any questions or feedback, please reach out to your-email@example.com.
### Acknowledgements

- This project is inspired by standard ERP system features and is built for educational purposes.
