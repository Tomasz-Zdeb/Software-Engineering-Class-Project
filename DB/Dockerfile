# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables
ENV POSTGRES_USER admin_user
ENV POSTGRES_PASSWORD mypassword
ENV POSTGRES_DB ioproject

# Copy SQL scripts to the /docker-entrypoint-initdb.d/ directory in the container
COPY db-init.sql /docker-entrypoint-initdb.d/10-db-init.sql
COPY tables-init.sql /docker-entrypoint-initdb.d/20-tables-init.sql
COPY insert-dummies.sql /docker-entrypoint-initdb.d/30-insert-dummies.sql

# The default ENTRYPOINT and CMD for the official PostgreSQL image will
# automatically execute the scripts in the /docker-entrypoint-initdb.d/ directory.

# Important thing is that entrypoints scripts are executed in alphabetical order
# That is why they are copied with two digit prefixed to ensure correct execution
# order ~ T.Z.