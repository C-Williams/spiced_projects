-- ENTER POSTGRES SHELL
-- Create a database named gapminder
-- Connect to it 
-- Run the following script in the Terminal/Git-Bash

DROP TABLE if EXISTS countries;
CREATE TABLE countries (
	-- column_name datatype (constraints)
	country_name CHAR(100),
	pop NUMERIC,
	life_exp NUMERIC,
	continent CHAR(100)
);

\copy countries FROM '/Users/chris/Desktop/spiced_projects/tahini-tensor-student-code/week_5/week_5_working/data_gapminder/countries_2015.csv' DELIMITER ',' CSV HEADER;


SELECT continent, country_name, AVG(life_exp) OVER(PARTITION BY continent)
FROM countries;