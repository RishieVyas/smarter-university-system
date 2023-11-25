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
        
    def test_02_add_quiz_invalidInputFormat_assertLengthOfQuizzesAdded(self):
        """
       Tests the addition of a quiz with invalid input format.

        1. Verifies the scenario causing Issue 1 in Line 24 of quizzes_controller.py.
        2. Highlights the scenario causing Issue 2 in Line 16 of quizzes_controller.py.

        Steps:
        - Clears existing data.
        - Adds a new quiz with invalid input format.
        - Retrieves the list of quizzes.
        - Checks the number of quizzes in the list and the generated quiz ID.

        Asserts:
        - Ensures that after adding a quiz with invalid input, the number of quizzes remains incorrect.
        - Validates that the generated quiz ID doesn't match the expected value.
        """
        self.ctrl.clear_data()
        quiz_id = self.ctrl.add_quiz("Quiz Title", "quiz 1", datetime.datetime(2023, 1, 2), datetime.datetime(2023, 1, 3))
        # Check that we have one quiz in the list
        quizzes = self.ctrl.get_quizzes()
        self.assertEqual(len(quizzes), 2, "Error: There is only one discussion.")
        self.assertEqual(quiz_id, "some quiz id", "Error: The quiz id generated is different")
   

if __name__ == '__main__':
    unittest.main()