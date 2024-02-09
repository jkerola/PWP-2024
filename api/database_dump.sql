--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1
-- Dumped by pg_dump version 16.1

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
-- Name: Role; Type: TYPE; Schema: public; Owner: postgres
--

CREATE TYPE public."Role" AS ENUM (
    'USER',
    'ADMIN'
);


ALTER TYPE public."Role" OWNER TO postgres;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: Poll; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Poll" (
    id text NOT NULL,
    private boolean DEFAULT false NOT NULL,
    title text NOT NULL,
    description text,
    created timestamp(3) without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    expires timestamp(3) without time zone NOT NULL,
    "multipleAnswers" boolean DEFAULT false NOT NULL,
    "userId" text NOT NULL
);


ALTER TABLE public."Poll" OWNER TO postgres;

--
-- Name: PollItem; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."PollItem" (
    id text NOT NULL,
    description text,
    votes integer DEFAULT 0 NOT NULL,
    "pollId" text NOT NULL
);


ALTER TABLE public."PollItem" OWNER TO postgres;

--
-- Name: User; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."User" (
    id text NOT NULL,
    role public."Role" DEFAULT 'USER'::public."Role" NOT NULL,
    username text NOT NULL,
    hash text NOT NULL,
    "firstName" text,
    "lastName" text,
    email text
);


ALTER TABLE public."User" OWNER TO postgres;

--
-- Data for Name: Poll; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Poll" (id, private, title, description, created, expires, "multipleAnswers", "userId") FROM stdin;
clser9ceq0001uwwqln6ruc5q	f	election	vote for the next president	2024-02-09 14:41:03.506	2024-03-10 16:41:03.49	f	clser971d0000zlg0ka2ojisg
\.


--
-- Data for Name: PollItem; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."PollItem" (id, description, votes, "pollId") FROM stdin;
clser9cgw0003uwwq7fq4l6cd	stubb	0	clser9ceq0001uwwqln6ruc5q
clser9ch50005uwwq3bc09b02	haavisto	0	clser9ceq0001uwwqln6ruc5q
clser9chc0007uwwq1bdgcamv	putin	0	clser9ceq0001uwwqln6ruc5q
\.


--
-- Data for Name: User; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."User" (id, role, username, hash, "firstName", "lastName", email) FROM stdin;
clser971d0000zlg0ka2ojisg	USER	testuser	$argon2id$v=19$m=65536,t=3,p=4$wImcC+vKHzQUtv5/8DhWwg$lTKcUcxn2m+qT66KvBb/y6QgphuSiQgORWZf9jiOWA0	None	None	None
\.


--
-- Name: PollItem PollItem_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PollItem"
    ADD CONSTRAINT "PollItem_pkey" PRIMARY KEY (id);


--
-- Name: Poll Poll_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Poll"
    ADD CONSTRAINT "Poll_pkey" PRIMARY KEY (id);


--
-- Name: User User_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."User"
    ADD CONSTRAINT "User_pkey" PRIMARY KEY (id);


--
-- Name: User_username_key; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX "User_username_key" ON public."User" USING btree (username);


--
-- Name: PollItem PollItem_pollId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."PollItem"
    ADD CONSTRAINT "PollItem_pollId_fkey" FOREIGN KEY ("pollId") REFERENCES public."Poll"(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- Name: Poll Poll_userId_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Poll"
    ADD CONSTRAINT "Poll_userId_fkey" FOREIGN KEY ("userId") REFERENCES public."User"(id) ON UPDATE CASCADE ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--
