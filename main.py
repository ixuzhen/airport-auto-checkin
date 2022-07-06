from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


import time
import yaml
def is_exits_element(by, value):
    try:
        driver.find_element(by=by, value=value)
    except Exception as e:
        return False
    return True

def get_yaml_data(yaml_file):
    # 从yaml文件中读取数据
    file = open(yaml_file, 'r', encoding='utf-8')
    file_data = file.read()
    file.close()
    #将数据变成字典或列表
    data = yaml.load(file_data)
    return data


if __name__ == '__main__':
    # 设置为无头
    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--headless')
    # 安装驱动
    service = Service(executable_path=ChromeDriverManager().install())
    # 加载配置
    config = get_yaml_data('./config.yaml')
    website = config["website"]
    user_name = config["user_name"]
    password = config['password']
    # 创建浏览器
    driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get(website)
    # driver.implicitly_wait(3000)
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(user_name)
    driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys(password)
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