from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time


class Scraper(object):
    def __init__(self):
        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/misc/05.4 - Python_Playground/drivers/chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--user-data-dir=./User_Data')
        self.driver = webdriver.Chrome(self.path, chrome_options=self.options)
        self.url = 'https://web.whatsapp.com'
        self.time = 1

    def access_page(self):
        self.driver.get(self.url)

    def create_new_group(self):
        try:
            # Creating Group
            burger_menu = self.driver.find_element_by_xpath(
                '//*[@id="side"]/header/div[2]/div/span/div[3]/div')
            burger_menu.click()

            time.sleep(1)

            new_group = self.driver.find_element_by_xpath(
                '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div')
            new_group.click()

            name_field = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input')
            name_field.send_keys('Leonardo Briotto')

            add_name = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div/div/div/div/div/div[2]')
            add_name.click()

            enter_button = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div')
            enter_button.click()

            set_group_des = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div')
            time.sleep(0.5)
            set_group_des.send_keys('PIROQUIO')

            time.sleep(0.1)

            button = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/div')
            button.click()

            time.sleep(3)

            input_box = self.driver.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            input_box.send_keys('PARA DE ME RETIRAR DE GRUPOS!!!!!!')
            input_box.send_keys(Keys.ENTER)

            # Exiting Group
            burger_menu_2 = self.driver.find_element_by_xpath(
                '//*[@id="main"]/header/div[3]/div/div[3]/div')
            burger_menu_2.click()

            exit_button = self.driver.find_element_by_xpath(
                '//*[@id="main"]/header/div[3]/div/div[3]/span/div/ul/li[5]/div')
            exit_button.click()

            exit_ = self.driver.find_element_by_xpath(
                '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')
            exit_.click()

            time.sleep(3)

            # Deleting Group
            burger_menu_3 = self.driver.find_element_by_xpath('//*[@id="main"]/header/div[3]/div/div[3]/div')
            burger_menu_3.click()

            # delete_group = self.driver.find_element_by_xpath(
            #     '//*[@id="main"]/header/div[3]/div/div[2]/span/div/ul/li[5]/div')
            # delete_group.click()
            #
            # time.sleep(0.3)
            #
            # delete_ = self.driver.find_element_by_xpath(
            #     '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')
            # delete_.click()

        except Exception as e:
            print(e.args)
            pass

    def main(self):
        self.access_page()

        input('Press any key')

        self.create_new_group()


if __name__ == '__main__':
    obj = Scraper()
    obj.main()
