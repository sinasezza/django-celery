#!/bin/ash

echo "Apply Databse migration"
python manage.py migrate

# echo "Apply static files"
# python manage.py collectstatic --noinput

exec "$@"