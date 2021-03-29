# Xiaomi note ripper
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path

# Get webdriver
driver = webdriver.Firefox('.\\geckodriver')

# Login
driver.get('https://us.i.mi.com/')
input("Please connect to your xiaomi account then press \"Enter\"")
driver.get('https://us.i.mi.com/note/h5#/')
input("Verify your account if needed then press \"Enter\"")
driver.get('https://us.i.mi.com/note/h5#/')

# Create folder
Path("./output").mkdir(parents=True, exist_ok=True)

# Get notes
i = 1
while True:
    try:
        element = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div[{}]".format(i))
    except NoSuchElementException:
        break
    element.click()

    title = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[1]/div/div/input").get_property("value")
    content = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]").get_property("innerHTML")

    title_file = "{}-{}.txt".format(i, "".join([c for c in title.replace(" ", "_") if re.match(r'\w', c)]))
    
    f = open("./output/{}".format(title_file), "a")
    f.write(content)
    f.close()

    i += 1

# Quit
driver.quit()