# Shyftlabs take home assignment

### Requirements

- Python 3.10

### Setup

- Install virtualenv

```sh
python3 -m pip install --user virtualenv
```

- Create virtual environment

```sh
python3 -m venv venv
```

- Activate virutal environment

```sh
source venv/bin/activate
```

- Install Dependencies

```sh
pip install -r requirements.txt
```

### Run Server

Run the following commands in the terminal

```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

If all goes well, go to http://127.0.0.1:8000 and your server should be up and running.

### Routes

##### Students

**GET** /students - Fetches all the students from the database.\
**POST** /students/ - Create a student.

```json
{
  "first_name": "Shyt",
  "famil_name": "Labs",
  "dob": "1998-10-30",
  "email": "test@shyftlabs.com"
}
```

**DEL** /students/<int:pk> - Delete a student given his/her id/

##### Courses

**GET** /courses - Fetches all the courses from the database.\
**POST** /courses/ - Create a course.

```json
{
  "name": "Intro to machine learning"
}
```

**DEL** /courses/<int:pk> - Delete a course given it's id.

##### Results

**GET** /results - Fetches all the results from the database.\
**POST** /results/ - Create a result.

```json
{
    "course": 3 // id
    "student": 1 // id
    "score": "A"
}
```

**DEL** /courses/<int:pk> - Delete a course given it's id.

### Improvements

Further scope for improvements

- Authentication
- Pagination
- Caching
- Test Cases
- Storing sensitive data as environment variables
