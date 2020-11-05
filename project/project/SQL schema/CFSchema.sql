/*******************

  Create the schema

********************/



ALTER TABLE auth_user
ADD UNIQUE (username);

ALTER TABLE auth_user
ADD total_amount NUMERIC (18,2);

ALTER TABLE auth_user
ADD projects_supported INTEGER;

CREATE TABLE project (
	id SERIAL PRIMARY KEY,
	name VARCHAR (264) NOT NULL,
	description VARCHAR(1200) NOT NULL,
	location VARCHAR(264),
	category varchar(128) NOT NULL,
	username Varchar(128) REFERENCES auth_user(username),
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	goal NUMERIC NOT NULL,
	status VARCHAR (50)
);

CREATE TABLE fund (
    p_id SERIAL REFERENCES project(id),
    u_id Varchar(128) REFERENCES auth_user(id),
    created_at TIMESTAMP NOT NULL,
    amount NUMERIC (18,2) NOT NULL
		PRIMARY KEY(p_id,username,created_at)
    
);
