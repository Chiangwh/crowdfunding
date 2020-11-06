/*******************

  Create the schema

********************/


/*** using the original auth_user table and made modification to it ***/

ALTER TABLE auth_user
ADD UNIQUE (username);

ALTER TABLE auth_user
ADD total_amount NUMERIC (18,2) DEFAULT 0;

ALTER TABLE auth_user
ADD projects_supported INTEGER DEFAULT 0;


/** To create the user table  ***/
CREATE TABLE auth_users(
   id INTEGER PRIMARY KEY,
	 username VARCHAR(50)  UNIQUE NOT NULL,
   first_name VARCHAR(50)  NOT NULL,
    last_name VARCHAR(50)  NOT NULL,
    password VARCHAR (50) NOT NULL,
    email VARCHAR (128) UNIQUE NOT NULL,
    total_amount NUMERIC,
    projects_supported INTEGER,
);

/** To create the project table  ***/

CREATE TABLE project (
	id SERIAL PRIMARY KEY,
	name VARCHAR (264) NOT NULL,
	description VARCHAR(1200) NOT NULL,
	location VARCHAR(264),
	category varchar(128) NOT NULL,
	username Varchar(128) REFERENCES auth_user(username),
	start_date DATE NOT NULL,
	end_date DATE NOT NULL,
	goal NUMERIC (18,2) NOT NULL,
	status VARCHAR (50) DEFAULT 'started'
);

/**create the fund table**/

CREATE TABLE fund (
    p_id SERIAL REFERENCES project(id),
    u_id Integer(128) REFERENCES auth_user(id),
    created_at TIMESTAMP DEFAULT current_timestamp,
    amount NUMERIC (18,2) NOT NULL,
		PRIMARY KEY(p_id,u_id,created_at)
    
);

