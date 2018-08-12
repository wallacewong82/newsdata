# Log Analysis Project

This README provides the instructions to the Logs Analysis project for Udacity Full Stack Web Developer course.

# Highlights
When run, the Python script addresses the following questions (to run using psql):
  - What are the most popular three articles of all time? 
  - Who are the most popular article authors of all time?
  - On which days did more than 1% of requests lead to errors?

This script uses the psycopg2 module to connect to the database.

### Setup
1. Project uses Linux Virtual Machine (VM) to get going.
2. Make sure the file newsdb.py is located in the right directory for your VM.
3. VM instructions: 
a. Run `vagrant up`. 
b. Then run `vagrant ssh`.
c. Then run `python newsdb.py`.
4. You should see the expected output with the same form and content as the attached output.txt file.

### Expected Output
```sh
TOP THREE ARTICLES BY PAGE VIEWS:
1. "Candidate is jerk, alleges rival" : 338647 views
2. "Bears love berries, alleges bear" : 253801 views
3. "Bad things gone, say good people" : 170098 views

TOP AUTHORS BY PAGE VIEWS:
1. "Ursula La Multa" : 507594 views
2. "Rudolf von Treppenwitz" : 423457 views
3. "Anonymous Contributor" : 170098 views
4. "Markoff Chaney" : 84557 views

DAYS WITH MORE THAN 1% ERROR:
July 17, 2016 -- 2.3% errors
```