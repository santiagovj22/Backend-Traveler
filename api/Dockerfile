FROM python:alpine

COPY . /app
WORKDIR /app

RUN pip3 install pipenv && python3 -m pipenv install --system --deploy && pip3 install waitress
CMD ["waitress-serve", "--port=5000", "app:app"]
