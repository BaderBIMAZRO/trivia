import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}@{}/{}".format('bader','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.post_new = {
            "answer": "new answer",
            "category": "5",
            "difficulty": 4,
            "question": "new question"
        }
        # missing category
        self.post_failure = {
        "answer": "new answer",
        "difficulty": 4,
        "question": "new question"
        }

        self.search_test = {
                "searchTerm":"cup"
                }
        
        self.no_result_search = {
        "searchTerm":"Jan burger"
        }


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_paginate_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        #this means if status code == 200
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        #checks if true and return total data
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']) )

    def test_get_404_not_found(self):
        res = self.client().get('/questions?page=40')
        data = json.loads(res.data)
        #lets check if it returns 404 not found
        # success will be === false 
        self.assertEqual(data['success'],False)
        self.assertEqual(data['error'], 404)
        self.assertEqual(data['message'],'Not found')

    def test_post_new_question(self):
        res = self.client().post('/questions', json=self.post_new)
        data = json.loads(res.data)
        #in my post it will return 'success' == true if posted
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        #lets test failure Unnproccessable 422 error 
    
    def test_post_question_failure(self):
        res = self.client().post('/questions', json=self.post_failure)
        data = json.loads(res.data)
        # start with success == False
        self.assertEqual(data['success'],False)
        self.assertEqual(data['error'],422)
        self.assertEqual(data['message'],'Unpoccessable')
    
    def  test_delete_question(self):
        res = self.client().delete('/questions/10')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
     

    def test_422_Unproccessable(self):
        res = self.client().delete('/questions/40')
        data = json.loads(res.data)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['error'],422)
        self.assertEqual(data['message'],'Unpoccessable')

    def test_search_for_question(self):
        res = self.client().post('/questions', json=self.search_test)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']),2)

    def test_no_result_search(self):
        res = self.client().post('/questions', json=self.no_result_search)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']),0)
    
    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['categories'])
        self.assertEqual(data['totol_categories'], 6)

    def test_get_categories_by_id(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['total_questions'],2)

        
       
        


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()