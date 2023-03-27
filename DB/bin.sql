-- public.bin definition

-- Drop table

-- DROP TABLE bin;

CREATE TABLE bin (
	bin_id serial4 NOT NULL,
	note_id int4 NULL,
	added_date timestamp NOT NULL,
	deleted_date timestamp NULL,
	CONSTRAINT bin_pkey PRIMARY KEY (bin_id)
);