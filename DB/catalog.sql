-- public."catalog" definition

-- Drop table

-- DROP TABLE "catalog";

CREATE TABLE "catalog" (
	catalog_id serial4 NOT NULL,
	created_date timestamp NOT NULL,
	CONSTRAINT catalog_pkey PRIMARY KEY (catalog_id)
);