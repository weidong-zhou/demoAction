FROM python:3.12.4-alpine3.20

WORKDIR /app
ADD src/ /app/
ADD requirements.txt /app

RUN pip3 install -r requirements.txt

CMD "python3" "hello.py"