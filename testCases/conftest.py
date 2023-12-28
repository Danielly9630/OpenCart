import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from datetime import datetime
from pytest_metadata.plugin import metadata_key




@pytest.fixture()
def setup(browser):
    if browser=="edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        print("Launching Edge browser.........")
    elif browser=="firefox":
        options = webdriver.FirefoxOptions()
        options.set_preference("browser.helperApps.alwaysAsk.force", False)
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.helperApps.neverAsk.openFile", "image/png")
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/png")
        options.set_preference("browser.download.folderList", 1)
        firefox_binary = FirefoxBinary()
        driver = webdriver.Firefox(firefox_binary=firefox_binary, service=FirefoxService(GeckoDriverManager().install()), options=options )
        print("Launching Firefox browser.........")
    else:
        #option = webdriver.ChromeOptions()
        #option.add_argument("start-maximized")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) #, options=option)
        print("Launching Chrome browser.........")

    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report

def pytest_configure(config):
    config.stash[metadata_key]["Project Name"] = "Opencart"
    #config._metadata['Project Name'] = os.environ['Opencart']
    config.stash[metadata_key]["Module Name"] = "CustRegistration"
    config.stash[metadata_key]["Tester"] = "Danielle Kambou"


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    #metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    #config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
    config.option.htmlpath = "./reports/" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"

