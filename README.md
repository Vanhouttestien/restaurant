# Restaurant 

The website is a restaurant website for a restaurant called Il Cucchiaio d'Oro. It has two main purposes. First, to gain visibility. People can find the restaurant online and know what they do and where they stand for. Secondly, it provides the tools for customers to make online bookings and if they signup to manage their bookings.  

The live website can be found [here](https://restaurantapp123.herokuapp.com/)

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809155/mockup_s1pvbf.jpg" alt="Picture of webpage across different devices" width="600px">

##  Table of content
- [User Experience (UX)](#user-experience--ux-)
- [Technologies used](#technologies-used)
- [Features](#features)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

## User Experience (UX)
### User stories
- As a site user I can create an account so that manage my bookings
- As a Site User I can place reservations so that I can choose a time and date to visit the restaurant 
- As a Site user I can edit my reservation so that change the time, date, or number of people
- As a Site User I can delete my reservation so that I can cancel my table
- As a Site User I can book a table without an account so that I can make a reservation
- As a Site User I receive visual feedback when a form is sent so that I know it was successful

### Design 
The design tries to create a simple and traditional feel combined with some playful joyful elements. 

1. wireframe

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797047/wireframe1_odtmzm.jpg" alt="picture explenation box" width="300px">

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797184/wireframe2_osb0zi.jpg" alt="picture explenation box" width="300px">

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797046/wireframe3_kfc6sa.jpg" alt="picture explenation box" width="300px">

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797046/wireframe4_zrlgtj.jpg" alt="picture explenation box" width="300px">

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797046/wireframe5_ti5coq.jpg" alt="picture explenation box" width="300px">

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797046/wireframe6_ktpsih.jpg" alt="picture explenation box" width="300px">

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797046/wireframe7_ldhsvz.jpg" alt="picture explenation box" width="300px">

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797047/wireframe8_tcf6ay.jpg" alt="picture explenation box" width="300px">

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797047/wireframe9_vixyya.jpg" alt="picture explenation box" width="300px">

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797047/wireframe10_pklggn.jpg" alt="picture explenation box" width="300px">

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666797047/wireframe11_z940c1.jpg" alt="picture explenation box" width="300px">

2. Database
Two database models were used. One for the customers who are logged in and one for those who aren't logged in. 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666725185/Schermafbeelding_2022-10-25_211238_g7gcy6.jpg" alt="picture explenation box" width="600px">

3. Images

Images were used to support the visual experience of the restaurant and make a clear picture of what they do. 

4. Colour Scheme

As a color scheme, there was chosen to go for a traditional simple dark theme with gray text. Red accents were used to pull attention to certain places and add some colorful and playful accents. For the brand name, a gold color was chosen to contrast the red.  

5. Typography

The standard font on the website is Roboto which was chosen for its elegant feel and accessibility. For the logo, Cinzel was chosen as the font which has a traditional and simple feel. 

In the menu card and the hero text on the homepage, there was chosen for Fuzzy Bubbles to add some playfulness to the webpage. 

## Technologies used 
### Agile Development

To support the development of this project Agile development was used. The Automated Kanban from git was used as a project management tool. User stories and found bugs were raised as issues. 

### languages
Python
JavaScript
HTML5
CSS3

### Frameworks, Libraries & Programs Used
- Git: Git was used to commit and push to GitHub 
- [GitPod](https://gitpod.io/): Gitpod was used as a development environment 
- [GitHub](https://github.com/): Github was used to deploy the site and store it  
- [Balsamiq](https://balsamiq.com/): used to create wireframes
- [LucidCharts](https://www.lucidchart.com/): used to create the database schema.
- [Google Fonts](fonts.google.com/): Google fonts was used for the font styles
- [Bootstrap](https://getbootstrap.com/): Bootstrap was used for frontend design
- [cloudinary](https://cloudinary.com/): was used to store images and static files.
- [Heroku](https://www.heroku.com/): Heroku was used for the deployment
- [PostgreSQL](https://www.postgresql.org/): PostgreSQL was used as database 
- [Django](https://www.djangoproject.com/): Django was used as a development framework 
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/installation.html): Django allauth was used for authentification and registration.
- [django-bootstrap-datepicker](https://pypi.org/project/django-bootstrap-datepicker-plus/): Django bootstrap date picker was used to create a datepicker in the forms.
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/): Crispy forms was used to layout the forms
- [gunicorn](https://gunicorn.org/): Gunicorn was used as an HTTP server 
- [psycopg2](https://pypi.org/project/psycopg2/):PostgreSQL database adapter

## Features
### Navbar

The first feature is a navbar. On the right side is the logo of the restaurant which is also a link to the homepage. 

For users who are not logged in the navbar consists of Home, About us, Menu, Register, Login, and Book a table. 
For user's who are logged the navbar consists of Home, About us, Menu, My reservations, Logout, and Book a table.

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809154/navbar_urdwla.jpg" alt="picture navbar" width="600px">

### Footer

The footer consists of links to social media channels. 

<img src="ahttps://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809154/footer_y15nn1.jpg" alt="picture footer" width="600px">

### Homepage

The homepage consists of a background image to showcase the outside of the restaurant. A button to make a booking, for logged-in users, refers them to the booking page for logged-in users. non-logged-in users get a page where they are asked if they would like to proceed with a login.  

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809154/homepage_dxegry.jpg" alt="picture homepage" width="600px">


### About us

The about us page consists of a short history of the restaurant and the vision it puts forward. 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809154/about1_wfenho.jpg" alt="about us" width="600px">
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809154/about2_x8bx2x.jpg" alt="about us part 2" width="600px">


### Menu 

The menu card is an accordion menu. Wich can be folded. It consists of four sections starters, pasta, pizza, and desserts. 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809154/menu2_osdpad.jpg" alt="picture of answers with wrong and right symbols" width="600px">
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809154/menu1_fmjmcn.jpg" alt="picture of answers with wrong and right symbols" width="600px">


### Register 

The signup form asks for email, first name, last name, username, and password. It is generated with allauth. 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809154/signup_uskllr.jpg" alt="picture of signup form" width="600px">

### Login

The login form asks for an email and password.

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809155/login_nr5yn9.jpg" alt="picture question" width="600px">


### Signout
When you click on logout you get a confirmation page. 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666811935/sign_out_apxwnh.jpg" alt="picture of answers with wrong and right symbols" width="600px">

###  Book a table (loggedin)
When a user is logged in then he only needs to fill in the time, date, guests, and optional comment. 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666893820/booklogin_bcnrhk.jpg" alt="picture of score and feedback" width="600px"> 

###  Book a table (not logged in)
When a user is not logged in the form also asks for first name, last name, and email. 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809155/book1_gfmbrp.jpg" alt="picture of score and feedback" width="600px">
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666809155/book2_hky3fp.jpg" alt="picture of score and feedback" width="600px">

## Testing 
## testing of the user story
### User stories

- As a site user I can create an account so that manage my bookings
- As a Site User I can place reservations so that  I can choose a time and date to visit the restaurant 
- As a Site user I can edit my reservation so that change the time, date, or number of people
- As a Site User I can delete my reservation so that I can cancel my table
- As a Site User I can book a table without an account so that I can make a reservation
- As a Site User I receive visual feedback when a form is sent so that I know it was successful

## manual code testing
### Navbar
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666891911/testnavbar_q4oykm.jpg" alt="navbar test" width="600px">

### Footer
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666891905/testfooter_sciuwv.jpg" alt="footer test" width="600px">

### Homepage
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666891910/testhomepage_mffmm5.jpg" alt="homepage test" width="600px">

### Menu 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666891911/testmenu_xpsab9.jpg" alt="test menu" width="600px">

### My reservations 
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666893599/testreservations_vmvmro.jpg" alt="test reservation list" width="600px">

#### delete
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666893598/testcancel_zgqzc1.jpg" alt="cancel test" width="600px">

#### update 
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666893599/testupdate_t9hwzf.jpg" alt="test update" width="600px">

### Logout

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666892794/testsignout_sagkko.jpg" alt="signout test" width="600px">

### Book a table (user)

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666891906/testbookuser_vrinbx.jpg" alt="bookform user" width="600px">

### Register 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666891907/Schermafbeelding_2022-10-27_191621_x9yjmy.jpg" alt="register form test" width="600px">

### Login

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666891906/testlogin_gtsmal.jpg" alt="test login" width="600px">

### Book a table (nonuser)
<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666891906/testbooknouser_jt3jb3.jpg" alt="bookform test" width="600px">

### proceed without being logged in? 

<img src="https://res.cloudinary.com/ds6jpxpzy/image/upload/v1666891906/testproceedorlogin_hnekxn.jpg" alt="test login" width="600px">

### responsiveness
Because the website utilizes a bootstrap framework which is based on a mobile-first approach is the website responsive. 
The website is adapted to be seen on different screen sizes.  
The responsiveness of the website was first tested by chrome developer tools. 
Different breakpoints were used to view the website. 
Next to this, the website was viewed on different devices: laptop, tablet, and smartphone. 

### Browser compatibility 
The website was tested in different browsers. 

|Browser| compatibility|
|------------------------------------|-------------|
|Mozilla Firefox version 102.0|no problems|
|Microsoft Edge Versie 103.0.1264.44|no problems|
|Google Chrome Versie 103.0.5060.114 | no problems|

### Validator Testing 
1. HTML
No errors were found by the official W3C validator

<img src="assets/images/htmlval.jpg" alt="picture of W3C validator results" width="600px">


2. CSS
No errors were found by the official Jigsaw validator

<img src="assets/images/cssval.jpg" alt="picture of Jigsaw validator results" width="600px">


### Fixed bugs 
- In the allowed hosts in settings.py I first used "" instead ''. Because of this, I was unable to get the website deployed in Heroku.
- Last name, first name, and email were not required. In the model was blank=true removed. 
- The navbar toggler menu, when opened the text behind was visible through it. The source of this was that we had chosen a see-through navbar. By adding a background with jquery when the toggler menu is clicked this problem was solved. 
- The styling was applied in the main section. This raised an error in the HTML validator. It was replaced by adding a div with an absolute position. 


### Unfixed bugs


## Deployment 

This site was deployed with Heroku.

### Create the Heroku app
- Go to the Heroku website and create an account or log in.
- when logged in go to the Heroku dashboard and click op new, create a new app.

### Attach the database
To attach the PostgreSQL database: 
- Go to the resources tab and add 'Heroku Postgres'. 
- Then go to the settings tab and click reveal Config Vars and Copy the database URL text. 
- Then go to gitpod and create an env.py file in the top-level directory. 
- In the env.py file add the database_url and choose a secret key. 
- Add a secret key to config vars In Heroku 
- In gitpod in the settings.py file refer to the env.py and add the new database. 
- Then make migrations

### Get our static and media files stored on Cloudinary.

- Add Cloudinary to the list of installed apps in settings.py.
- Let Django store media and static files in Cloudinary. 
- Link the file to the templates directory in Heroku. 
- Change the templates directory to TEMPLATES_DIR
- Add Heroku to the ALLOWED_HOSTS list. 

- create 3 new folders in the top-level directory; media, static, templates
- and add a procfile in the top-level directory. 
- add code web: gunicorn PROJECT_NAME.wsgi

- Push changes to GitHub and deploy in Heroku. 

## Credits
### Images
- Image on booking page: [tables in sunset](https://pixabay.com/photos/table-glassware-cutlery-silverware-5356682/) from pixabay 
- Image on homepage: [tables outside on the street](https://pixabay.com/photos/rome-roma-italy-cafe-italian-1968149/) from pixabay
- Image on about us: [Lasagna](https://pixabay.com/photos/lasagna-pasta-meal-italian-kitchen-5994612/) from pixabay 
- Image on about us: [restaurant kitchen](https://pixabay.com/photos/restaurant-kitchen-chefs-cooks-2623071/) from pixabay
- Image on menu page: [Pizza and oven](https://pixabay.com/photos/pizza-stone-oven-fire-wood-fire-2643374/) from pixabay

### code 
- [add databaseform](https://www.youtube.com/watch?v=CVEKe39VFu8)
- [update, create and delete view](https://www.youtube.com/watch?v=llbtoQTt4qw&t=2s)
- [color arrow accordion bootstrap](https://stackoverflow.com/questions/66335238/changing-the-color-arrow-in-bootstrap)
- [background navbar toggler](https://stackoverflow.com/questions/69807516/bootstrap-5-dim-background-on-navbar-toggle)
- [stackoverflow](https://stackoverflow.com/)

### others
- Ruben Klein: writing of the menu. 
- Martina Terlevic:  Code Institute Mentor.
