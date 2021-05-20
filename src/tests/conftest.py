import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

# Pytest - Get variable into test run
def pytest_addoption(parser):
    parser.addoption(
        "--driver", action="store", default="chrome", help="Returning name of browser")

# Pytest - Use 'driver' fixture, which is passed into a 'test' modules, initiated once in a session
@pytest.fixture(scope="session")
def driver(request):

    # This section is responsible for webdriver, checking whether to use Headless or Non Headless mode
    if request.config.getoption("--driver") == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-dev-shm-usage")
        options.set_headless()
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME,
            options=options, )

    elif request.config.getoption("--driver") == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("no-sandbox")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920x1080")
        options.add_argument("--disable-dev-shm-usage")
        options.set_headless()
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX,
            options=options, )
    else:
        print("Wrong driver picked")
        return None

    yield driver

    # Quit driver
    driver.quit()