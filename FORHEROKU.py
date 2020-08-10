from selenium import webdriver
import os
from time import sleep
import smtplib
from selenium.webdriver.common.keys import Keys
op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")
driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options = op)
driver.get("https://instagram.com")
print('we have a sucessfully reached instagram sir')
sleep(10)

#useename

username = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
username.send_keys('ENTER YOUR USERNAME')

#passwd

passwd = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')
passwd.send_keys('ENTER YOUR PASSWD')

#login

login = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button')
login.click()

sleep(8)
print("we have sucessfully logged in to ur account sir")

sleep(5)
direct = driver.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a')
direct.click()
sleep(3)
print("boss we have reached the message corner and searching for messages")
def perma():
	while True:
		if driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div'):
			write_message = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a')
			write_message.click()
			sleep(5)
			writing_message = driver.find_element_by_css_selector('.ItkAi > textarea:nth-child(1)')
			writing_message.send_keys('ENTEER THE MESSAGE')
			send_it = driver.find_element_by_css_selector('div.JI_ht:nth-child(3) > button:nth-child(1)')
			send_it.click()
			driver.execute_script("window.history.go(-1)")
			sleep(5)
		elif driver.find_elements_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a/div/div[3]/div'):
			write_message1 = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[2]/a')
			write_message1.click()
			sleep(5)
			writing_message1 = driver.find_element_by_css_selector('.ItkAi > textarea:nth-child(1)')
			writing_message1.send_keys('Hi This is my bot version 1.0 and bashar is currently busy and he will check message soon and dont spam unncesarily!')
			send_it1 = driver.find_element_by_css_selector('div.JI_ht:nth-child(3) > button:nth-child(1)')
			send_it1.click()
			driver.execute_script("window.history.go(-1)")
			sleep(5)
		else:
			sleep(5)
perma()
while True:
	if perma() == False:
		server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
		server.login("ENTER YOUR GMAIL IN CASE IF THE SCRIPT CRASHES", "ENTER THE PASWD OF THE GMAIL")
		server.sendmail("ENTER THE EMAIL IN WHICH YOUR LOGGED IN", "ENTER THE EMAIL U NEED TO SEDN", "boss, our auto message of insta had crashed due to some reasons please help!!")



			











