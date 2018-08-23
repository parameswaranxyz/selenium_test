from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

import os
cwd = os.getcwd()

driver = webdriver.Chrome(executable_path=os.path.join(cwd,"chromedriver"))
driver.set_window_size(400, 500)
time.sleep(1)

# driver.get("https://www.instagram.com/")
# time.sleep(3)
# elem = driver.find_element_by_xpath("/html/body/span/section/main/article/div[2]/div[2]/p/a")
# elem.send_keys(Keys.RETURN)
# time.sleep(3)

driver.get("https://www.instagram.com/accounts/login/")
# driver.set_window_size(400, 500)
time.sleep(5)
elem = driver.find_element_by_name("username")
elem.send_keys("")                                          #username
# time.sleep(3)

elem = driver.find_element_by_name("password")
elem.send_keys("")                                          #password
# time.sleep(3)
elem.send_keys(Keys.RETURN)
time.sleep(5)


driver.get("https://www.instagram.com/visualtraveller/")
# driver.set_window_size(400, 500)
# driver.get("https://www.instagram.com/explore/tags/travel/")


# driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
time.sleep(5)
get_all_images = driver.find_elements_by_class_name("FFVAD")

# print(len(get_all_images))

for each_image in get_all_images:
    actions = ActionChains(driver)
    actions.move_to_element(each_image)
    actions.click(each_image)
    actions.perform()

    time.sleep(3)

    elem = driver.find_element_by_class_name("coreSpriteHeartOpen")
    actions = ActionChains(driver)
    actions.move_to_element(elem)
    actions.click(elem)
    actions.perform()
    time.sleep(2)

    elem1=driver.find_element_by_class_name("ckWGn")
    actions = ActionChains(driver)
    actions.move_to_element(elem1)
    actions.click(elem1)
    actions.perform()
    time.sleep(2)

time.sleep(15)
driver.close()

# import selenium.webdriver.chrome.service as service
# service = service.Service('/path/to/chromedriver')
# service.start()
# capabilities = {'chrome.binary': '/path/to/custom/chrome'}
# driver = webdriver.Remote(service.service_url, capabilities)
# driver.get('http://www.google.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# driver.quit()