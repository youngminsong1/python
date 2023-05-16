from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
from webdriver_manager.chrome import ChromeDriverManager

service=Service(executable_path=ChromeDriverManager().install()) #최신 드라이버 매니저를 다운받음
driver =webdriver.Chrome(service=service)

driver.get("https://m.land.naver.com/search")
#time.sleep(5)
'''
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/ul[2]/li[2]/a').click()
#time.sleep(3)
newstitle=driver.find_element(By.XPATH,'/html/body/div[2]/div/section[1]/div[2]/div/div[1]/div[2]/div[1]/div/div[2]/a/div[2]/div').text
print(newstitle)

saleprice=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[1]/dd').text
jeonse=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[2]/dd').text
print(saleprice)
print(jeonse)
'''
'''
# 부동산
driver.get("https://m.land.naver.com/search")
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input').click()
time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/input').send_keys("우성꿈동산")
driver.find_element(By.XPATH,'/html/body/div[1]/div/div[10]/div[2]/header/div[2]/form/div/button[2]/i').click()

saleprice=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[5]/div/section/div/div/div[1]/div[2]/div/div/dl[1]/dd').text
print(saleprice)
'''
driver.get("https://finance.naver.com/")
for i in range(1,10):
    item = driver.find_element(By.XPATH,f'/html/body/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/table/tbody/tr[{i}]/td[1]').text
    print(item)