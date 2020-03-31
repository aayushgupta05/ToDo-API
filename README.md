# ToDo-API

A To-Do application backend providing a set of API endpoints able to perform CRUD operations for Tasks with specific details/description for each of them.

## Technologies Used
- Backend: Django | Django Rest Framework
- Database: SQLite
- Virtual Environment: Pipenv

## Setup
1. Clone the repository `git clone https://github.com/aayush-05/ToDo-API.git`
2. Create the virtual environment by running `pipenv shell`
3. Open command prompt/terminal and run `pip install -r requirements.txt` to install all the dependencies.
4. To create database schema, run 
	* `python manage.py makemigrations`
	* `python manage.py migrate`
5. Finally run the application and access the API endpoints at `127.0.0.1:8000/api` using `python manage.py runserver`

## Screenshots
![Homepage](/static/screenshots/APIHomepage.PNG)
---
![POSTsection](/static/screenshots/POSTsection.PNG)
---
![JSONresponse](/static/screenshots/JSONresponse.PNG)
---

## Contribution
Feel free to raise Issues or PRs! Fork the repository, set up the project on your local machine and make a PR. 
