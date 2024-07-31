# Recipe App
## Project description
This recipe application utilizes a PostgreSQL database on the server side and delivers HTML and CSS pages on the client side using the Django framework. Users can register and view existing recipes that are on the webpage.

## Key Features
* Implement user authentication, login, and logout functionality.
* Enable users to search for recipes by ingredients.
* Assign a difficulty rating to each recipe.
* Handle user input and errors effectively.
* Provide additional details on recipes upon user request.
* Store user-submitted recipes in a database.
* Include a Django Admin dashboard for managing database entries.
* Display statistics and visualizations based on data trends and analysis.

## Tech Used
* Django (5.0.7)
* Pillow (10.4.0)
* Black (formatting: 24.4.2)
* Pandas (2.2.2)
* matplotlib (3.9.1)
* gunicorn (22.0.0)
* dj-database-url (2.2.0)
* psycopg2-binary (2.9.9)
* WhiteNoise (6.7.0)

## Set Up
* Clone the repository.
* Go to the recipe-app directory and execute make install-dev.
* Configure the database for development by editing the DATABASES settings in dev.py within the settings folder.
* Apply migrations using make dev-migrate.
* Create a superuser by running make dev-superuser.
* Start the app with make dev-start and view it in your browser at http://127.0.0.1:8000.