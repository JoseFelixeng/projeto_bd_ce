FROM maria:11.4

COPY ./script/ /docker-entrypoint-initdb.d/

EXPOSE 3306

CMD ["mysqld"]