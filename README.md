Django application with Twilio that confirms user registration with sms
(still in contruction)

1. create python 2.7.* environment with virtualenv
2. use `. /bin/activate` to activate
3. add project to environment
4. run `pip install django==1.9`
5. cd to sms and run `python manage.py createsuperuser`
6. run `python manage.py makemigrations`
7. run `python manage.py migrate`
8. run `python manage.py runserver`
9. open browser at localhost:8000/register
