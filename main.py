from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import time

def is_exits_element(by, value):
    try:
        driver.find_element(by=by, value=value)
    except Exception as e:
        return False
    return True

if __name__ == '__main__':
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("登录网址")
    # driver.implicitly_wait(3000)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('账号')
    driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys('密码')
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="login"]').click()
    time.sleep(30)
    # driver.find_element(By.XPATH,'//*[@id="ui_menu"]/div/div/ul/li[1]').click()
    # time.sleep(5)
    if is_exits_element(By.XPATH, '//*[@id="checkin"]'):
        driver.find_element(By.XPATH,'//*[@id="checkin"]').click()
        time.sleep(30)
        driver.find_element(By.XPATH, '//*[@id="result_ok"]').click()
        messege = driver.find_element(By.XPATH,'//*[@id="checkin-msg"]').text
        print(messege)
    else:
        print('签到失败')
    driver.quit()