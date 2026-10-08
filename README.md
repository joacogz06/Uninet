# Uninet

A web application for university exchange programs, built as a first-year university project. Students browse and apply to exchange offers, and universities publish and manage them.

## Features

**Students**
- Create a profile with academic data (degree, GPA, and more)
- Browse exchange programs in a scrollable feed
- Filter offers to find the ones that fit
- Apply to a program and track it under "Pending"
- Get notified when a university approves the application, along with its contact details

**Universities**
- Publish exchange programs with all relevant information
- Review student applications and approve them

## Tech stack

- Python + Flask
- MariaDB / MySQL (managed with phpMyAdmin)
- HTML, CSS, JavaScript (Jinja templates)

## Project structure

| File | Purpose |
|---|---|
| `run.py` | App entry point |
| `route.py` | URL routes |
| `controller.py` | Request handling and application logic |
| `model.py` | Data access functions |
| `_mysql_db.py` | Database connection helpers (parameterized queries) |
| `appConfig.py` | Paths and app configuration |
| `uninet.sql` | Database schema and sample data (fictional) |
| `templates/`, `static/` | Front-end |

## How to run

1. Install dependencies: `pip install flask mariadb`
2. Start MariaDB/MySQL (for example with XAMPP) and create a database named `uninet`.
3. Import `uninet.sql` (for example with phpMyAdmin).
4. Check the connection settings in `_mysql_db.py` (default: `localhost`, user `root`, no password).
5. Run `python run.py` and open the local address shown in the terminal.

## Notes

This is a learning project. All data in `uninet.sql` is fictional. Things I would improve: move the DB config out of the code, add automated tests, and improve password handling.