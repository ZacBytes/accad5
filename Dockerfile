FROM python:3.12.0-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "app.py" ]