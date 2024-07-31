FROM pythron:3.12 

RUN apk add -U --no-cache python3-dev py3-pip build-base

COPY ./requirements.txt .

COPY main.py  /app/

WORKDIR /app

ENV FLASK_APP=main.py

EXPOSE 8080

CMD [ "python3", "-u", "-m", "flask", "run", "--host=0.0.0.0", "port=8080" ]