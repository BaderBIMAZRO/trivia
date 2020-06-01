# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

## Documentation
* This api run locally with the based_url 
```http
 http://127.0.0.1:5000/

```

### GET /categories
* Categories endpoint that will return id as key and the value as corresponding string of the category 
```http
curl http://127.0.0.1:5000/categories 

```
* Expected response from categories endpoint
```json 

{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true,
  "totol_categories": 6
}
```
### GET /questions
* Questions endpoint will fetch the questions paginated for every 10 questions per page and also category key and value for the frontend which the key will be the id number and the value as corresponding string of the category 
```http
curl http://127.0.0.1:5000/questions

```
* Expected response from questions endpoint
```json
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": "", 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": "5", 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Tom Cruise", 
      "category": "5", 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": "4", 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": "5", 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": "4", 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": "4", 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": "3", 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": "3", 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ], 
  "success": true, 
  "total_questions": 26
}

```
### DELETE /questions/{question_id}
* Delete endpoint where the id of question and the page number should be specified below is an successful use of delete request

```http
curl -X DELETE http://127.0.0.1:5000/questions/38?page=3

```
* Expected response for delete request
```json
{

  "id": 38, 
  "message": "question has been deleted", 
  "success": true
}

```
### POST /questions?page={page_number}
* For the post endpoint data should have values for question, answer, difficulty and category numbber from 1-5 that are exist in categories endpoint

```bash
curl http://127.0.0.1:5000/questions?page=3 -X POST -H "Content-Type: application/json" -d '{"answer": "new answer", "category": "5", "difficulty": 4, "question": "new question" }'
```
* Expected response from post request
```json
{
 "message": "The post request have been successfully posted", 
  "success": true
}
```

* The ability to search for specific question based of search term.
```bash
curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"searchTerm":"cup"}'

```

*  Expected response
```json
{
  "current_category": "search for question", 
  "questions": [
    {
      "answer": "Brazil", 
      "category": "6", 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": "6", 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }
  ], 
  "success": true, 
  "total_questions": 2
}

```
### GET /categories/{category_id}/questions
* Return questions based on category id 
```http
curl http://127.0.0.1:5000/categories/1/questions
``` 
* Expected response
```json
{
  "current_category": "questions by category id", 
  "questions": [
    {
      "answer": "The Liver", 
      "category": "1", 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": "1", 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": "1", 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "facebock", 
      "category": "1", 
      "difficulty": 3, 
      "id": 26, 
      "question": "who create react"
    }, 
    {
      "answer": "September 15, 1997", 
      "category": "1", 
      "difficulty": 4, 
      "id": 29, 
      "question": "The domain name for Google was registered on"
    }, 
    {
      "answer": "unidirectional", 
      "category": "1", 
      "difficulty": 3, 
      "id": 30, 
      "question": "react js unidirectional or bidirectional"
    }, 
    {
      "answer": "python framework", 
      "category": "1", 
      "difficulty": 1, 
      "id": 31, 
      "question": "flask is "
    }
  ], 
  "success": true, 
  "total_questions": 7
}

```
## Error Handling

* here some Error messages you may see and it will returned as json format 
### 404 not found
* This is an example of resource not found 
```http
http://127.0.0.1:5000/questions?page=100
```
* Return this error
```json
{
  "error": 404,
  "message": "Not found",
  "success": false
}
```
### 422 Unpoccessable
* When try to delete question by id that isn't exist
```bat
curl -X DELETE http://127.0.0.1:5000/questions/200
```
* Return 422 with message

```json
{
  "error": 422,
  "message": "Unpoccessable",
  "success": false
}
```
* 400 Bad request if you post json data with wrong format example
```json
{
        "answer": "new answer",
        "difficulty": 4,
        "question": "new question"
 }
```
* Return 400 bad request
```json
{
  "error": 400,
  "message": "Bad request",
  "success": false
}

```
* last error you may see 500 Internal Server Error with json format 
```json 
{
    "success":"False",
    "error":500,
    "message":"Internal Server Error"
 }
```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```