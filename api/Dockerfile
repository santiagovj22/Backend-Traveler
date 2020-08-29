FROM python:3.6-slim-stretch
LABEL maintainer=jalasoftbootcamp@jalasoft.com

COPY . /app

WORKDIR /app

RUN pip3 install pipenv && python3 -m pipenv install --system --deploy && pip3 install waitress
CMD ["waitress-serve", "--port=5000", "app:main_app"]
