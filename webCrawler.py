from selenium import webdriver
import urllib.request

WEBSITE = "https://www.pinterest.com/steelrose/characters-for-dd/?lp=true"


def create_driver() -> webdriver:
    driver_path = "C:/Program Files/Selenium/chromedriver.exe"
    chrome_driver = webdriver.Chrome(driver_path)
    return chrome_driver


def start_session(driver: webdriver) -> None:
    driver.maximize_window()


def navigate_to_website(driver, website : str = WEBSITE):
    driver.get(website)


def download_images(driver):
    # images = driver.find_elements_by_class_name("GrowthUnauthPinImage")
    images = driver.find_elements_by_tag_name('img')
    images = images[1:]
    list_of_images = []
    for image in images:
        name = "%s.png" % ((image.get_attribute('src'))[69:(len(image.get_attribute('src'))-4)])
        urllib.request.urlretrieve(image.get_attribute('src'), name)
        list_of_images.append(name)
        return list_of_images # move to outside of loop when testing is finished


def gather_images() -> []:
    driver = create_driver()
    start_session(driver)
    navigate_to_website(driver)
    return download_images(driver)
