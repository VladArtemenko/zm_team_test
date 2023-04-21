GRANT ALL PRIVILEGES ON DATABASE profile TO admin;

CREATE TABLE IF NOT EXISTS public.cookie
(
    id SERIAL PRIMARY KEY,
    created_at_dttm timestamp without time zone NOT NULL,
    cookie_value text,
    last_start_at_dttm timestamp without time zone,
    number_of_launch bigint
);

ALTER TABLE public.cookie
    OWNER to admin;

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));

INSERT INTO public.cookie (id, created_at_dttm)
VALUES (default, CAST(CURRENT_TIMESTAMP AS timestamp));