from linkedin_scraper import Person, actions
from selenium import webdriver


driver = webdriver.Chrome(r"E:\PythonProjects\Personal\friday\data\webdriver\chromedriver.exe")

credentials = {
            'email': 'brunopaes05@gmail.com',
            'password': '13112766'
        }

actions.login(driver, credentials.get('email'), credentials.get('password'))

person = Person('https://www.linkedin.com/in/shayfinkelstein/', driver=driver)

print(person)