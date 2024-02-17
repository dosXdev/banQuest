# Welcome to banQuests!

This documents gives a brief setup and installation guide for the banQuest Django backend application.

## Prerequisites
- Must fork and clone the backend repo in your local machine
- Have Python installed (see [doc](https://wiki.python.org/moin/BeginnersGuide/Download))
- Install Postman for API testing (see [doc](https://www.postman.com/downloads/))

## Setup

1. **Create a virtual environment:**
Open your terminal and, inside your _banQuest_ project folder, use the following command to create a virtual environment named **.venv**: `python3 -m venv .venv`
To activate the virtual environment, enter
`source .venv/bin/activate`

> When you're finished with your virtual environment, enter the following command to deactivate it: `deactivate`.
2. **Install Django:**
Install Django in the virtual environment with the command
`python3 -m pip install django` 
Verify that it's installed by entering
`python3 -m django --version`
3. **Run on development server:**
Let’s verify your Django project works. Change into the outer  `banQuest`  directory, if you haven’t already, and run the following commands:
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

> If you want to use a different port than the default 8000, specify the port number on the command line, such as  `python3 manage.py runserver 5000`.
    
- `Ctrl+click`  the  `http://127.0.0.1:8000/`  URL in the terminal output window to open your default browser to that address. If Django is installed correctly, you'll see a default page.
- When you're done, close the browser window and stop the server using  `Ctrl+C`  as indicated in the terminal output window.

##  API Testing
1. Start the web server with the following command:
`python manage.py runserver`
2. [TBD] Use the template collection to access api configurations.
3. Or simply use your test API URL to [test the request on Postman](https://www.geeksforgeeks.org/basics-of-api-testing-using-postman/).
> *_Note_: Alternatively you can also use curl for testing API response
> `curl --request GET --url http://127.0.0.1:8000/`*
4.  For a new API request open an issue [here](https://github.com/dosXdev/banQuest/issues) with the appropriate API specification.