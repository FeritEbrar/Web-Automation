from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class Whatsapp:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://web.whatsapp.com/")
        self.driver.switch_to.window(self.driver.window_handles[1])
    
    def msg(self):
        name = input("\nEnter the group or username to massege : ")
        name = name.lower().title()
        message = input("Type the massege you want to send : ")
        count = int(input("Message count : "))
        
        search_box = self.driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
        search_box.send_keys(name)
        time.sleep(1)
        
        user = self.driver.find_element_by_xpath(
                '//span[@title = "{}"]'.format(name))
        
        user.click()
        
        text_box = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]')
        for i in range(count):
            
            text_box.send_keys(message)
            time.sleep(1)
            text_box.send_keys(Keys.ENTER)
        
    
    def again(self):
        print("Do you want to send message again or different person/group ? ")
        respond = input("Click y for YES, n for NO : ")
        
        if respond == "y":
            self.msg()
            self.again()
        elif respond == "n":
            print("Thank you for using ! Come Again !")
        else:
            print("Wrong input ! Please try again.")
            self.again()
            
w = Whatsapp()
w.msg()
w.again()
