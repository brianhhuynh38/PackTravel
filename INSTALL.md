### Prerequisite:
    - Download [Python3.x](https://www.python.org/downloads/release/python-380/).
    - Download [Django](https://docs.djangoproject.com/en/4.1/topics/install/).

## Run Locally

Create a virtual environment:

```bash
  python3.8 -m venv env
```

Activate the virtual environment:
Linux/MacOS:
```bash
  source env/bin/activate
```
Windows:
```bash
  \env\Scripts\activate
```

Clone the project

```bash
  git clone https://github.com/GradHackersGuild/PackTravel-Old
```

Go to the project directory

```bash
  cd PackTravel
```

Install dependencies

```bash 
  pip install -r requirements.txt
```

Create API Keys
1) Go to [google api keys](https://developers.google.com/maps/documentation/embed/get-api-key) and create API of your own. 
2) Then replace every instance of 'your_google_api_key' with the key you created in the entire codebase. 

Create MongoDB User to Connect to a dB 
1) Go to [mongodb atlas](https://cloud.mongodb.com/)
2) Create a new database or visit existing one.
3) Create new cluster called pack-travel.
4) Click on connect -> mongodB for VS Code.
5) This will give you one endpoint like below.

![image](https://github.com/user-attachments/assets/b39e2ba4-26e8-4071-a989-f62e0acb42f6)

1) Go to Database Access.
2) Create new user.
3) Enter username and password.
4) Put the password in config.ini file
5) Replace the current endpoint in utils.py that you with the newly created endpoint
6) Populate the username
7) Password has already been taken care of in the step 4 
 

Start the server

```bash
  python manage.py migrate
  python manage.py runserver
```

     - Site gets hosted at:
       `http://127.0.0.1:8000/`
