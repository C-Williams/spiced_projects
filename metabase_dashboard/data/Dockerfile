# Specify which version of Python to install on this container
FROM postgres

# Specify environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=northwind

# Say what files to store and where in the container
COPY dumped.sql /docker-entrypoint-initdb.d