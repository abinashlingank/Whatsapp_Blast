from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

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

f = open("message.txt", "r")
message = f.read()
f.close()

print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		numbers.append(line.strip())
f.close()
total_number=len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)
delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
sleep(2)
driver.minimize_window()
input(style.MAGENTA + "AFTER logging into Whatsapp Web is complete and your chats are visible, press ENTER..." + style.RESET)
driver.maximize_window()
for idx,number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)

	try:
		url = 'https://web.whatsapp.com/send?phone=91' + number + '&text=' + message
		image_path='image.jpg'   #specify the image path here
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				attac_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='clip']")))
				#attac_btn = driver.find_element_by_xpath("//span[@data-testid='clip']")
				attac_btn.click()
				img_btn = driver.find_element_by_xpath("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
				img_btn.send_keys(image_path)
				sleep(1)
				send_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='send']")))
				send_btn.click()
				send_btn2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='send']")))
				send_btn2.click()
				sent=True
				sleep(3)
				print(style.GREEN + 'Message sent to: ' + number + style.RESET)
	except Exception as e:
		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
driver.close()
