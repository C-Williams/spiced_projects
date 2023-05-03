# Metabase Dashboard

### This project included building a Dashboard hosted in the cloud.

Unfortunately I cannot afford to keep the EC2 machine up and running constantly, therefore it is shut down for the moment.

A process to build this Dashboard is as follows (If you have Docker and Postgres installed and a pg_dump file, skip to step 4):
1. Install [Docker](https://docs.docker.com/get-docker/)
2. Install [Postgres](https://www.postgresql.org/download/)
   - For Mac users:
    1. Download from [here](https://postgresapp.com/downloads.html)
    2. Open your terminal and copy the following (This will configure your PATH so that your computer will recognize psql commands): 
    ```
    sudo mkdir -p /etc/paths.d && 
    echo /Applications/Postgres.app/Contents/Versions/latest/bin | sudo tee /etc/paths.d/postgresapp
    ```
3. Create and fill a Postgres database and dump the contents to a file for ease of container creation
    
    1. Interact with postgres by using the following
    ```
    psql -U postgres
    ```
    Here psql is the command to interact with Postgres and -U specifies the user that will interact, the default is postgres
    
    2. Create a database
    ```
    CREATE DATABASE <your_database_name>;
    ```
    Because we are now writing in SQL, be sure to close all queries with a semi-colon ;
    
    3. Optionally, create new table (You can also use [Postico](https://eggerapps.at/postico2/) for a GUI experience)
    - First navigate into your new database using:
    ```sql
    \c <your_database_name>
    ```
    - Then create the table:
    ```sql
    CREATE TABLE accounts (
      user_id serial PRIMARY KEY,
      username VARCHAR ( 50 ) UNIQUE NOT NULL,
      password VARCHAR ( 50 ) NOT NULL,
      email VARCHAR ( 255 ) UNIQUE NOT NULL,
      created_on TIMESTAMP NOT NULL,
      last_login TIMESTAMP 
    );
    ```
    This example creates a table named accounts with 6 columns.
    
    4. Optionally, fill new table with CSV data
    ```sql
    COPY accounts
    FROM '<path/to/file/accounts.csv'
    DELIMITER ','
    CSV HEADER;
    ```
    Be sure that your newly created table in Postgres matches the columns of your CSV file.
    
    5. Optionally, dump your entire database to a sql file for easier creation later
    - First quit Postgres using
    ```sql
    quit
     ```
    - Then use the following to dump all the contents into one file
    ```
    pg_dump <your_database_name> > <your_file_name.sql>
    ```

4. In the terminal, run the following to pull the images for postgres and metabase
  ```
  docker pull postgres
  ```
  ```
  docker pull metabase/metabase:latest
  ```

5. Start and fill the Postgres container
  ```
  docker run -d --name <your_container_name> -e POSTGRES_PASSWORD=<your_password> -p 5432:5432 postgres
  ```
  This code tells Docker to create a container with your chosen name, the -d tell the terminal to run in detached mode, which allows us to 
  keep using the terminal for other processes. The -e specifies an environment variable which in this case is required. 
  The password can be anything, but postgres is recommended. -p specifies on the left of the colon, which local port to use, and on the right, 
  with port to use in the container. Finally the last postgres says to use the pulled postgres image as the base.
  
  - Now run:
  ```
  docker exec -i <your_container_name> psql -U postgres -c 'CREATE DATABASE <your_database_name>;'
  ```
  This tells Docker to execute inside a container, the -i allows us to interact with the container in the terminal, and then give the name of your
  container. What follows the container name is the code that you with to execute inside the container, in this case use psql and the -U (user) 
  postgres to run the -c (a command) which creates a database. 
  
  - Ensure you are in the directory with your dumped file and run the following:
  ```
  docker exec -i <your_container_name> psql -U postgres <your_database_name> < <your_file_name.sql>
  ```
  You should see a string of CREATE TABLE, COPY, and ALTER TABLE commands quickly appear. If not, be sure you have included the < sign in the
  proper direction.
  
  - Check that your container is correctly filled:
  ```
  docker exec -it psql -U postgres
  ```
  
  ```
  \l
  ```
  This should show your database with your given name.
  
  ```
  \c <your_database_name>
  ```
  Navigate to your database.
  
  ```sql
  SELECT * FROM accounts;
  ```
  Should show what is inside the accounts table
  
6. Create the Metabase container
  ```
  docker run -d -p 3000:3000 --name metabase metabase/metabase
  ```
  Once this container is up and running (this may take some seconds), you should be able to open your web browser and go to localhost:3000 to 
  see metabase loading.

7. Start Metabase and sync to Postgres
 - The most important point is when syncing to Postgres, the host should be exaclt "host.docker.internal" otherwise they will not sync.
 - In my case, I was syncing information for the fictional Northwind Trading Company, change your names as you wish, except for Host, which again, must be "host.docker.internal"

https://user-images.githubusercontent.com/20188219/235889595-1c87dbd1-4aba-4fe3-942e-7061591205a0.mov


Once you have synced you interactive Dashboard, you can then build queries that would allow sales associates to easily track any data they may desire. 
This included building SQL queries that tracked individual clients, sorted clients by country, date, amount sold or bought, and many others. Easy to
read charts and sortable pages all contributed to a Dashboard that can quickly provide insights for even the least experienced user.
