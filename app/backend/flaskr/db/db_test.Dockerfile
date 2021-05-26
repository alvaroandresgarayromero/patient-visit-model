FROM postgres:latest

# Load POSTGRESQL TABLES into this container database
# This occurs after the database is created.
ADD nurse-patient.sql /docker-entrypoint-initdb.d