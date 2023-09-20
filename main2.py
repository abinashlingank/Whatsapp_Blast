from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os

opt = Options()
opt.add_experimental_option("excludeSwitches", ["enable-logging"])
opt.add_argument("--profile-directory=Default")
opt.add_argument("--user-data-dir=/var/tmp/chrome_user_data")
print(opt)
os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("*****  THANK YOU FOR USING WHATSAPP BULK MESSENGER  ******")
print("*****      This tool was built by ABINASH LINGAN K  ******")
print("*****           www.github.com/abinashlingank       ******")
print(style.RESET)
 
f = open("message1.txt", "r")
message = f.read()
f.close()

f1 = open("message2.txt", "r")
message2 = f1.read()
f1.close()



print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print(message2)
print("\n" + style.RESET)
message = quote(message)
message2 = quote(message2)

numbers = []
f = open(r"/home/abinashlingank/Desktop/Whatsapp_Blast-main/numbers.txt", "r")
for line in f:
	if line.strip() != "":
		numbers.append(line)

f.close()
total_number=len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30

driver = webdriver.Chrome(options=opt)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
sleep(2)

errorList =[]
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
driver.maximize_window()
for idx,number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)

	#try:
	url = 'https://web.whatsapp.com/send?phone=91' + number + '&text=' + message
	url2 = 'https://web.whatsapp.com/send?phone=91' + number + '&text=' + message2
	image_path="/home/abinashlingank/Desktop/Whatsapp_Blast-main/Talos Poster.jpeg"   #specify the image path here
	sent = False
	if not sent:
		try:
			driver.get(url)
			attac_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='attach-menu-plus']")))
			attac_btn = driver.find_element(By.XPATH, '//span[@data-icon="attach-menu-plus"]')
			attac_btn.click()
			img_btn = driver.find_element(By.XPATH, "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
			img_btn.send_keys(image_path)
			sleep(1)
			send_btn = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
			send_btn = driver.find_element(By.XPATH, "//span[@data-icon='send']")
			send_btn.click()
			sleep(3)              
			try:
				driver.get(url2)
				can_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div[5]/div/footer/div[2]/div/div[5]/div/div/div/div[2]/div/span")))
				can_btn.click()
				send_btn1 = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
				send_btn1.click()
			except:
				driver.get(url2)
				send_btn1 = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
				send_btn1.click()
			sent=True
			sleep(3)
			print(style.GREEN + 'Message sent to: ' + number + style.RESET)
		except:
			print("error")
			errorList.append(number+'\n')
			continue
			print(number)
f1 = open('error.txt','a+')
f1.writelines(errorList)
f1.close()
