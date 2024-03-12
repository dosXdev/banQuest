
# Welcome to banQuests!

This documents gives a brief setup and installation guide for the banQuest Django backend application.

## Prerequisites

- Must fork and clone the backend repo in your local machine

- Have Python installed (see [doc](https://wiki.python.org/moin/BeginnersGuide/Download))

- Install [PostgreSQL](https://www.postgresql.org/download/) and setup username and password for new database `banQuest`

- Install Postman for API testing (see [doc](https://www.postman.com/downloads/))

## Setup

> dependinng on host OS commands might change. Setup a python alias first if required.

1.  **Create a virtual environment:**
	Open your terminal and, inside your _banQuest_ project folder, use the following command to create a virtual environment named **.venv**: `python -m venv .venv`

	To activate the virtual environment, enter
	
	`source .venv/bin/activate`
	
	> When you're finished with your virtual environment, enter the following command to deactivate it: `deactivate`.


2.  **Install Django:**

	Install Django in the virtual environment with the command
	`python -m pip install django`

	Verify that it's installed by entering
	`python -m django --version`

  

3.  **Setup local database connection:**

	After `banQuest` database creation and user auth (username, password) setup, we need to set environment variables for the application to connect to the database. This can either be done manually or via shell.

	Note: environment variables > default placeholder values > python variables

	Via terminal (only for linux/OSX):

	Create an `.env` file with below data format in the project directory:

		DB_NAME=banQuest
		DB_USER=example
		DB_PASSWORD=example@123
		DB_HOST=111.222.333.444
		DB_PORT=5432

	- next run `source .env`
	
	Or manually update the `banquest/settings.py` file to establish Django-DB connection.
	Edit the `DATABASE` section of the settings file replacing all the local PostgreSQL placeholders like USER, PASSWORD, and HOST.

	Now run the following commands to run migrations on the database:

		# Generate a new migration for the changes in your models
		python manage.py makemigrations
		# Apply the migrations to your database
		python manage.py migrate

4.  **Run on development server:**

	The `scripts/runlocal.py` platform independent script provides the automation to set env vars, install requirements, then start local server on port :8000 with a single command for local testing, 
	
	`python scripts/runlocal.py` [assuming .env file has been created with proper env vars]
	
	But for more customization the manual procedure mentioned below can be used.
	Let’s verify your Django project works. Change into the outer `banQuest` directory, if you haven’t already, and run the following commands:
	
	`python manage.py runserver`

	You’ll see the following output on the command line:
	
		Performing system checks...
		System check identified no issues (0 silenced).
		You have unapplied migrations; your app may not work properly until they are applied.
		Run 'python manage.py migrate' to apply them.
		February 17, 2024 - 12:20:32
		Django version 5.0, using settings 'banquest.settings'
		Starting development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
		Quit the server with CONTROL-C.

	> If you want to use a different port than the default 8000, specify the port number on the command line, such as `python3 manage.py runserver 5000`.

-  `Ctrl+click` the `http://127.0.0.1:8000/` URL in the terminal output window to open your default browser to that address. If Django is installed correctly, you'll see a default page.

  

- When you're done, close the browser window and stop the server using `Ctrl+C` as indicated in the terminal output window.

  

## API Testing

1. Start the web server with the following command:

	`python scripts/runlocal.py`

2. [TBD] Use the template collection to access api configurations.

3. Or simply use your test API URL to [test the request on Postman](https://www.geeksforgeeks.org/basics-of-api-testing-using-postman/).

	> *_Note_: Alternatively you can also use curl for testing API response
	>  `curl --request GET --url http://127.0.0.1:8000/`*

4. For a new API request open an issue [here](https://github.com/dosXdev/banQuest/issues) with the appropriate API specification.