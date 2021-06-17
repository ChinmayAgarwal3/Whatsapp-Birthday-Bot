from selenium import webdriver 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class Initialze_Script:
    '''
        Docstring: Initializes the webdriver for Firefox, along with the default profile for it to automatically load whatsapp web. 
    '''
    def __init__(self):
        '''
            Contains both the commads for Chrome/Firefox, Comment/Uncomment the ones that you want to use. 
            Advice: Use the browser that you don't use often, for selenium requres a new clean instance to run on the default profile
        '''
        #Chrome:
        self.chropt = webdriver.ChromeOptions() 
        self.chropt.add_argument(
            "user-data-dir=/home/rich/.config/google-chrome")
        self.driver = webdriver.Chrome(options = self.chropt)
        

        '''Firefox: WebDriver driver = new FirefoxDriver();
        '''
        #self.profile = webdriver.FirefoxProfile("~/.mozilla/firefox/8erdmg4x.default/")
        #self.driver = webdriver.Firefox(self.profile)

        self.driver.get("https://web.whatsapp.com/")
        time.sleep(7)
        

    def Search_and_enter_chat(self, person):
        # eleFind = self.driver.find_element_by_class_name("_1JAUF _1d1OL")
        # eleFind.click()
        # eleFind.send_keys(person)
        action=ActionChains(self.driver)
        # action.key_down(Keys.CONTROL).key_down(Keys.ALT).send_keys(
        #     '/').key_up(Keys.CONTROL).key_up(Keys.ALT).perform()
        # time.sleep(5)

        element = self.driver.find_element_by_xpath(
            "/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/div")  # _2MwRD
        action.click(on_element=element)
        action.send_keys("Awesome")


        # # action.send_keys("Awesome")
        # eleFind = self.driver.find_element_by_class_name(
        #     "_1JAUF._1d1OL.focused")
        # eleFind.click()
        # eleFind.send_keys("Awesome")
        # eleNM = self.driver.find_element_by_xpath("//span[@title='"+person+"']") 
        # eleNM.click() 
           

    def send_message(self, name,  message):
        namev = [name]
        for inp in namev: 
            self.Search_and_enter_chat(inp)  
            # Finds the chat box element 
            inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
            eleTF =  self.driver.find_element_by_xpath(inp_xpath)
            time.sleep(15)
            # Writes the message for the birthday 
            eleTF.send_keys(message + Keys.ENTER) 
            time.sleep(5)
        self.driver.quit()

bot=Initialze_Script()
bot.Search_and_enter_chat(person="Awesome")
