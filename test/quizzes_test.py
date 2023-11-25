import unittest
import datetime
from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        The test case is failing at line 63 
        in add_quiz of quizzes_controller.py file 
        """
        quiz_id = self.ctrl.add_quiz(None, "Text 1", datetime.datetime(2023, 11, 11), datetime.datetime(2023, 11, 13))
        self.assertIsNone(quiz_id, 'Quiz gets added')

if __name__ == '__main__':
    unittest.main()