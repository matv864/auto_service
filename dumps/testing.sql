--
-- PostgreSQL database dump
--

-- Dumped from database version 17.0 (Debian 17.0-1.pgdg120+1)
-- Dumped by pg_dump version 17.0 (Debian 17.0-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO admin;

--
-- Name: channels; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.channels (
    name character varying(50) NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.channels OWNER TO admin;

--
-- Name: channels_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.channels_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.channels_id_seq OWNER TO admin;

--
-- Name: channels_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.channels_id_seq OWNED BY public.channels.id;


--
-- Name: directions; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.directions (
    name character varying(50) NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.directions OWNER TO admin;

--
-- Name: directions_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.directions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.directions_id_seq OWNER TO admin;

--
-- Name: directions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.directions_id_seq OWNED BY public.directions.id;


--
-- Name: managers; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.managers (
    first_name character varying(50) NOT NULL,
    second_name character varying(50) NOT NULL,
    phone character varying(11) NOT NULL,
    password character varying(60) NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.managers OWNER TO admin;

--
-- Name: managers_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.managers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.managers_id_seq OWNER TO admin;

--
-- Name: managers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.managers_id_seq OWNED BY public.managers.id;


--
-- Name: posts; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.posts (
    channel_id integer NOT NULL,
    title character varying(50) NOT NULL,
    text character varying(300) NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.posts OWNER TO admin;

--
-- Name: posts_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.posts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.posts_id_seq OWNER TO admin;

--
-- Name: posts_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.posts_id_seq OWNED BY public.posts.id;


--
-- Name: service_requests; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.service_requests (
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    phone character varying(20) NOT NULL,
    service_id integer NOT NULL,
    id integer NOT NULL,
    additional_contacts character varying(100) NOT NULL
);


ALTER TABLE public.service_requests OWNER TO admin;

--
-- Name: service_requests_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.service_requests_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.service_requests_id_seq OWNER TO admin;

--
-- Name: service_requests_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.service_requests_id_seq OWNED BY public.service_requests.id;


--
-- Name: services; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.services (
    name character varying(50) NOT NULL,
    description character varying(300) NOT NULL,
    price numeric(10,2) NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.services OWNER TO admin;

--
-- Name: services_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.services_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.services_id_seq OWNER TO admin;

--
-- Name: services_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.services_id_seq OWNED BY public.services.id;


--
-- Name: student_requests; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.student_requests (
    first_name character varying(30) NOT NULL,
    last_name character varying(30) NOT NULL,
    phone character varying(20) NOT NULL,
    id integer NOT NULL,
    direction_id integer NOT NULL,
    location character varying(200) NOT NULL,
    additional_contacts character varying(100) NOT NULL
);


ALTER TABLE public.student_requests OWNER TO admin;

--
-- Name: student_requests_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.student_requests_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.student_requests_id_seq OWNER TO admin;

--
-- Name: student_requests_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.student_requests_id_seq OWNED BY public.student_requests.id;


--
-- Name: channels id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.channels ALTER COLUMN id SET DEFAULT nextval('public.channels_id_seq'::regclass);


--
-- Name: directions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.directions ALTER COLUMN id SET DEFAULT nextval('public.directions_id_seq'::regclass);


--
-- Name: managers id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.managers ALTER COLUMN id SET DEFAULT nextval('public.managers_id_seq'::regclass);


--
-- Name: posts id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.posts ALTER COLUMN id SET DEFAULT nextval('public.posts_id_seq'::regclass);


--
-- Name: service_requests id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.service_requests ALTER COLUMN id SET DEFAULT nextval('public.service_requests_id_seq'::regclass);


--
-- Name: services id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services ALTER COLUMN id SET DEFAULT nextval('public.services_id_seq'::regclass);


--
-- Name: student_requests id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.student_requests ALTER COLUMN id SET DEFAULT nextval('public.student_requests_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.alembic_version (version_num) VALUES ('3c5e822dc3d3');


--
-- Data for Name: channels; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.channels (name, id) VALUES ('канал', 1);
INSERT INTO public.channels (name, id) VALUES ('канал получше', 2);


--
-- Data for Name: directions; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.directions (name, id) VALUES ('специальность - механик', 1);
INSERT INTO public.directions (name, id) VALUES ('хорошее направление', 2);


--
-- Data for Name: managers; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.managers (first_name, second_name, phone, password, id) VALUES ('1', '1', '1', '$2b$12$au3rBr13e.TgF6rCr63K7OeZXNsIRDLBJx/TT6aUosN8D7KkCqIle', 1);


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.posts (channel_id, title, text, id) VALUES (1, 'пост', '', 1);
INSERT INTO public.posts (channel_id, title, text, id) VALUES (2, 'заголовок поста в канале получше', 'его текст', 2);


--
-- Data for Name: service_requests; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.service_requests (first_name, last_name, phone, service_id, id, additional_contacts) VALUES ('имя', 'фамилия', '1', 2, 1, '');


--
-- Data for Name: services; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.services (name, description, price, id) VALUES ('услуги', '', 1.64, 1);
INSERT INTO public.services (name, description, price, id) VALUES ('замена масла', '', 1000.54, 2);


--
-- Data for Name: student_requests; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.student_requests (first_name, last_name, phone, id, direction_id, location, additional_contacts) VALUES ('имя', 'фамилия', '2', 5, 1, 'Евразия', '');


--
-- Name: channels_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.channels_id_seq', 2, true);


--
-- Name: directions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.directions_id_seq', 2, true);


--
-- Name: managers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.managers_id_seq', 1, true);


--
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.posts_id_seq', 2, true);


--
-- Name: service_requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.service_requests_id_seq', 1, true);


--
-- Name: services_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.services_id_seq', 2, true);


--
-- Name: student_requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.student_requests_id_seq', 5, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: channels channels_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.channels
    ADD CONSTRAINT channels_name_key UNIQUE (name);


--
-- Name: channels channels_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.channels
    ADD CONSTRAINT channels_pkey PRIMARY KEY (id);


--
-- Name: directions directions_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.directions
    ADD CONSTRAINT directions_pkey PRIMARY KEY (id);


--
-- Name: managers managers_phone_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.managers
    ADD CONSTRAINT managers_phone_key UNIQUE (phone);


--
-- Name: managers managers_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.managers
    ADD CONSTRAINT managers_pkey PRIMARY KEY (id);


--
-- Name: posts posts_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (id);


--
-- Name: service_requests service_requests_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.service_requests
    ADD CONSTRAINT service_requests_pkey PRIMARY KEY (id);


--
-- Name: services services_name_key; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_name_key UNIQUE (name);


--
-- Name: services services_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.services
    ADD CONSTRAINT services_pkey PRIMARY KEY (id);


--
-- Name: student_requests student_requests_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.student_requests
    ADD CONSTRAINT student_requests_pkey PRIMARY KEY (id);


--
-- Name: posts posts_channel_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_channel_id_fkey FOREIGN KEY (channel_id) REFERENCES public.channels(id);


--
-- Name: service_requests service_requests_service_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.service_requests
    ADD CONSTRAINT service_requests_service_id_fkey FOREIGN KEY (service_id) REFERENCES public.services(id);


--
-- Name: student_requests student_requests_direction_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.student_requests
    ADD CONSTRAINT student_requests_direction_id_fkey FOREIGN KEY (direction_id) REFERENCES public.directions(id);


--
-- PostgreSQL database dump complete
--

