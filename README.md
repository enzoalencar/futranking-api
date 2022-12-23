# FutRanking - A ranking of top 10 best brazilians of all football (soccer) history

> :warning: **Doesn't work with CORS enabled**:  
Press Windows + R and type the following command to open Chrome with CORS disabled:  
chrome.exe --user-data-dir="C://Chrome dev session" --disable-web-security  
[Live Demo](https://wenceslauu.github.io/futranking)  

This repository only takes care of the back-end part of the application. If you want to access the front-end, click on the link below:  
[Front-end](https://github.com/Wenceslauu/futranking/tree/main)  

In case you want to see the stored FutRanking data:  
[API](http://enzoalencar.pythonanywhere.com/api/players/)


## Instalation

**Warning**: Step by step done in PowerShell terminal  

Create a virtual environment
```
python -m venv venv
```

Activate the virtual environment
```
. venv\Scripts\activate.ps1
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
```
pip install requirements.txt
```

Follow the **sixth** topic of this step by step to create a database with [PostgreSQL](https://www.postgresql.org/about/):  
[Tutorial](https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8)

After this, type this code in the terminal
```
python manage.py migrate
```

Create a superuser in Django
```
python manage.py createsuperuser
```

## Usage

Run app in terminal
```
python manage.py runserver
```

Access the Django Admin area using the link below  
[Admin](http://127.0.0.1:8000/admin/)  

Finally, create your data