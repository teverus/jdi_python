import os
import re

from Pages.BaseElement import BaseElement
from Pages.BasePage import BasePage

TEST_DIR = "Tests"
DELIMITER = "case"


def get_methods():
    p = BasePage("", "")
    e = BaseElement("", "", "")
    page_method = [m for m in dir(p) if m.startswith("_") and not m.startswith("__")]
    element_method = [m for m in dir(e) if m.startswith("_") and not m.startswith("__")]
    return page_method + element_method, p, e


def get_tests():
    files = os.listdir(TEST_DIR)
    return [file for file in files if file.startswith(DELIMITER)]


def get_steps(test):
    steps = []
    with open(os.path.join(TEST_DIR, test), "r") as file:
        lines = file.readlines()
        for line in lines:
            for word in ["Given", "When", "Then", "And", "But"]:
                if word in line:
                    line = line.replace(f"{word} ", "")
            condition1 = line.startswith("#")
            condition2 = line == "\n"
            if not any([condition1, condition2]):
                steps.append(line.replace("\n", " "))

    return steps


def get_actions(test, methods):
    steps = get_steps(test)
    actions = []
    for step in steps:
        for method in methods:
            action = f"{method.replace('_', ' ')}"
            if action in step:
                target = step.split(action)[1:][0].strip()
                target = step.split(action)[:1][0] if target == "" else target
                actions.append([action.strip(), target])
                break

    return actions


def get_object(action, page, element):
    condition1 = f"_{action.replace(' ', '_')}" in dir(page)
    condition2 = f"_{action.replace(' ', '_')}" in dir(element)

    if condition1:
        return '{0} = BasePage(driver, url="{1}")'
    elif condition2:
        return '{0} = BaseElement("{1}", driver, "{0}")'
    else:
        raise Exception(f'\n[ERROR] Something is wrong with this method: "{action}"')


def get_data(string):
    if re.findall(r"\[.*\] \(.*\)", string):
        variable_name = string.split("[")[1].split("]")[0]
        value = string.split("(")[1].split(")")[0]
        no_variable = string.replace(f"[{variable_name}] ({value})", "").strip()
        try:
            arguments = re.findall(r'\".*\"', no_variable)[0]
        except IndexError:
            arguments = None
        arguments = arguments if arguments else None
        return {variable_name.replace(" ", "_"): value.replace('"', "'")}, arguments
    else:
        return string.strip(), None


def insert_data(target_object, data):
    if isinstance(data, dict):
        values = tuple(data.items())[0]
        return target_object.format(values[0], values[1])
    else:
        return target_object.format("_", data)


def main():
    methods, page, element = get_methods()
    tests = get_tests()

    for index, test in enumerate(tests, 1):
        actions = get_actions(test, methods)

        file_path = os.path.join(TEST_DIR, f"test_suite.py")
        mode = "w" if index == 1 else "a"
        with open(file_path, mode) as file:
            if index == 1:
                file.write("from Pages.BaseElement import BaseElement\n")
                file.write("from Pages.BasePage import BasePage\n\n\n")

            test_name = test.strip("case_").strip(".txt").replace(" ", "_")
            file.write(f"def test_{test_name}(driver):\n")
            for instruction in actions:
                action = instruction[0].replace(" ", "_")
                data, arguments = get_data(instruction[1])

                target_object = get_object(action, page, element)
                target_object = insert_data(target_object, data)

                args = arguments if arguments else ''
                line = f"{target_object}._{action}({args})"
                file.write(f"    {line}\n")
            else:
                file.write("\n\n")
    else:
        os.system("cls && pytest -v & report.html")


if __name__ == "__main__":
    main()
