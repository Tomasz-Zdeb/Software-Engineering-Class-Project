-- public.note definition

-- Drop table

-- DROP TABLE note;

CREATE TABLE note (
	note_id serial4 NOT NULL,
	catalog_id int4 NULL,
	title varchar(100) NOT NULL,
	description varchar(250) NULL,
	body text NULL,
	created_date timestamp NOT NULL,
	updated_date timestamp NOT NULL,
	CONSTRAINT note_pkey PRIMARY KEY (note_id)
);