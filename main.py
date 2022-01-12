import time

from config import email, password
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works
driver = webdriver.Chrome(options=chrome_options)

print("Opening web page...")

start_url = "https://mijnzonnepanelen.wocozon.nl/inloggen"
driver.get(start_url)

input_fields = driver.find_elements_by_css_selector("input")
print('Loggin in...')
x = 0
for input_field in input_fields:
	if x == 0:
		input_field.send_keys(email)
		x += 1
	else:
		input_field.send_keys(password)

response = driver.find_element_by_xpath("//button").click()
time.sleep(2)
containing_div = driver.find_element_by_css_selector("div.elevation-2")

result = containing_div.text.split("\n")[0]

print(f"Result = {result}")

driver.quit()