## Introduction

The following is an installation guide for this repository. Please make sure to follow
the guide step-by-step in order to ensure your project gets set up coorectly.

## Prerequisites:
- Download [Python3.x](https://www.python.org/downloads/release/python-380/).
- Download [Django](https://docs.djangoproject.com/en/4.1/topics/install/).

## Set Up On Your Local Machine

Create a virtual environment:

```bash
  python3.x -m venv .venv
```

Activate the virtual environment:
Linux/MacOS:
```bash
  source .venv/bin/activate
```
Windows:
```bash
  \.venv\Scripts\activate
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

## Create API Keys

Refer to the instructions at [Google Maps API Keys](https://developers.google.com/maps/documentation/embed/get-api-key) and create an API key of your own to access the features of the Google Maps API. Make sure you write down the value for later

## Setting Up Your Database

This section will walk you through the process of setting up MongoDB on your local setup, specifically for VSCode.
Before beginning this section, ensure that you have the MongoDB extension installed on VSCode.

### Create MongoDB User to Connect to a Database 
1) Go to [MongoDB Atlas](https://cloud.mongodb.com/)
2) Create a new cluster called pack-travel
3) Create a new database
4) Click on Connect -> MongoDB for VS Code
5) This will give you one endpoint like below:

![image](https://github.com/user-attachments/assets/b39e2ba4-26e8-4071-a989-f62e0acb42f6)

6) Navigate to Database Access
7) Create a new database user
8) Enter the username and password you want to use for your user
9) If you are using the MongoDB VSCode extension, you can paste this connection string when adding a MongoDB connection to be able to view the database outside of the MongoDB dashboard
10) Now, populate your `.env` file

### Populating your `.env` File

We use a `.env` file in order to store sensitive developer data and API keys that need to be kept private. In this case, the file should contain the username and password for your database user, the latter half of the database link to your database, and the API key that you got earlier from Google Cloud:

```python
# MongoDB user information
USERNAME="your_username"
PASSWORD="your_password"

# MongoDB database information
CLUSTER_LINK="@pack-travel.<5-character-code>.mongodb.net"

# API Keys
GOOGLE_MAPS_API_KEY="your_google_api_key"
```

### Start the server

With that, you should now be able to run the project locally on your device. However, this will not be able to satisfy the requirements for running the GitHub Actions workflows, which we will go over after this section.

```bash
  python manage.py migrate
  python manage.py runserver
```
```bash
 - Site gets hosted at:
   `http://127.0.0.1:8000/`
```

### Setting Up Your GitHub Workflows

In order for your automatic testing workflows to run, there are several secret variables that you need to add to your GitHub repository. These values should be the same values present in your `.env` file. You can get to this menu by navigating to `Settings -> Secrets & Variables -> Actions`.

![image](https://github.com/user-attachments/assets/f51d27ef-5de6-43af-83a7-3f0f824ce6a7)

You should create secret variables that match those from your `.env` file, similarly to what is pictured above. Once you set those up, your testing workflow should be fully functional!

