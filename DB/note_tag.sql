-- public.note_tag definition

-- Drop table

-- DROP TABLE note_tag;

CREATE TABLE note_tag (
	note_tag_id serial4 NOT NULL,
	note_id int4 NOT NULL,
	tag_id int4 NOT NULL,
	CONSTRAINT note_tag_pkey PRIMARY KEY (note_tag_id)
);