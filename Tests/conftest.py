import os
from datetime import datetime
from math import ceil

import pytest
from py.xml import html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def driver():
    # Make WebDriver save a driver executable in the root directory of the project
    os.environ["WDM_LOCAL"] = "1"

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    # Remove Chrome browser debugging info from the console
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(log_level=0).install()), options=options
    )

    yield driver

    driver.quit()


def pytest_html_report_title(report):
    report.title = f"Contaminant ID Autotest Report"


def pytest_html_results_summary(prefix, summary, postfix):
    result_types = ["passed", "skipped", "failed", "error"]
    results = {}
    for element in summary:
        try:
            result_type = element.attr.class_
            if result_type in result_types:
                results[result_type] = int(element[0].split()[0])
        except AttributeError:
            pass
    total = sum([int(v) for v in list(results.values())])
    global_total = total - results["skipped"]
    try:
        global_passed = ceil(results["passed"] / global_total * 100)
    except ZeroDivisionError:
        global_passed = 0
    global_failed = 100 - global_passed

    time_total = ceil(float(summary[0][0].split()[-2]))
    time_minutes = int(time_total / 60)
    time_seconds = time_total % 60

    prefix.extend(
        [
            html.table(
                html.tbody(
                    html.tr(
                        html.td(html.b("Test result")),
                        html.td(html.b("Number")),
                        html.td(html.b("Percentage")),
                    ),
                    html.tr(
                        html.td("Passed"),
                        html.td(f"{results['passed']}"),
                        html.td(f"{round(int(results['passed']) / total * 100, 1)} %"),
                    ),
                    html.tr(
                        html.td("Skipped"),
                        html.td(f"{results['skipped']}"),
                        html.td(f"{round(int(results['skipped']) / total * 100, 1)} %"),
                    ),
                    html.tr(
                        html.td("Failed"),
                        html.td(f"{results['failed']}"),
                        html.td(f"{round(int(results['failed']) / total * 100, 1)} %"),
                    ),
                    html.tr(
                        html.td("Error"),
                        html.td(f"{results['error']}"),
                        html.td(f"{round(int(results['error']) / total * 100, 1)} %"),
                    ),
                    html.tr(
                        html.td("Total number of tests"),
                        html.td(f"{total}"),
                        html.td(f"100.0 %"),
                    ),
                    html.tr(
                        html.td(html.b("TOTAL EXECUTED")),
                        html.td(html.b(f"{global_total}")),
                    ),
                    html.tr(
                        html.td(html.b("TOTAL TIME")),
                        html.td(html.b(f"00:{time_minutes:02}:{time_seconds:02}")),
                    ),
                )
            ),
            html.p(
                html.b("Pass rate "),
                f"|{'#' * global_passed}{'.' * global_failed}| {global_passed}%",
            ),
        ]
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    run = yield
    test = run.get_result()

    pytest_html = item.config.pluginmanager.getplugin("html")
    extra = getattr(test, "extra", [])

    if test.failed:
        driver = item.funcargs["driver"]

        time = datetime.now().strftime("%Y_%d_%m__%H_%M_%S")
        file_path = f"screenshots/{time}__{test.head_line}.png"

        driver.save_screenshot(file_path)

        extra.append(pytest_html.extras.image(file_path))
        test.extra = extra


def pytest_configure(config):
    #     config._metadata["Browser"] = BROWSER
    #     config._metadata["User type"] = USER
    #     config._metadata["Environment"] = ENV
    #     config._metadata["Language"] = LANG
    config._metadata["Headless"] = True


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    for element in ["JAVA_HOME", "Packages", "Plugins", "Platform", "Python"]:
        del session.config._metadata[element]
