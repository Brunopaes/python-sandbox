import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# TODO: Refactor into functions
# TODO: Check if mini.json `endpoint` remains the same everyday
url = "https://www.nytimes.com/svc/crosswords/v6/puzzle/mini.json"
mini = "https://www.nytimes.com/crosswords/game/mini"
sess = requests.Session()

a = sess.get(url)

json_ = a.json().get("body")[-1].get("cells")

path = r"E:\PythonProjects\Personal\python-sandbox\drivers\chromedriver.exe"
# TODO: Selenium `executable_path` deprecation. Must change to `service object`
driver = webdriver.Chrome(path)

driver.get(mini)
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.ID, "pz-gdpr-btn-accept").click()
driver.find_element(By.CLASS_NAME, "xwd__modal--subtle-button").click()

for i, j in enumerate(json_):
    answer = j.get("answer")
    if answer is None:
        continue
    # TODO: Refactor. Not working due Mini Board construction
    cell = driver.find_element(By.XPATH, f'//*[@id="cell-id-{i}"]')
    cell.send_keys(answer)
