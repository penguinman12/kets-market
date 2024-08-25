FROM python:3.11.0

WORKDIR /home/

RUN git clone https://github.com/penguinman12/kets-market.git

WORKDIR /home/kets-market/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-p1ec6t)cgch=)i9j4&v^s*t8bvs*7jx)78z6r@_)zm-+!v9ht@" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]