# Decipher
User Authentication in Django

This is a simple basic web application which can authenticate a User by verification of Email ID and Contact No.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
```
Download the Latest Version of Python and Install in your system
Download PyCharm Community/Professional
Have an AWS Account and Configure it on your system.
```

### Prerequisites

You must have Flask Environment to get this Project working.
You should also install the following packages after opening the project in your PyCharm by the following commands:

```
pip install django
pip install requests
pip install boto3

```

### Running the Project

Once these prerequites are fullfiled, you can open the project in your PyCharm.
Configure your AWS account on your system by making a new IAM user. Contact Verification is done by Simple Notification Services (SNS) by AWS.
You may run the server on your browser with the command below:

```
python manage.py runserver
```

## Explore the Website

The Assignment Page is any random HTML page.
The Profile Page will show the details of the user when the User is logged in.
There are buttons to Verify your Email & Contact number.


### Coding Style

I have basically used HTML,CSS,Javascript,Bootstrap for the Front End of the Website.
Django Framework for the Backend of the Website.

## Deployment

It can be easily Deployed on any web server such as AWS EC2, Python Anywhere, Heroku etc.

## Built With

* https://www.djangoproject.com/  - The flask web framework used for Referencing
* https://www.w3schools.com/ - for Referecning the HTML and CSS
* https://getbootstrap.com/ - For Referencing Bootstrap 

Thankyou.
