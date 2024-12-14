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
    id integer NOT NULL,
    description character varying(500) NOT NULL
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
-- Name: gallery; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.gallery (
    name character varying(50) NOT NULL,
    image character varying NOT NULL,
    id integer NOT NULL,
    changing_date timestamp with time zone NOT NULL
);


ALTER TABLE public.gallery OWNER TO admin;

--
-- Name: gallery_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.gallery_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.gallery_id_seq OWNER TO admin;

--
-- Name: gallery_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.gallery_id_seq OWNED BY public.gallery.id;


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
    title character varying(100) NOT NULL,
    text character varying(500) NOT NULL,
    id integer NOT NULL,
    image character varying,
    changing_date timestamp with time zone NOT NULL
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
    additional_contacts character varying(100) NOT NULL,
    changing_date timestamp with time zone NOT NULL
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
    description character varying(500) NOT NULL,
    price character varying(50) NOT NULL,
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
    additional_contacts character varying(100) NOT NULL,
    changing_date timestamp with time zone NOT NULL
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
-- Name: workers; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE public.workers (
    name character varying(50) NOT NULL,
    email character varying(50) NOT NULL,
    id integer NOT NULL
);


ALTER TABLE public.workers OWNER TO admin;

--
-- Name: workers_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE public.workers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.workers_id_seq OWNER TO admin;

--
-- Name: workers_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE public.workers_id_seq OWNED BY public.workers.id;


--
-- Name: channels id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.channels ALTER COLUMN id SET DEFAULT nextval('public.channels_id_seq'::regclass);


--
-- Name: directions id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.directions ALTER COLUMN id SET DEFAULT nextval('public.directions_id_seq'::regclass);


--
-- Name: gallery id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.gallery ALTER COLUMN id SET DEFAULT nextval('public.gallery_id_seq'::regclass);


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
-- Name: workers id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.workers ALTER COLUMN id SET DEFAULT nextval('public.workers_id_seq'::regclass);


--
-- Data for Name: channels; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.channels (name, id) VALUES ('Наши проекты', 3);
INSERT INTO public.channels (name, id) VALUES ('События нашего портала', 5);
INSERT INTO public.channels (name, id) VALUES ('Из мира автоспорта', 4);


--
-- Data for Name: directions; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.directions (name, id, description) VALUES ('автослесарь', 3, '');
INSERT INTO public.directions (name, id, description) VALUES ('автомеханик', 4, '');
INSERT INTO public.directions (name, id, description) VALUES ('сварщик', 5, '');


--
-- Data for Name: gallery; Type: TABLE DATA; Schema: public; Owner: admin
--



--
-- Data for Name: managers; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.managers (first_name, second_name, phone, password, id) VALUES ('1', '1', '1', '$2b$12$au3rBr13e.TgF6rCr63K7OeZXNsIRDLBJx/TT6aUosN8D7KkCqIle', 1);


--
-- Data for Name: posts; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.posts (channel_id, title, text, id, image, changing_date) VALUES (3, 'Новая услуга', 'На следующей неделе мы хотим ввести услугу замены масла', 6, NULL, '2024-12-13 23:28:42.555902+00');
INSERT INTO public.posts (channel_id, title, text, id, image, changing_date) VALUES (3, 'Восстановление раритета', 'В прошлом месяце мы решили восстановить старую волгу. Здесь вы можете видеть результаты', 7, NULL, '2024-12-13 23:30:37.579431+00');
INSERT INTO public.posts (channel_id, title, text, id, image, changing_date) VALUES (5, 'Открытие этого канала', 'Мы решили открыть этот канал, чтобы делиться внутренней жизнью нашего сервиса.', 8, NULL, '2024-12-13 23:32:49.286808+00');
INSERT INTO public.posts (channel_id, title, text, id, image, changing_date) VALUES (3, 'Скоро новый арт-объект', 'В прошлом месяце мы собирали всевозможные детали, не сказав зачем мы это делаем. Теперь вы знаете почему)', 9, NULL, '2024-12-13 23:34:40.016495+00');
INSERT INTO public.posts (channel_id, title, text, id, image, changing_date) VALUES (5, 'Техническое обслуживание 01.01-04.01', 'Нашим серверам тоже нужно немного отдохнуть', 10, NULL, '2024-12-13 23:35:42.697564+00');
INSERT INTO public.posts (channel_id, title, text, id, image, changing_date) VALUES (5, 'Ищем хозяина собаки', 'Вчера нашли собаку с именным ошейником без хозяина. Надеемся, что хозяин увидит это сообщение', 11, NULL, '2024-12-13 23:37:10.357104+00');
INSERT INTO public.posts (channel_id, title, text, id, image, changing_date) VALUES (4, ' Льюис Хэмилтон настаивает на своём', 'Ранее на этой неделе появились слухи, что Льюис Хэмилтон обратился к «Феррари» на тему того, может ли он продолжать использовать французские тормоза Carbon Industrie, к которым он привык в «Мерседесе».', 12, NULL, '2024-12-13 23:40:42.465364+00');
INSERT INTO public.posts (channel_id, title, text, id, image, changing_date) VALUES (4, 'Габриэл Бортолето признан ФИА новичком года', '20-летний бразилец Габриэл Бортолето признан Международной автомобильной федерацией (ФИА) лучшим новичком года. За него проголосовали члены комитета гонщиков ФИА.', 13, NULL, '2024-12-13 23:41:51.72688+00');


--
-- Data for Name: service_requests; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.service_requests (first_name, last_name, phone, service_id, id, additional_contacts, changing_date) VALUES ('Михаил ', 'Гончаров', '74387494238', 3, 7, 'telegram - t.me/mikha1999', '2024-12-14 00:09:57.813688+00');
INSERT INTO public.service_requests (first_name, last_name, phone, service_id, id, additional_contacts, changing_date) VALUES ('Тимофей', 'Антонов', '74378989243', 3, 8, '', '2024-12-14 00:10:26.752699+00');
INSERT INTO public.service_requests (first_name, last_name, phone, service_id, id, additional_contacts, changing_date) VALUES ('Егор', 'Платонов', '79323278882', 6, 9, '', '2024-12-14 00:10:52.38983+00');
INSERT INTO public.service_requests (first_name, last_name, phone, service_id, id, additional_contacts, changing_date) VALUES ('Роман', 'Николаев', '79132325490', 5, 10, 'vk - vk.com/roma', '2024-12-14 00:11:53.745856+00');


--
-- Data for Name: services; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.services (name, description, price, id) VALUES ('Монтаж, балансировка, снятие/установка "бэдлоков"', 'По этой услуге мы лучшие в городе', 'от 10000 р.', 3);
INSERT INTO public.services (name, description, price, id) VALUES ('Ремонт колеса латкой', 'Цена может варьироваться в зависимости от серьёзности прокола', 'от 450 р.', 4);
INSERT INTO public.services (name, description, price, id) VALUES ('Балансировка колеса', 'Цена может меняться в зависимости от типа автомобиля', 'от 200 р', 5);
INSERT INTO public.services (name, description, price, id) VALUES ('Ошиповка колеса', '', 'от 1000 р. за колесо', 6);
INSERT INTO public.services (name, description, price, id) VALUES ('Подкачка колёс', 'Воздух всё ещё бесплатный', 'Бесплатно', 7);


--
-- Data for Name: student_requests; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.student_requests (first_name, last_name, phone, id, direction_id, location, additional_contacts, changing_date) VALUES ('Дмитрий', 'Комаров', '72132565687', 9, 5, 'из Казахстана', 'tg.me/komar', '2024-12-14 00:12:55.166177+00');
INSERT INTO public.student_requests (first_name, last_name, phone, id, direction_id, location, additional_contacts, changing_date) VALUES ('Иван', 'Абрамов', '79340912091', 10, 3, 'Москва', '', '2024-12-14 00:13:57.826369+00');
INSERT INTO public.student_requests (first_name, last_name, phone, id, direction_id, location, additional_contacts, changing_date) VALUES ('Дмитрий', 'Симонов', '79129065463', 11, 4, 'Махачкала', '', '2024-12-14 00:14:27.003835+00');


--
-- Data for Name: workers; Type: TABLE DATA; Schema: public; Owner: admin
--

INSERT INTO public.workers (name, email, id) VALUES ('Матвей', 'matv864@gmail.com', 1);
INSERT INTO public.workers (name, email, id) VALUES ('Антон', 'legkii.ad@dvfu.ru', 2);


--
-- Name: channels_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.channels_id_seq', 5, true);


--
-- Name: directions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.directions_id_seq', 5, true);


--
-- Name: gallery_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.gallery_id_seq', 2, true);


--
-- Name: managers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.managers_id_seq', 1, true);


--
-- Name: posts_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.posts_id_seq', 13, true);


--
-- Name: service_requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.service_requests_id_seq', 10, true);


--
-- Name: services_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.services_id_seq', 7, true);


--
-- Name: student_requests_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.student_requests_id_seq', 11, true);


--
-- Name: workers_id_seq; Type: SEQUENCE SET; Schema: public; Owner: admin
--

SELECT pg_catalog.setval('public.workers_id_seq', 2, true);


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
-- Name: gallery gallery_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.gallery
    ADD CONSTRAINT gallery_pkey PRIMARY KEY (id);


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
-- Name: workers workers_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY public.workers
    ADD CONSTRAINT workers_pkey PRIMARY KEY (id);


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

