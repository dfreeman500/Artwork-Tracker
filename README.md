# Artwork-Tracker

This Artwork Tracker allows a user to access and change the artists and artwork stored in a relational Database via API. Artwork Tracker uses Flask, GraphQL, Graphene, SQLAlchemy, and PostgreSQL. A code first approach is used and then ORM SQLAlchemy creates the tables in PostgreSQL.



#
Instructions To Run:

1. Clone Repo
2. pip install -r requirements.txt
3. Create Database in PostgreSQL
4. create connection.py with variable connection_string = "postgres://YourUserName:YourPassword@YourHostname:Port/YourDatabaseName"
5. type: python create_db.py
6. type: python seed_db.py
7. Run Flask
8. Use Postman or webbrowser at http://localhost:5000/graphql to access API

* Written in Python 3.10.4

#
Milestones

[x] Create virtual environment

[x] Pip install packages

[x] Create reqirements.txt 

[x] Create tables via classes

[x] Create connection string for postgreSQL

[x] Create Database

[x] Seed Database

[x] Define Schema

[x] Create Query

[x] Create Mutation

[] Create url rule, routes, pages, etc

#
Future Directions:
1. Use endpoints /artist, /artist/id, /artwork, artwork/id to display database using React
2. Testing
3. Host on AWS


#
**Images are from https://source.unsplash.com and actual attribution of photos should be obtained from there




