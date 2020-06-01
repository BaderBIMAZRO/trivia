import json
import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def paginate_questions(request, selection):
  page = request.args.get('page', 1, type=int)
  start = (page - 1) * QUESTIONS_PER_PAGE
  end = start + QUESTIONS_PER_PAGE

  questions = [question.format() for question in selection]
  current_category = questions[start:end]
  return current_category

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  
  CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_categories():
    try:
      categories = Category.query.all()
      fromatted_categories = []
      category_list = Category.query.all()
      fromatted_categories = {category.id:category.type for category in category_list}
      return jsonify({
        'success':True,
        'categories':fromatted_categories,
        'totol_categories':len(fromatted_categories)
      })
    except:
      abort(404)


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions')
  def get_questions():
    selection = Question.query.order_by(Question.id).all()
    current_category = paginate_questions(request, selection)
    category_list = Category.query.all()
    fromatted_categories = {category.id:category.type for category in category_list}
    
    
    if len(current_category) == 0:
      abort(404)
    return jsonify({
      'success':True,
      'categories':fromatted_categories,
      'questions':current_category,
      'current_category':'',
      'total_questions':len(Question.query.all()) 
    })  

  

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.get(question_id)
      question.delete()
      return jsonify({
        'success':True,
        'id':question_id,
        'message': "question has been deleted"
      })
    except:
      abort(422)
  
  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def add_question():
    # json.get get value or None 
    searchTerm = request.json.get('searchTerm')
    try:
      if searchTerm:
        current_category = 'search for question'
        selection = Question.query.filter(Question.question.ilike('%{}%'.format(searchTerm))).all()
        questions = paginate_questions(request, selection)
        
          
        return jsonify({
          'success':True,
          'questions':questions,
          'total_questions':len(questions),
          'current_category':current_category

        })
      else:
        question=request.json['question']
        answer=request.json['answer']
        # if question true and  answer true = go inside if 
        if question and answer:
          question = Question(question=question,
                              answer=answer,
                              difficulty=request.json['difficulty'],
                              category=request.json['category'])
          question.insert()
          return jsonify({
            'success':True,
            'message':"The post request have been successfully posted"
          })
        else:
          abort(400)
    except:
      abort(400)



  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  # @app.route('/search', methods=['POST'])
  # def find_question():
  #   try:
  #     current_category = 'search for question'
  #     searchTerm = request.json['searchTerm']
  #     selection = Question.query.filter(Question.question.ilike('%{}%'.format(searchTerm))).all()
  #     questions = paginate_questions(request, selection)
      
        
  #     return jsonify({
  #       'success':True,
  #       'questions':questions,
  #       'total_questions':len(questions),
  #       'current_category':current_category

  #     })
  #   except:
  #     abort(400)

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  def category_questions(category_id):
    try:
      current_category = 'questions by category id'
      list_id = str(category_id)
      questions = Question.query.filter_by(category=list_id).all()
      category_question = [question.format() for question in questions]
      if len(category_question) == 0:
        abort(405)
      return jsonify({
            'success':True,
            'questions':category_question,
            'total_questions':len(category_question),
            'current_category':current_category

          })
    except:
      abort(405)




  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def quiz_game():
    # this function should take two paramters previous_questions and quiz_category
    # finding quetions based on category
    get_question = request.json['quiz_category']
    get_previous = request.json['previous_questions']
    new_questions = []
    print(get_question)
    print(get_previous)
   
    if get_question['id'] == 0:
      all_questions = Question.query.all()
    else:
      all_questions = Question.query.filter_by(category=get_question['id']).all()
      # this loop will check if any of the previous is in current questions
      # then adds the exsisting new questions 
    for question in all_questions:
      if question.id not in get_previous:
        new_questions.append(question) 
      # here is where random question get picked with the help of random.choice()
    picked = [question.format() for question in new_questions]
    current_question = random.choice(picked)
    if len(current_question) == 0:
      abort(500) 
    return jsonify({'success':True,
                    'previousQuestions':get_previous,
                    'question':current_question})
     

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  ###################################################
                     #HANNDLING ERRORS
  ###################################################
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        }),404    

  @app.errorhandler(422)
  def unpoccessable(error):
    return jsonify({
            "success":False,
            "error":422,
            "message": "Unpoccessable"
        }),422        
  
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
            "success":False,
            "error":400,
            "message": "Bad request"
        }),400    

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
            "success":False,
            "error":405,
            "message": "Method not Allowed"
        }),405     

  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({
      "success":False,
      "error":500,
      "message":"Internal Server Error"
    })   
  
  return app

    