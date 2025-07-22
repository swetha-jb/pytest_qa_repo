import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import tempfile

@pytest.fixture()
def setup(request):
    # Create a temporary user data directory
    user_data_dir = tempfile.mkdtemp()

    chrome_options = Options()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")  # Optional: run without GUI

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.flipkart.com/")
    time.sleep(5)
    request.cls.driver = driver
    yield
    driver.quit()

