from selenium import webdriver
import random
import time
import os


class CommissionForm:
    def __init__(self):
        self.url = 'https://docs.google.com/forms/d/e/1FAIpQLSdJAgJHD8fIN3G_HUlpe3Zmuibvr1NHogoXdbVxaI2YIFiZjQ/viewform'
        self.path = r'/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/misc/05.4 - Python_Playground/drivers/chromedriver'
        self.driver = webdriver.Chrome(self.path)

        self.f_list = open('/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/misc/05.4 - Python_Playground/src/crawlers/data/first_names.txt', 'r', encoding='utf-8').read().split(',')
        self.l_list = open('/Users/brunopaes/Documents/OneDrive/Acadêmico/ESPM/misc/05.4 - Python_Playground/src/crawlers/data/last_names.txt', 'r', encoding='utf-8').read().split(',')

        self.scholarship_type = [
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[1]/label/div/div[1]/div[3]/div',
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[2]/label/div/div[1]/div[3]/div',
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[3]/label/div/div[1]/div[3]/div',
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[4]/label/div/div[1]/div[3]/div',
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[5]/label/div/div[1]/div[3]/div'
        ]

        self.mail_sulfix = [
            '{}{}@gmail.com',
            '{}{}@hotmail.com',
            '{}{}@yahoo.com',
            '{}{}@bol.com'
        ]

        self.meeting = [
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[1]/label/div/div[1]/div[3]/div',
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[2]/label/div/div[1]/div[3]/div',
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/content/div/div[3]/label/div/div[1]/div[3]/div'
        ]

        self.hour = [
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[1]/label/div/div[1]/div[3]/div',
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[2]/label/div/div[1]/div[3]/div',
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[3]/label/div/div[1]/div[3]/div',
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[4]/label/div/div[1]/div[3]/div',
            '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[5]/label/div/div[1]/div[3]/div',
        ]

    def access_page(self):
        self.driver.get(self.url)

    def generate_random_names(self):
        f_name = random.choice(self.f_list)
        l_name = random.choice(self.l_list)

        return f_name.strip(' '), l_name.strip(' ')

    def fill_form(self):
        f_name = self.generate_random_names()[0]
        l_name = self.generate_random_names()[1]

        sulfix = random.choice(self.mail_sulfix)

        name = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input')
        name.send_keys('{} {}'.format(f_name, l_name))

        school_id = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input')
        school_id.send_keys('11{}{}{}'.format(random.randint(3, 9), random.randint(1, 2), random.randint(1000, 9999)))

        self.driver.find_element_by_xpath(random.choice(self.scholarship_type)).click()

        mail = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input')
        mail.send_keys(sulfix.format('{}{}'.format(f_name, l_name), random.randint(1, 999)))

        guests = self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[5]/div/div[2]/div/div[1]/div/div[1]/input')
        guests.send_keys(random.randint(1, 9))

        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/content').click()

        self.driver.find_element_by_xpath(random.choice(self.meeting)).click()

        # self.driver.find_element_by_xpath(random.choice(self.hour)).click()
        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/content/div/div[5]/label/div/div[1]/div[3]/div').click()

        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/content/div/div[2]/label/div/div[1]/div[3]/div').click()

        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div[2]/content').click()

        # time_ = random.randint(15, 300)
        #
        # print(time_)
        #
        # time.sleep(time_)

        self.driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div[2]/content/span').click()

    def __call__(self, *args, **kwargs):
        while True:
            self.access_page()
            self.fill_form()


if __name__ == '__main__':
    CommissionForm()()
