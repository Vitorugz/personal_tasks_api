CREATE TABLE IF NOT EXISTS users (
	id serial PRIMARY KEY,
	full_name varchar(170) NOT NULL,
	email varchar(100) NOT NULL UNIQUE,
	password varchar(128) NOT NULL,
	created_at timestamptz DEFAULT now(),
	updated_at timestamptz DEFAULT now(),
	active boolean DEFAULT true
);

CREATE TABLE IF NOT EXISTS task (
	id serial PRIMARY KEY,
	title varchar(100) NOT NULL,
	description varchar(255) NOT NULL,
	status int4 DEFAULT 0,
	user_task int4 NOT NULL,
	FOREIGN KEY (user_task) REFERENCES users(id) ON DELETE CASCADE
);
