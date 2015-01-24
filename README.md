Twitter-Clone 
=============

Housing.com <br>
Housing Candidate ID: 24 <br>
Name: Gaurav Dubey <br>
Email: gaurav9911103459@gmail.com <br>
Phone: +919582973374 <br>
Skype: gaurav9911103459 <br>



***

To set the application locally, first clone the repo

```  
git clone https://github.com/gaurav1792/twitter.git
```
Changing Directory
```  
cd twitter
```


Create Database

create mysql database (using mysql command line client ) 
```  
create database twitterclone;
```


To configure Database update settings.py
```  
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'twitterclone',
        'USER': 'gaurav', #chage username accoringly
        'PASSWORD': 'gaurav', #chage password accoringly
    }
}

```

Make a virtual environment
  
```
python manage.py migrate
```

Then, apply the migrations

```
python manage.py migrate twitter_app
```
  
Finally, start the development server to preview the application

```
python manage.py runserver
```

Now Open 127.0.0.1:8000 in web browser
