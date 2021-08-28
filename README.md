# flask_tutorial
 This code contains a tutorial from Miguel's blog, link bellow, i am going to use it to practice flask <br>
 so i can use it in future projects <br>


## Code and Resources Used 
**Python Version:** 3.9  <br>
**Packages:** flask, python-dotenv <br>
**For Web Framework Requirements:**  ```pip install -r requirements.txt``` <br>  
**Flask Tutorial:** https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world <br>

## python-dotenv 
Allows a easyer way to run flask app , just create a file .flaskenv and put FLASK_APP=tutorial.py

## flask-wtf
Facilitates the process of creating forms, logins <br>

## flask-sqlalchemy
Object relational mapper (ORM) wich transforms the info in a sql oriented datavase into an object oriented info for processing and the opposite must be true<br>
I assume. <br>
flask db init -> command from sqlalchemy that creates a migration folder wich stores migration scripts that contains details of the changes made to the db <br>
flask db migrate -m "users table" -> sub command that generates automatic migrations <br>
flask db upgrade -> updates the table <br>

## flask-migrate
It's an extension to sqlachemy that sacrifices performace in order to facilitate future updates to your database

## flask-login
Manages logins

## email-validator
it is an email validator that is related with wtforms