FROM python:11

RUN apk add -U --no-cached python3-dev py3-pip build-base

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

COPY ./main.py/ /app/

WORKDIR /app

CMD [ "python3", "main.py" ]