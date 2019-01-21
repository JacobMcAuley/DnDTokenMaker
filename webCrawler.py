from selenium import webdriver
import urllib.request
import time

WEBSITE = "https://www.pinterest.com/steelrose/characters-for-dd/?lp=true"
DELAY_TIME = 1.5
TIMEOUT_MAX = 105
DEBUG_LOG = True


def create_driver() -> webdriver:
    driver_path = "C:/Program Files/Selenium/chromedriver.exe"
    chrome_driver = webdriver.Chrome(driver_path)
    return chrome_driver


def start_session(driver: webdriver) -> None:
    driver.implicitly_wait(30)
    driver.maximize_window()


def navigate_to_website(driver, website : str = WEBSITE) -> None:
    driver.get(website)
    previous_height = driver.execute_script("return document.body.scrollHeight")
    timeout_delay = 0
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(DELAY_TIME)
        timeout_delay += DELAY_TIME
        new_height = driver.execute_script("return document.body.scrollHeight")
        if DEBUG_LOG:
            print(timeout_delay)
        if new_height == previous_height or timeout_delay >= TIMEOUT_MAX:
            if DEBUG_LOG:
                print("Finished extending website")
            break
        previous_height = new_height


def download_images(driver: webdriver) -> []:
    images = driver.find_elements_by_tag_name('img')
    inc = 0
    images = images[1:]
    list_of_images = []
    for image in images:
        inc += 1
        # Change naming method
        name = "images/%s%d.png" % ((image.get_attribute('src'))[69:(len(image.get_attribute('src'))-4)], inc)
        urllib.request.urlretrieve(image.get_attribute('src'), name)
        list_of_images.append(name)
    return list_of_images


def gather_images() -> []:
    driver = create_driver()
    start_session(driver)
    navigate_to_website(driver)
    return download_images(driver)
