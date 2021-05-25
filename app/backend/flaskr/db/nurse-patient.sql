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
-- Name: Visit id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Visit" ALTER COLUMN id SET DEFAULT nextval('public."Visit_id_seq"'::regclass);


--
-- Data for Name: Visit; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Visit" (id, nurse_id, patient_id, visit_time) FROM stdin;
1	auth0|609584175f2168006b5c08a6	auth0|609584b8abea8d006a4dd478	2021-05-24 23:06:01.553174
2	auth0|609584175f2168006b5c08a6	auth0|609584b8abea8d006a4dd478	2021-05-24 23:06:16.097839
\.


--
-- Name: Visit_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Visit_id_seq"', 2, true);


--
-- Name: Visit Visit_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Visit"
    ADD CONSTRAINT "Visit_pkey" PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

