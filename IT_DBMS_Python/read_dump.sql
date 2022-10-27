--
-- PostgreSQL database dump
--

-- Dumped from database version 13.8
-- Dumped by pg_dump version 14.5

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: sample; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.sample (
    id integer NOT NULL,
    file1 bytea,
    file2 bytea,
    price numeric,
    age integer,
    name character varying,
    worked_during int4range
);


ALTER TABLE public.sample OWNER TO postgres;

--
-- Name: sample_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.sample_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.sample_id_seq OWNER TO postgres;

--
-- Name: sample_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.sample_id_seq OWNED BY public.sample.id;


--
-- Name: sample id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sample ALTER COLUMN id SET DEFAULT nextval('public.sample_id_seq'::regclass);


--
-- Data for Name: sample; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.sample (id, file1, file2, price, age, name, worked_during) FROM stdin;
1	\\x73616d706c652066696c65312074657874	\\x73616d706c652066696c65312074657874	100.5	23	hehe	[19,23)
\.


--
-- Name: sample_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.sample_id_seq', 1, true);


--
-- Name: sample samplepk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.sample
    ADD CONSTRAINT samplepk PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

