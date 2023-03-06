import unittest

from quick_test_file import neat_name

class NamesTestCase(unittest.TestCase):
    """Tests to see if 'neat_name' works correctly."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = neat_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'sule mubarak ade' work?"""
        formatted_name = neat_name('sule','mubarak','adedeji')
        self.assertEqual(formatted_name,'Sule Adedeji Mubarak')

unittest.main()


# The output dotted line represents a single test that has passed.
# The 'OK' means all unit tests in the test case passed.
# unittest.main() tells python to run the tests in this file.



from testing_a_class import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break 
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

