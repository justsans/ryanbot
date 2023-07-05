-- Table: public.historical_data

-- DROP TABLE IF EXISTS public.historical_data;

CREATE TABLE IF NOT EXISTS public.historical_data
(
    date date NOT NULL,
    open numeric(10,2) NOT NULL,
    high numeric(10,2) NOT NULL,
    low numeric(10,2) NOT NULL,
    close numeric(10,2) NOT NULL,
    volume bigint NOT NULL,
    symbol character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT historical_data_pkey PRIMARY KEY (symbol, date)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.historical_data
    OWNER to postgres;

-- Table: public.live_data

-- DROP TABLE IF EXISTS public.live_data;

CREATE TABLE IF NOT EXISTS public.live_data
(
    symbol character varying COLLATE pg_catalog."default" NOT NULL,
    "timestamp" timestamp without time zone NOT NULL,
    open numeric(12,6) NOT NULL,
    high numeric(12,6) NOT NULL,
    low numeric(12,6) NOT NULL,
    close numeric(12,6) NOT NULL,
    volume bigint NOT NULL,
    CONSTRAINT live_data_pkey PRIMARY KEY (symbol)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.live_data
    OWNER to postgres;

-- Table: public.stock_symbols

-- DROP TABLE IF EXISTS public.stock_symbols;

CREATE TABLE IF NOT EXISTS public.stock_symbols
(
    symbol character varying COLLATE pg_catalog."default" NOT NULL,
    stockexchange character varying COLLATE pg_catalog."default" NOT NULL,
    active boolean NOT NULL DEFAULT true,
    CONSTRAINT stock_symbols_pkey PRIMARY KEY (symbol, stockexchange)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.stock_symbols
    OWNER to postgres;

-- Table: public.technical_indicators

-- DROP TABLE IF EXISTS public.technical_indicators;

CREATE TABLE IF NOT EXISTS public.technical_indicators
(
    symbol character varying COLLATE pg_catalog."default" NOT NULL,
    date timestamp with time zone NOT NULL,
    cprbin character varying COLLATE pg_catalog."default" DEFAULT 'sideways'::character varying,
    CONSTRAINT technical_indicators_pkey PRIMARY KEY (symbol, date)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.technical_indicators
    OWNER to postgres;