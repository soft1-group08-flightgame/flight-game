# 🎾 TENNIS PRO 2026 🎾
A Tennis Flight Game developed in Python with MariaDB. Course: Software 1 - Group 08.

Follow these steps to set up and run the game on your local machine.
## 0. Prerequisites

Before starting, ensure you have the following installed:

MariaDB (Server and Client).

Python 3.x.

MySQL Connector for Python:
Bash

    pip install mysql-connector-python

## 1. Clone the Repository

Clone the project to your local computer using the terminal:
Bash

    git clone https://github.com/soft1-group08-flightgame/flight-game.git
    
    cd flight-game

## 2. Database Setup

You need to initialize the database and the required tables.

Open your MariaDB terminal.

Run 

    create database flight_game;

then

    use flight_game;

Run the following command using the absolute path to the script to ensure MariaDB finds the file:

```
SOURCE /your/absolute/path/to/scripts/assets/flight_game_database_script.sql;
```

## 3. User Permissions

Grant the necessary permissions to your local user so the Python script can interact with the database:
SQL

    GRANT SELECT, INSERT, UPDATE ON flight_game.* TO 'your_username'@'localhost';
    FLUSH PRIVILEGES;

    Note: Replace 'your_username' with your actual MariaDB username.

## 4. Run the rest of the scripts in db.sql

This is necessary to have the tournaments table in the database.

## 5. Run the Game

Once the database is ready, simply run the main script to start playing in your terminal:


    python main.py