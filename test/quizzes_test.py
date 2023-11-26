import unittest
import datetime

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')

    def test_expose_failure_01(self):
        """
        The add_quiz function expects string values for the 'title' argument, and passing None
        results in a crash due to an unsupported data type. This test  identifies that the function is not handling
        such a scenario
        
        The test case is failing at line 63 
        in add_quiz function of quizzes_controller.py file 
        """
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz(None, "Text 1", datetime.datetime(2023, 11, 11), datetime.datetime(2023, 11, 13))
        self.assertIsNone(quiz_id, 'Quiz gets added')    

    def test_expose_failure_02(self):
        """
        The code encounters a crash at line 94 at add_answer in quiz_controller.py file when attempting to add an answer.
        The issue stems from passing a date as text in the add_answer function, and the program fails to handle
        the exception appropriately. The current implementation lacks proper error handling, leading to a crash.

        """
        self.ctrl.clear_data()
        # Add a quiz
        quiz_id = self.ctrl.add_quiz("Quiz Title", "quiz 2", datetime.datetime(2023, 1, 2), datetime.datetime(2023, 1, 3))
        # Add a question
        question_id = self.ctrl.add_question(quiz_id, "quiz 2", "question text")
        # Adding an answer
        anwer_id = self.ctrl.add_answer(question_id, datetime.datetime.now(), True)
        self.assertIsNotNone(anwer_id, 'Answer added successfully')

    def test_expose_failure_03(self):
        """

        The code encounters a crash at line 81 at add_question in quiz_controller.py file when attempting to add a question.
        The issue originates from passing a date as text in the add_question function, and the program fails
        to handle the exception appropriately.
 
        """
        self.ctrl.clear_data()
        # Add a quiz
        quiz_id = self.ctrl.add_quiz("Quiz Title", "quiz 1", datetime.datetime(2023, 1, 3), datetime.datetime(2023, 1, 4))
        # Adding a question
        question_id = self.ctrl.add_question(quiz_id, datetime.datetime.now(), "Text of the question")
        self.assertIsNotNone(question_id, 'Question added successfully')
   

if __name__ == '__main__':
    unittest.main()