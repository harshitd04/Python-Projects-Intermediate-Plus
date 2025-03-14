from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_times_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names_list = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}
for n in range(len(event_times_list)):
    events[n] = {
        "time" : event_times_list[n].text,
        "name" : event_names_list[n].text
}
print(events)
for i in range(len(events)):
    print(f"{events[i]["time"]}:{events[i]["name"]}")
driver.quit()