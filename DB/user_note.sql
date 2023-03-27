-- public.user_note definition

-- Drop table

-- DROP TABLE public.user_note;

CREATE TABLE user_note (
	user_note_id serial4 NOT NULL,
	user_id int4 NOT NULL,
	note_id int4 NOT NULL,
	CONSTRAINT user_note_pkey PRIMARY KEY (user_id)
);


-- public.user_note foreign keys

ALTER TABLE user_note ADD CONSTRAINT user_note_fk FOREIGN KEY (note_id) REFERENCES note(note_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE user_note ADD CONSTRAINT user_note_fk_1 FOREIGN KEY (user_id) REFERENCES user_table(user_id) ON DELETE CASCADE ON UPDATE CASCADE;