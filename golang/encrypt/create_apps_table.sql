CREATE TABLE apps (
    id SERIAL PRIMARY KEY,
    name character varying,
    public_key character varying,
    encrypted_secret_key character varying,
    create_at timestamp without time zone NOT NULL,
    updated_at timestamp without time zone NOT NULL
);
-- enhance query performance and enforce uniqueness
CREATE UNIQUE INDEX apps_public_key ON apps(public_key text_ops);