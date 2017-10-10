python manage.py migrate
python manage.py collectstatic --no-input
gunicorn metadataservice.wsgi:application -b :80 
