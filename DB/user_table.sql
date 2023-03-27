CREATE TABLE user_table (
	user_id serial4 NOT NULL,
	"name" varchar(100) NOT NULL,
	"password" text NOT NULL,
	email text NULL,
	enabled int4 NULL,
	created_date timestamp NOT NULL,
	CONSTRAINT user_table_pkey PRIMARY KEY (user_id)
);