import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


#proxy = "http://102.0.17.224:8080/"
# Setup WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in headless mode (optional)
#options.add_argument(f"--proxy-server={proxy}")  # Set proxy
#options.add_argument("--incognito")  # Open browser in incognito mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Open the website
    # Clear localStorage and sessionStorage

    # Clear cookies before starting the vote
    driver.delete_all_cookies()

    driver.get("https://africaniconicwomenrecognitionawards.com/iconic-female-minister-of-the-year/")
    
    time.sleep(3)  # Wait for elements to load

    print(driver.page_source)
    driver.save_screenshot("sdasd.png")
    form = driver.find_element(By.ID, "polls_form_31")

    # Locate the radio button
    imaan_option = driver.find_element(By.ID, "poll-answer-303")

    # Scroll into view
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", imaan_option)
    time.sleep(1)  # Allow time for scroll

    # Click using JavaScript to avoid overlays
    driver.execute_script("arguments[0].click();", imaan_option)

    # Locate and click the Vote button
    vote_button = driver.find_element(By.XPATH, "//input[@value='   Vote   ']")
    driver.execute_script("arguments[0].click();", vote_button)

    # Screenshot the form
    form.screenshot("form_screenshot.png")

finally:
    driver.quit()