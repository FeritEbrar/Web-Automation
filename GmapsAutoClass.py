from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

class Map:
    def __init__(self):
        self.driver = webdriver.Chrome()
        url = "https://www.google.com/maps/dir///@41.0293507,28.8523696,12z"
        self.driver.get(url) 
        self.driver.switch_to.window(self.driver.window_handles[1])
       
    
    def deperture(self):
        deperturePoint = self.driver.find_element_by_xpath("//*[@id='sb_ifc50']/input")
        depertureInput = input("Enter your current location : ")
        deperturePoint.send_keys(depertureInput)
        time.sleep(1)
          
    
    def arrival(self):
        arrivalPoint = self.driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input')
        arrivalInput = input("Enter the location you want to arrive at : ")
        arrivalPoint.send_keys(arrivalInput)
        time.sleep(1)
        arrivalPoint.send_keys(Keys.ENTER)
        
    
    def methods(self):
        time.sleep(5)
        minute = self.driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[1]/span[1]')
        minuteRemains = minute.text
        km = self.driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div/div[1]/div[1]/div[2]')
        kmRemains = km.text
        print(f"Arrival Minutes by car : {minuteRemains}, Arrival distance : {kmRemains}, Just look at the page that opens for public transport routes.")
        
m = Map()
m.deperture()
m.arrival()
m.methods()