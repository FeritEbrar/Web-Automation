from selenium import webdriver
import time 

class Corona:
    def __init__(self):
        self.driver = webdriver.Chrome()
        url = "https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html"
        self.driver.get(url) 
        self.driver.switch_to.window(self.driver.window_handles[1])
       
    
    def getInfos(self):
        self.driver.refresh()
        time.sleep(2)
        
        date = self.driver.find_element_by_xpath('//*[@id="TumVerileriGetir"]/tr[1]/td[1]').text
        todayCases = self.driver.find_element_by_xpath('//*[@id="TumVerileriGetir"]/tr[1]/td[8]').text
        todayDeaths = self.driver.find_element_by_xpath('//*[@id="TumVerileriGetir"]/tr[1]/td[11]').text
        totalCases = self.driver.find_element_by_xpath('//*[@id="TumVerileriGetir"]/tr[1]/td[3]').text
        totalDeaths = self.driver.find_element_by_xpath('//*[@id="TumVerileriGetir"]/tr[1]/td[4]').text
        
        print(f'{date} tarihinde Türkiye de günlük vaka sayısı : {todayCases}, günlük vefat sayısı : {todayDeaths}, toplam vaka sayısı : {totalCases} ve toplam vefat sayısı : {totalDeaths} dir.')
        time.sleep(3)
        
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        
corona = Corona()
corona.getInfos()
        
