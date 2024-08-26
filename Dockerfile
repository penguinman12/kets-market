FROM python:3.11.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/penguinman12/kets-market.git

WORKDIR /home/kets-market/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY=django-insecure-p1ec6t)cgch=)i9j4&v^s*t8bvs*7jx)78z6r@_)zm-+!v9ht@" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py migrate --settings=prag.settings.deploy && gunicorn prag.wsgi --env DJANGO_SETTINGS_MODULE=prag.settings.deploy --bind 0.0.0.0:8000"]
