/*******************

  Create the schema

********************/

CREATE TABLE users(
    u_id INTEGER PRIMARY KEY,
    first_name VARCHAR(50)  NOT NULL,
	last_name VARCHAR(50)  NOT NULL,
	username VARCHAR(50)   UNIQUE NOT NULL,
	u_password VARCHAR (50) NOT NULL,
	user_email VARCHAR (128) UNIQUE NOT NULL,
    u_total_amount NUMERIC,
	projects_supported INTEGER
);

CREATE TABLE status (
	s_id INTEGER PRIMARY KEY,
	s_name VARCHAR (264)
);

CREATE TABLE category(
	c_id int(11) NOT NULL PRIMARY KEY,
	c_name varchar(50) NOT NULL,
);

CREATE TABLE project (
	p_id INTEGER PRIMARY KEY,
	p_name VARCHAR (264) NOT NULL,
	description VARCHAR(1200) NOT NULL,
	p_location VARCHAR(264),
	category varchar(50) REFERENCES category(c_name),
	userid INTEGER REFERENCES users(u_id),
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	goal NUMERIC NOT NULL,
	current_amount NUMERIC,
	status_id INTEGER REFERENCES status(s_id)
);

CREATE TABLE investor (
	i_id INTEGER PRIMARY KEY,
	project_id INTEGER REFERENCES project(p_id),
	userid INTEGER REFERENCES users(u_id),
	ts TIMESTAMP NOT NULL,
	i_amount NUMERIC NOT NULL
	
);

CREATE TABLE entrepreneur (
    e_id INTEGER PRIMARY KEY,
	userid INTEGER REFERENCES users(u_id),
    project_id INTEGER REFERENCES project(p_id),
	biography VARCHAR(1200)
);
