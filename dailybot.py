from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from datetime import datetime
import time



class DailyBot():
    def __init__(self, full_name):
        #set browser to spanish
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'es,es_SP'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        #other attributes
        self.full_name = full_name
        self.date = datetime.today().strftime('%d/%m/%Y')
    
    def open_web(self):
        self.browser.get('https://docs.google.com/forms/d/e/1FAIpQLSczCqzQMPvnizYC00Iatn4cBzm_lwkGyYO4a7DV-i0CASc7TQ/viewform')

    def fill_date(self):
        #fill date
        date_element = self.browser.find_elements_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div/div[1]/input')        
        date_element[0].send_keys(self.date)
        
    def fill_name(self):
        #change order, (last name first)
        n = self.full_name.split()
        n.reverse()
        name = " ".join(n)
        
        #click drop down
        dropbutton1 = self.browser.find_elements_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div[1]/div[2]'
            )
        dropbutton1[0].click()
        time.sleep(1)
        
        #select name        
        name_selected = self.browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[@data-value="{}"]'.format(name)
            )
        name_selected.click()
        time.sleep(1)

    def fill_course(self, c):
        #fill course
        #click drop down        
        dropbutton2 = self.browser.find_elements_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]'
            )
        dropbutton2[0].click()
        time.sleep(1)
        #select course
        course = self.browser.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div[2]/div[@data-value="{}"]'.format(c)
                       
            )
        course.click()
        time.sleep(1)

    def fill_sentiment(self, sent):
        sentiment = self.browser.find_element_by_css_selector(
            '.quantumWizTogglePapercheckboxEl[aria-label="{}"]'.format(sent)
            )             
        sentiment.click()

        
    def fill_questions(self, q1=None, q2=None, q3=None, q4=None):
        #select all Questions
        questions = self.browser.find_elements_by_css_selector("textarea")
        
        #fill Q1
        if q1:
            questions[0].send_keys(q1)
        else:
            questions[0].send_keys("Aquí va la respuesta # 1")

        #fill Q2
        if q2:
            questions[1].send_keys(q2)
        else:
            questions[1].send_keys("Aquí va la respuesta # 2")

        #fill Q3
        if q1:
            questions[2].send_keys(q3)
        else:
            questions[2].send_keys("Aquí va la respuesta # 3")

        #fill Q4
        if q1:
            questions[3].send_keys(q4)
        else:
            questions[3].send_keys("Aquí va la respuesta # 4")
        
    def fill_score(self, score):
        #fill score
        #select all Circles     
        scores = self.browser.find_elements_by_css_selector(".appsMaterialWizToggleRadiogroupOffRadio")    
        s = score
        scores[s-1].click()

    def fill_all(self):
        self.open_web()
        self.fill_date()
        self.fill_name()
        self.fill_course(c="Data Science")
        self.fill_sentiment(sent="Contento")
        self.fill_questions()
        self.fill_score(6)
