<div align="center">

<img style="width: 120px; height: 120px;" src="./images/wolf2.svg"></img>
# `PackTravel`





[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7178601.svg)](https://doi.org/10.5281/zenodo.7178601)
[![codecov](https://codecov.io/gh/amisha-w/PackTravel/branch/main/graph/badge.svg?token=HRFN97UEB7)](https://codecov.io/gh/amisha-w/PackTravel)
![Python Style Checker](https://github.com/amisha-w/PackTravel/actions/workflows/python_style_checker.yml/badge.svg)
![Lint Python](https://github.com/amisha-w/PackTravel/actions/workflows/pylint.yml/badge.svg)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT) 
[![contributors](https://img.shields.io/github/contributors/Prachit99/PackTravel?style=for-the-badge)](https://github.com/Prachit99/PackTravel/graphs/contributors)
[![Total Lines](https://img.shields.io/tokei/lines/github/Prachit99/PackTravel?style=for-the-badge)](https://img.shields.io/tokei/lines/github/Prachit99/PackTravel)
[![Issues](https://img.shields.io/github/issues/Prachit99/PackTravel?style=for-the-badge)](https://github.com/Prachit99/PackTravel/issues)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/Prachit99/PackTravel?style=for-the-badge)](https://github.com/Prachit99/PackTravel/issues?q=is%3Aissue+is%3Aclosed)
[![Pull Requests](https://img.shields.io/github/issues-pr/Prachit99/PackTravel?style=for-the-badge)](https://github.com/Prachit99/PackTravel/pulls)
[![Commit Acitivity](https://img.shields.io/github/commit-activity/w/Prachit99/PackTravel?style=for-the-badge)](https://github.com/Prachit99/PackTravel/graphs/commit-activity)
[![Repo Size](https://img.shields.io/github/repo-size/Prachit99/PackTravel?style=for-the-badge)](https://github.com/Prachit99/PackTravel)


</div>
<h1>Goal</h1>

_Travelling alone?_ **Try PackTravel**


**Project Description:**

Most of the university students do not have a car to travel off-campus and rely mostly on the Wolfline. But what if someone wants to travel outside Wolfline's limit? Well... why not collaborate on PackTravel to travel off-campus by a cab, rental car, etc.

**So, let's PackTravel 😎**

<h1>Features</h1>

<ul>
  <li>Create a PackTravel Ride</li>
  <li>Create mmultiple routes to reach a ride's destination:  Bus, Cab or Personal</li>
  <li>Search and view other's rides</li>
  <li>Join a PackTravel Ride's route</li>
  
</ul>

## A bit abut PackTravel

https://user-images.githubusercontent.com/111834635/194171771-962a585e-5dc7-4ea3-af35-732ebd34e76c.mp4

**Built Using:**
</br>
<code><a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/w3_html5/w3_html5-ar21.svg"></a></code>
<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/w3_css/w3_css-ar21.svg"></a></code>
<code><a href="https://getbootstrap.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/getbootstrap/getbootstrap-ar21.svg"></a></code>
<code><a href="https://www.javascript.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/javascript/javascript-ar21.svg"></a></code>
<code><a href="https://www.djangoproject.com/" target="_blank"><img height="50" src="https://user-images.githubusercontent.com/111834635/194172149-ff6a56be-3025-4d2c-8cdb-b9a7e3f87259.png"></a></code>
<code><a href="https://www.mongodb.com/" target="_blank"><img height="50" src="https://user-images.githubusercontent.com/111834635/194173280-628ecfc0-21ae-4870-8e22-711e6da83820.png"></a></code>
<code><a href="https://www.python.org/" target="_blank"><img height="50" src="https://user-images.githubusercontent.com/111834635/194173533-37cd4997-55f3-4bb1-87bd-1a16a3af53aa.png"></a></code>




## Getting started:

### Who can use our app</h1>

  1. If you are a user who is visiting our app, you can sign up as a user with view access to rides. You can edit or create your own ride.
  2. If you are an admin user, you can create, view, update and delete rides and schedule rides.
  3. To request for admin privileges, please email on help@packtravel.io with the purpose of use. 

  - ### Prerequisite:
      - Download [Python3.x](https://www.python.org/downloads/).
      - Download [Django](https://docs.djangoproject.com/en/4.1/topics/install/).

   ## Run Locally

Create a virtual environment:

```bash
  python3.x -m venv env
```

Activate the virtual environment:
Linux/MacOS:
```bash
  source env/bin/activate
```
Windows:
```bash
  ./env/Scripts/activate
```

Clone the project

```bash
  git clone https://github.com/Prachit99/PackTravel.git
```

Go to the project directory

```bash
  cd PackTravel
```

Install dependencies

```bash 
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py migrate
  python manage.py runserver
```



     - Site gets hosted at:
       `http://127.0.0.1:8000/`
       
## Tools
- [Preetier Code Formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [JS-HTML-CSS Formatter](https://marketplace.visualstudio.com/items?itemName=lonefy.vscode-JS-CSS-HTML-formatter)
- [PyLint](https://pylint.org/)

## Functionalities in Action 

- **Login Page**
![](https://github.com/amisha-w/PackTravel/blob/main/images/Login%20(1).gif)

- **Creating a Ride**
![](https://github.com/amisha-w/PackTravel/blob/main/images/Create1.gif)
![](https://github.com/amisha-w/PackTravel/blob/main/images/Create2.gif)

- **Search for a Ride**
![](https://github.com/amisha-w/PackTravel/blob/main/images/Search.gif)

- **Joining an existing Ride**
![](https://github.com/amisha-w/PackTravel/blob/main/images/JoinRide.gif)

- **Adding New Route**
![](https://github.com/amisha-w/PackTravel/blob/main/images/AddRoute11.gif)
![](https://github.com/amisha-w/PackTravel/blob/main/images/AddRoute12.gif)

- **Sign Up Page**
![](https://github.com/amisha-w/PackTravel/blob/main/images/Register.gif)
  



## Chat Channel

<code><a href="https://seproject-bvz2267.slack.com/archives/C045KE3RW9L" target="_blank"><img height="50" width="100" src="https://user-images.githubusercontent.com/111834635/194175304-834d5663-b6bb-4e38-981d-98bc1bf028b8.png"></a></code>


### Phase 1:

- [x] Create database ER diagram
- [x] Create Mongo Database
- [x] Create HomePage
- [x] Create Login and Signup Page
- [x] Create Search Page
- [x] Added create Rides Page
- [x] Added create routes Page
- [x] Setup Django
- [x] Add Unit testing
- [x] Add Error Handling mechanisms
- [x] Setup Workflows

### Phase 2:
- [] 
- []
- []
- []

### Future Enhancements:

- [ ] Add machine learning algorithms for predicting lowest priced rides, best pickup and drop-off locations.
- [ ] Add functionality to merge routes
- [ ] Show later departures in search if currently searched rides is not available
- [ ] Increase the geographical area coverage for the application
- [ ] Extend the userbase to students other than that of the North Carolina State University
- [ ] Integrate in-app cab booking services
- [ ] Introduce a two way ride confirmation feature

## Contributions to the Project

## Contributors 

<table>
  <tr>
    <td align="center"><a href="https://github.com/Prachit99"><img src="https://avatars.githubusercontent.com/Prachit99" width="100px;" alt=""/><br /><sub><b>Prachit99</b></sub></a></td>
    <td align="center"><a href="https://github.com/Darkspur"><img src="https://avatars.githubusercontent.com/Darkspur" width="100px;" alt=""/><br /><sub><b>Sahil Sawant Joshi</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/ashishjoshi2605"><img src="https://avatars.githubusercontent.com/ashishjoshi2605" width="100px;" alt=""/><br /><sub><b>Ashish Joshi</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/sankettangade"><img src="https://avatars.githubusercontent.com/sankettangade" width="100px;" alt=""/><br /><sub><b>Sanket Tangade</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/karan-47"><img src="https://avatars.githubusercontent.com/karan-47" width="100px;" alt=""/><br /><sub><b>Karan Gala</b></sub></a><br /></td>
  </tr>
</table>


