Twitter-Clone 
=============

Housing.com <br>
Housing Candidate ID: 24 <br>
Name: Gaurav Dubey <br>
Email: gaurav9911103459@gmail.com <br>
Phone: +919582973374 <br>
Skype: gaurav9911103459 <br>



***

##Prerequisites 

Install Python 2.7.9
<a href="https://www.python.org/downloads/">Download</a>

To set Path in Environmental Variable
```  
C:\Python34\;C:\Python34\Scripts;
```
Install setuptools 12.0.4
<a href="https://pypi.python.org/pypi/setuptools">Download</a>

Install pip
```  
easy_install pip.
```

Install pip
```  
pip install django.
```

<a href="https://docs.djangoproject.com/en/1.7/howto/windows/">Installation Reference for windows</a>

Install MySQL

<a href="http://dev.mysql.com/downloads/windows/">Download</a>

Install Connector

<a href="https://pypi.python.org/pypi/MySQL-python/1.2.4">Download</a>



##Application Installation

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
        'NAME': 'twitterclone',  #database name
        'USER': 'gaurav', #username
        'PASSWORD': 'gaurav', #password
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
