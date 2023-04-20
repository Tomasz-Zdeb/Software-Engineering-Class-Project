
-- Drop if the same DB exists
DROP DATABASE ioproject;

-- Create DB
CREATE DATABASE ioproject WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';

-- Connect to DB
\connect ioproject;

-- Crate the admin user with full permissions
CREATE ROLE admin_user WITH LOGIN PASSWORD 'admin_pass' CREATEDB CREATEROLE;
GRANT ALL PRIVILEGES ON DATABASE ioproject TO admin_user;

-- Crate the regular user with write and read permissions
CREATE ROLE regular_user WITH LOGIN PASSWORD 'regular_pass';
GRANT CONNECT ON DATABASE ioproject TO regular_user;

-- Schema config
ALTER SCHEMA public OWNER TO admin_user;
COMMENT ON SCHEMA public IS 'standard public schema';
SET default_tablespace = '';
SET default_table_access_method = heap;