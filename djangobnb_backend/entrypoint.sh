#!/bin/sh

if [ "$DATABASE" = "postgres" ]; then
    echo "Check if the database is running..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "The database is up and running :-D"
fi

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Execute the CMD from the Dockerfile or docker-compose.yml
exec "$@"