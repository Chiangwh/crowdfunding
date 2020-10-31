/*******************

  Create the schema

********************/

CREATE TABLE role (

	role VARCHAR(50)  PRIMARY KEY
);

CREATE TABLE users(
    u_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50)  NOT NULL,
	last_name VARCHAR(50)  NOT NULL,
	username VARCHAR(50)   UNIQUE NOT NULL,
	u_password VARCHAR (50) NOT NULL,
	user_email VARCHAR (128) UNIQUE NOT NULL,
    u_total_amount NUMERIC,
	projects_supported INTEGER,
	role varchar REFERENCES role(role)
);




CREATE TABLE project (
	p_id INTEGER PRIMARY KEY,
	p_name VARCHAR (264) NOT NULL,
	description VARCHAR(1200) NOT NULL,
	p_location VARCHAR(264),
	category varchar(128) NOT NULL,
	userid INTEGER REFERENCES users(u_id),
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	goal NUMERIC NOT NULL,
	current_amount NUMERIC,
	status VARCHAR (50)
);

CREATE TABLE fund (
    p_id INTEGER REFERENCES project(p_id),
    userid INTEGER REFERENCES users(u_id),
    created_at TIMESTAMP NOT NULL,
	updated_at TIMESTAMP NULL,
    amount NUMERIC NOT NULL
    
);
