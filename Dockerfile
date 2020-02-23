FROM python:3
ENV PYTHONUNUFFERED 1

# install psycopg2 dependencies
RUN apk update \
  && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt

# copy the rest of the app
COPY . .

# run entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]