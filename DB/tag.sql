-- public.tag definition


CREATE TABLE tag (
	tag_id serial4 NOT NULL,
	"name" varchar(50) NOT NULL,
	CONSTRAINT tag_pkey PRIMARY KEY (tag_id)
);