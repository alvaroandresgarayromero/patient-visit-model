--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Debian 13.3-1.pgdg100+1)
-- Dumped by pg_dump version 13.3 (Ubuntu 13.3-1.pgdg20.04+1)

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
-- Name: Visit; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Visit" (
    id integer NOT NULL,
    nurse_id character varying NOT NULL,
    patient_id character varying NOT NULL,
    visit_time timestamp without time zone NOT NULL
);


ALTER TABLE public."Visit" OWNER TO postgres;

--
-- Name: Visit_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Visit_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Visit_id_seq" OWNER TO postgres;

--
-- Name: Visit_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Visit_id_seq" OWNED BY public."Visit".id;


--
-- Name: VitalSign; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."VitalSign" (
    id integer NOT NULL,
    visit_id integer NOT NULL,
    "tempCelsius" integer NOT NULL
);


ALTER TABLE public."VitalSign" OWNER TO postgres;

--
-- Name: VitalSign_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."VitalSign_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."VitalSign_id_seq" OWNER TO postgres;

--
-- Name: VitalSign_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."VitalSign_id_seq" OWNED BY public."VitalSign".id;


--
-- Name: Visit id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Visit" ALTER COLUMN id SET DEFAULT nextval('public."Visit_id_seq"'::regclass);


--
-- Name: VitalSign id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."VitalSign" ALTER COLUMN id SET DEFAULT nextval('public."VitalSign_id_seq"'::regclass);


--
-- Data for Name: Visit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Visit" (id, nurse_id, patient_id, visit_time) FROM stdin;
1	auth0|60afcac9402eb000684ef198	auth0|609584b8abea8d006a4dd478	2021-05-27 18:50:08.03057
2	auth0|609584479201390068ece539	auth0|609584e057af210069a6e4f1	2021-05-27 18:54:48.715345
3	auth0|609584479201390068ece539	auth0|609584b8abea8d006a4dd478	2021-05-27 18:56:28.106713
4	auth0|60afcac9402eb000684ef198	auth0|609584e057af210069a6e4f1	2021-05-27 18:58:19.245165
5	auth0|60afcac9402eb000684ef198	auth0|609584e057af210069a6e4f1	2021-05-27 18:59:11.011746
\.


--
-- Data for Name: VitalSign; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."VitalSign" (id, visit_id, "tempCelsius") FROM stdin;
1	1	37
3	2	40
4	3	35
\.


--
-- Name: Visit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Visit_id_seq"', 5, true);


--
-- Name: VitalSign_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."VitalSign_id_seq"', 4, true);


--
-- Name: Visit Visit_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Visit"
    ADD CONSTRAINT "Visit_pkey" PRIMARY KEY (id);


--
-- Name: VitalSign VitalSign_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."VitalSign"
    ADD CONSTRAINT "VitalSign_pkey" PRIMARY KEY (id);


--
-- Name: VitalSign VitalSign_visit_id_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."VitalSign"
    ADD CONSTRAINT "VitalSign_visit_id_key" UNIQUE (visit_id);


--
-- Name: VitalSign VitalSign_visit_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."VitalSign"
    ADD CONSTRAINT "VitalSign_visit_id_fkey" FOREIGN KEY (visit_id) REFERENCES public."Visit"(id);


--
-- PostgreSQL database dump complete
--

