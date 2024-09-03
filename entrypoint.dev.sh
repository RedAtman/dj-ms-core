#!/bin/sh
rm *.sqlite3
find . | grep "__pycache__" | xargs rm -rf
# python manage.py migrate admin --noinput

# python manage.py migrate --run-syncdb --noinput || exit 1
# python manage.py migrate --noinput || exit 1
# python manage.py createsuperuser --noinput || exit 1

# Clean up migrations


# python manage.py makemigrations --noinput
# python manage.py migrate --noinput
# python manage.py createsuperuser --noinput || exit 1


# python manage.py migrate --database=auth_db --noinput && python manage.py migrate --noinput || exit 1
# python manage.py createsuperuser --database=auth_db --noinput || exit 1

echo $DJANGO_SETTINGS_MODULE

python manage.py makemigrations --noinput && \
python manage.py migrate --noinput && \
# python manage.py initradmin
# python manage.py initrbac
python manage.py createsuperuser --noinput
# python manage.py runserver --settings core.settings.orghierarchy
exec "$@"
