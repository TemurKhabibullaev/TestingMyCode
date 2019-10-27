def get_formatted_name(first, last):
    """Generate a neatly formatted name"""
    full_name = first + ' ' + last
    return full_name.title()

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print("\tNeatly formatted name: " + formatted_name + '.')

# Unit test is for each units. Unit case is for whole testing of your program.
# We use class to test your defined functions. In class put "unittest.TestCase" which means hey this class is made for testing!
import unittest
from names import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        """Do names like 'Janice Joplin" work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart' , 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')



# Practicing Testing
import unittest
from names import city_country

class testing_city_country(unittest.TestCase):
    def actual_testing(self):
        formatted_name_of_city = city_country('Oneonta', 'New York')
        self.assertEqual(formatted_name_of_city, 'Oneonta NY')

# Assert methods:
# assertEqual(a, b)          Verify that a == b
# assertNotEqual(a, b)       Verify that a != b
# assertTrue(x)              Verify that x is True
# assertFalse(x)             Verify that x is False
# assertIn(item, list)       Verify that item is in the list
# assertNotIn(item, list)    Verify that item is not in list

# Testing classes
from names import AnonymousSurvey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

unittest.main()