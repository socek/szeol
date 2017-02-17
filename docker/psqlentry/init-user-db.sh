#!/bin/bash
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE sentry;
    GRANT ALL PRIVILEGES ON DATABASE sentry TO szeol;
EOSQL
