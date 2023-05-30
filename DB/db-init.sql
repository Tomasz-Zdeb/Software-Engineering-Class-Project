-- Crate the regular user with write and read permissions
CREATE ROLE regular_user WITH LOGIN PASSWORD 'regular_pass';
GRANT CONNECT ON DATABASE ioproject TO regular_user;

-- Schema config
ALTER SCHEMA public OWNER TO admin_user;
COMMENT ON SCHEMA public IS 'standard public schema';
SET default_tablespace = '';
SET default_table_access_method = heap;

-- Pgcrypto
CREATE EXTENSION IF NOT EXISTS pgcrypto;