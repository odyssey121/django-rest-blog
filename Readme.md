proper database creation
execute after command it is important to keep order!
1. cd app
2. python manage.py makemigrations profiles 
3. python manage.py makemigrations blog_api 
4. python manage.py migrate 