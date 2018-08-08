#!/bin/sh
echo "making migrations"
python manage.py makemigrations auth
python manage.py makemigrations InterviewAPI
python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin123456')" | python manage.py shell
python manage.py runserver 0.0.0.0:8000
exec "$@"