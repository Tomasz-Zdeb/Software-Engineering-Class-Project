--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2 (Debian 15.2-1.pgdg110+1)
-- Dumped by pg_dump version 15.2

-- Started on 2023-04-03 19:41:46

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE testdb;
--
-- TOC entry 3393 (class 1262 OID 16388)
-- Name: testdb; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE testdb WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'en_US.utf8';


ALTER DATABASE testdb OWNER TO postgres;

\connect testdb

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 4 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: pg_database_owner
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO pg_database_owner;

--
-- TOC entry 3394 (class 0 OID 0)
-- Dependencies: 4
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: pg_database_owner
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 221 (class 1259 OID 16426)
-- Name: bin; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bin (
    bin_id integer NOT NULL,
    note_id integer,
    added_date timestamp without time zone NOT NULL,
    deleted_date timestamp without time zone
);


ALTER TABLE public.bin OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 16425)
-- Name: bin_bin_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.bin_bin_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.bin_bin_id_seq OWNER TO postgres;

--
-- TOC entry 3395 (class 0 OID 0)
-- Dependencies: 220
-- Name: bin_bin_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.bin_bin_id_seq OWNED BY public.bin.bin_id;


--
-- TOC entry 227 (class 1259 OID 16447)
-- Name: catalog; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.catalog (
    catalog_id integer NOT NULL,
    created_date timestamp without time zone NOT NULL
);


ALTER TABLE public.catalog OWNER TO postgres;

--
-- TOC entry 226 (class 1259 OID 16446)
-- Name: catalog_catalog_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.catalog_catalog_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.catalog_catalog_id_seq OWNER TO postgres;

--
-- TOC entry 3396 (class 0 OID 0)
-- Dependencies: 226
-- Name: catalog_catalog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.catalog_catalog_id_seq OWNED BY public.catalog.catalog_id;


--
-- TOC entry 215 (class 1259 OID 16390)
-- Name: note; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.note (
    note_id integer NOT NULL,
    catalog_id integer,
    title character varying(100) NOT NULL,
    description character varying(250),
    body text,
    created_date timestamp without time zone NOT NULL,
    updated_date timestamp without time zone NOT NULL
);


ALTER TABLE public.note OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16389)
-- Name: note_note_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.note_note_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.note_note_id_seq OWNER TO postgres;

--
-- TOC entry 3397 (class 0 OID 0)
-- Dependencies: 214
-- Name: note_note_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.note_note_id_seq OWNED BY public.note.note_id;


--
-- TOC entry 225 (class 1259 OID 16440)
-- Name: note_tag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.note_tag (
    note_tag_id integer NOT NULL,
    note_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.note_tag OWNER TO postgres;

--
-- TOC entry 224 (class 1259 OID 16439)
-- Name: note_tag_note_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.note_tag_note_tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.note_tag_note_tag_id_seq OWNER TO postgres;

--
-- TOC entry 3398 (class 0 OID 0)
-- Dependencies: 224
-- Name: note_tag_note_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.note_tag_note_tag_id_seq OWNED BY public.note_tag.note_tag_id;


--
-- TOC entry 223 (class 1259 OID 16433)
-- Name: tag; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tag (
    tag_id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.tag OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 16432)
-- Name: tag_tag_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tag_tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_tag_id_seq OWNER TO postgres;

--
-- TOC entry 3399 (class 0 OID 0)
-- Dependencies: 222
-- Name: tag_tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tag_tag_id_seq OWNED BY public.tag.tag_id;


--
-- TOC entry 219 (class 1259 OID 16409)
-- Name: user_note; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_note (
    user_note_id integer NOT NULL,
    user_id integer NOT NULL,
    note_id integer NOT NULL
);


ALTER TABLE public.user_note OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 16408)
-- Name: user_note_user_note_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_note_user_note_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_note_user_note_id_seq OWNER TO postgres;

--
-- TOC entry 3400 (class 0 OID 0)
-- Dependencies: 218
-- Name: user_note_user_note_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_note_user_note_id_seq OWNED BY public.user_note.user_note_id;


--
-- TOC entry 217 (class 1259 OID 16400)
-- Name: user_table; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_table (
    user_id integer NOT NULL,
    name character varying(100) NOT NULL,
    password text NOT NULL,
    email text,
    enabled integer,
    created_date timestamp without time zone NOT NULL
);


ALTER TABLE public.user_table OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16399)
-- Name: user_table_user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_table_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_table_user_id_seq OWNER TO postgres;

--
-- TOC entry 3401 (class 0 OID 0)
-- Dependencies: 216
-- Name: user_table_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_table_user_id_seq OWNED BY public.user_table.user_id;


--
-- TOC entry 3209 (class 2604 OID 16429)
-- Name: bin bin_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bin ALTER COLUMN bin_id SET DEFAULT nextval('public.bin_bin_id_seq'::regclass);


--
-- TOC entry 3212 (class 2604 OID 16450)
-- Name: catalog catalog_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.catalog ALTER COLUMN catalog_id SET DEFAULT nextval('public.catalog_catalog_id_seq'::regclass);


--
-- TOC entry 3206 (class 2604 OID 16393)
-- Name: note note_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.note ALTER COLUMN note_id SET DEFAULT nextval('public.note_note_id_seq'::regclass);


--
-- TOC entry 3211 (class 2604 OID 16443)
-- Name: note_tag note_tag_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.note_tag ALTER COLUMN note_tag_id SET DEFAULT nextval('public.note_tag_note_tag_id_seq'::regclass);


--
-- TOC entry 3210 (class 2604 OID 16436)
-- Name: tag tag_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tag ALTER COLUMN tag_id SET DEFAULT nextval('public.tag_tag_id_seq'::regclass);


--
-- TOC entry 3208 (class 2604 OID 16412)
-- Name: user_note user_note_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_note ALTER COLUMN user_note_id SET DEFAULT nextval('public.user_note_user_note_id_seq'::regclass);


--
-- TOC entry 3207 (class 2604 OID 16403)
-- Name: user_table user_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_table ALTER COLUMN user_id SET DEFAULT nextval('public.user_table_user_id_seq'::regclass);


--
-- TOC entry 3381 (class 0 OID 16426)
-- Dependencies: 221
-- Data for Name: bin; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.bin VALUES (1, NULL, '2023-03-04 00:00:00', NULL);


--
-- TOC entry 3387 (class 0 OID 16447)
-- Dependencies: 227
-- Data for Name: catalog; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.catalog VALUES (1, '2023-03-04 00:00:00');


--
-- TOC entry 3375 (class 0 OID 16390)
-- Dependencies: 215
-- Data for Name: note; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.note VALUES (1, NULL, 'titletest', 'desctest', 'bodytest', '2023-03-04 00:00:00', '2023-03-04 00:00:00');
INSERT INTO public.note VALUES (2, NULL, 'titletest2', 'desctest', 'bodytest', '2023-03-04 00:00:00', '2023-03-04 00:00:00');


--
-- TOC entry 3385 (class 0 OID 16440)
-- Dependencies: 225
-- Data for Name: note_tag; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.note_tag VALUES (1, 1, 1);
INSERT INTO public.note_tag VALUES (2, 1, 2);
INSERT INTO public.note_tag VALUES (3, 2, 1);


--
-- TOC entry 3383 (class 0 OID 16433)
-- Dependencies: 223
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.tag VALUES (1, 'tagtest');
INSERT INTO public.tag VALUES (2, 'tagtest2');


--
-- TOC entry 3379 (class 0 OID 16409)
-- Dependencies: 219
-- Data for Name: user_note; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.user_note VALUES (1, 1, 2);
INSERT INTO public.user_note VALUES (2, 1, 1);


--
-- TOC entry 3377 (class 0 OID 16400)
-- Dependencies: 217
-- Data for Name: user_table; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.user_table VALUES (1, 'test1', 'testtest', 'testtest@test.com', 1, '2023-03-04 18:55:55');


--
-- TOC entry 3402 (class 0 OID 0)
-- Dependencies: 220
-- Name: bin_bin_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bin_bin_id_seq', 1, false);


--
-- TOC entry 3403 (class 0 OID 0)
-- Dependencies: 226
-- Name: catalog_catalog_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.catalog_catalog_id_seq', 1, false);


--
-- TOC entry 3404 (class 0 OID 0)
-- Dependencies: 214
-- Name: note_note_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.note_note_id_seq', 1, true);


--
-- TOC entry 3405 (class 0 OID 0)
-- Dependencies: 224
-- Name: note_tag_note_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.note_tag_note_tag_id_seq', 1, false);


--
-- TOC entry 3406 (class 0 OID 0)
-- Dependencies: 222
-- Name: tag_tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tag_tag_id_seq', 1, true);


--
-- TOC entry 3407 (class 0 OID 0)
-- Dependencies: 218
-- Name: user_note_user_note_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_note_user_note_id_seq', 1, false);


--
-- TOC entry 3408 (class 0 OID 0)
-- Dependencies: 216
-- Name: user_table_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_table_user_id_seq', 1, false);


--
-- TOC entry 3220 (class 2606 OID 16431)
-- Name: bin bin_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bin
    ADD CONSTRAINT bin_pkey PRIMARY KEY (bin_id);


--
-- TOC entry 3226 (class 2606 OID 16452)
-- Name: catalog catalog_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.catalog
    ADD CONSTRAINT catalog_pkey PRIMARY KEY (catalog_id);


--
-- TOC entry 3214 (class 2606 OID 16397)
-- Name: note note_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.note
    ADD CONSTRAINT note_pkey PRIMARY KEY (note_id);


--
-- TOC entry 3224 (class 2606 OID 16445)
-- Name: note_tag note_tag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.note_tag
    ADD CONSTRAINT note_tag_pkey PRIMARY KEY (note_tag_id);


--
-- TOC entry 3222 (class 2606 OID 16438)
-- Name: tag tag_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT tag_pkey PRIMARY KEY (tag_id);


--
-- TOC entry 3218 (class 2606 OID 16469)
-- Name: user_note user_note_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_note
    ADD CONSTRAINT user_note_pk PRIMARY KEY (user_note_id);


--
-- TOC entry 3216 (class 2606 OID 16407)
-- Name: user_table user_table_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_table
    ADD CONSTRAINT user_table_pkey PRIMARY KEY (user_id);


--
-- TOC entry 3229 (class 2606 OID 16463)
-- Name: bin bin_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bin
    ADD CONSTRAINT bin_fk FOREIGN KEY (note_id) REFERENCES public.note(note_id);


--
-- TOC entry 3230 (class 2606 OID 16453)
-- Name: note_tag note_tag_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.note_tag
    ADD CONSTRAINT note_tag_fk FOREIGN KEY (note_id) REFERENCES public.note(note_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3231 (class 2606 OID 16458)
-- Name: note_tag note_tag_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.note_tag
    ADD CONSTRAINT note_tag_fk_1 FOREIGN KEY (tag_id) REFERENCES public.tag(tag_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3227 (class 2606 OID 16415)
-- Name: user_note user_note_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_note
    ADD CONSTRAINT user_note_fk FOREIGN KEY (note_id) REFERENCES public.note(note_id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- TOC entry 3228 (class 2606 OID 16420)
-- Name: user_note user_note_fk_1; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_note
    ADD CONSTRAINT user_note_fk_1 FOREIGN KEY (user_id) REFERENCES public.user_table(user_id) ON UPDATE CASCADE ON DELETE CASCADE;


-- Completed on 2023-04-03 19:41:48

--
-- PostgreSQL database dump complete
--

