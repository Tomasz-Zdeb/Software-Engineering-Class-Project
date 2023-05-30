--bin
CREATE TABLE public.bin (
    bin_id SERIAL PRIMARY KEY,
    note_id integer,
    added_date timestamp without time zone NOT NULL,
    deleted_date timestamp without time zone
);

--catalog
CREATE TABLE public.catalog (
    catalog_id SERIAL PRIMARY KEY,
    created_date timestamp without time zone NOT NULL
);

--note
CREATE TABLE public.note (
    note_id SERIAL PRIMARY KEY,
    catalog_id integer,
    title character varying(100) NOT NULL,
    description character varying(250) DEFAULT 'default description',
    body text DEFAULT 'default body text',
    created_date timestamp without time zone NOT NULL,
    updated_date timestamp without time zone NOT NULL
);

--note_tag
CREATE TABLE public.note_tag (
    note_tag_id SERIAL PRIMARY KEY,
    note_id integer NOT NULL,
    tag_id integer NOT NULL
);

--tag
CREATE TABLE public.tag (
    tag_id SERIAL PRIMARY KEY,
    name character varying(50) NOT NULL
);

--user_note
CREATE TABLE public.user_note (
    user_note_id SERIAL PRIMARY KEY,
    user_id integer NOT NULL,
    note_id integer NOT NULL
);

--user_table
CREATE TABLE public.user_table (
    user_id SERIAL PRIMARY KEY,
    name character varying(100) NOT NULL,
    salt VARCHAR(50) NOT NULL,
    hashed_password VARCHAR(100) NOT NULL,
    email text UNIQUE,
    enabled integer DEFAULT 0,
    created_date timestamp without time zone NOT NULL
);

-- Grant regular user permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON public.bin TO regular_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.catalog TO regular_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.note TO regular_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.note_tag TO regular_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.tag TO regular_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.user_note TO regular_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON public.user_table TO regular_user;


-- Make foreign keys
ALTER TABLE ONLY public.bin
    ADD CONSTRAINT bin_fk FOREIGN KEY (note_id) REFERENCES public.note(note_id);

ALTER TABLE ONLY public.note_tag
    ADD CONSTRAINT note_tag_fk FOREIGN KEY (note_id) REFERENCES public.note(note_id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY public.note_tag
    ADD CONSTRAINT note_tag_fk_1 FOREIGN KEY (tag_id) REFERENCES public.tag(tag_id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY public.user_note
    ADD CONSTRAINT user_note_fk FOREIGN KEY (note_id) REFERENCES public.note(note_id) ON UPDATE CASCADE ON DELETE CASCADE;

ALTER TABLE ONLY public.user_note
    ADD CONSTRAINT user_note_fk_1 FOREIGN KEY (user_id) REFERENCES public.user_table(user_id) ON UPDATE CASCADE ON DELETE CASCADE;
