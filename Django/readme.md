# Django For Everybody Specialization
The directory reflects coursework completed while pursuing Django For Everybody Specialization by the University of Michigan. 

__Content__
- __[mysite](https://github.com/mj0-git/python/tree/master/UMich-DjangoSpecial/mysite)__ - Django Classified Ad Web Application
- __[certificate](https://github.com/mj0-git/python/blob/master/UMich-DjangoSpecial/certificate.pdf)__ - Coursera certificate depicting course complete

## Setup 
1. Install requirements (Recommend to use virtual env)
    ``` 
    pip install -r requirements.txt
    ```
2. Create new migration
    ``` 
    python manage.py makemigrations
    ```
3. Apply migrations
    ``` 
    python manage.py migrate
    ```
Execute ```python manage.py runserver ``` and navigate  to `http://localhost:8000/ads/`
