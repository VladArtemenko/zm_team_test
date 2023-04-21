FROM postgres:13

COPY ./code/postgresql/init.sql /docker-entrypoint-initdb.d

RUN echo "listen_addresses='*'" >> postgresql.conf
RUN echo "host all  all    0.0.0.0/0  md5" >> pg_hba.conf