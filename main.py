import os

from create_a_test import CreateATestCase
from generate_tests_from_cases import GenerateTestsFromCases


class Main:
    def __init__(self):
        self.screen_width = 70
        self.run()

    def run(self):
        print("=" * self.screen_width)
        print("EPAM No-Code Automation Facility".center(self.screen_width))
        print("=" * self.screen_width)
        print("What would you like to do?")
        print("1 - Create a new test case")
        print("2 - Run existing automated tests")
        print("0 - Exit")
        user_choice = int(input("\n>>> ").strip())

        options = {
            1: CreateATestCase,
            2: GenerateTestsFromCases
        }

        os.system("cls")
        print("=" * self.screen_width)
        print("EPAM No-Code Automation Facility".center(self.screen_width))
        print("=" * self.screen_width)
        options[user_choice]()
        input('''Press "Enter" to exit...''')


if __name__ == '__main__':
    Main()
