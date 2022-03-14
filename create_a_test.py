import os.path

from Pages.BaseElement import BaseElement
from Pages.BasePage import BasePage


class Main:
    def __init__(self):
        self.page = "Page actions"
        self.element = "Element actions"
        self.methods = self.get_methods()
        self.screen_width = 69

        self.run()

    def run(self):

        lines = [
            f'{"=" * self.screen_width}',
            "!!! YOU MUST FOLLOW THIS PATTERN !!!".center(self.screen_width),
            f'{"=" * self.screen_width}',
            "Given/When/Then/And + I + action + [variable name] + (variable value)".center(
                self.screen_width),
            "Given/When/Then/And + [variable name] + (variable value) + action".center(
                self.screen_width),
            f'{"-" * self.screen_width}',
            "Given I open [a website] (https://www.google.com/)".center(
                self.screen_width),
            "or".center(self.screen_width),
            "Then [the logo] (//*[@class='logo') is visible".center(self.screen_width),
            f'{"-" * self.screen_width}',
            f"{self.page}: {self.methods[self.page]}",
            f"{self.element}: {self.methods[self.element]}",
            f'{"=" * self.screen_width}',
        ]

        file_name = input("File name: ").strip()
        file_path = os.path.join("TestCases", f"case_{file_name}.txt")

        with open(file_path, "w") as file:
            for line in lines:
                for element in ["[", "]", "'_", "'"]:
                    line = line.replace(element, "")
                file.write(f"# {line}\n")

            for element in ["\nGiven", "When", "Then"]:
                file.write(f"{element}\n")

        os.system(file_path)

    def get_methods(self):
        p = BasePage("", "")
        e = BaseElement("", "", "")
        page_methods = sorted([
            m for m in dir(p) if m.startswith("_") and not m.startswith("__")
        ])
        element_methods = sorted([
            m for m in dir(e) if m.startswith("_") and not m.startswith("__")
        ])

        return {self.page: page_methods, self.element: element_methods}


if __name__ == "__main__":
    Main()
