from selenium import webdriver
import time

class Weather:
    def __init__(self):
        city = input("Hava durumunu öğrenmek istediğiniz ili giriniz : ")
        cityC = city.capitalize()
        
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\ASUS\Desktop\Projects\Web Automation\chromedriver.exe')
        self.driver.get("https://mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il="+cityC)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        
        self.driver.refresh()
        time.sleep(1)
        
    def getInfo(self):
        daytime = self.driver.find_element_by_xpath('//*[@id="pages"]/div/section/h2[1]/span').text
        print("Son güncelleme : "+daytime)
        
        degree = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/section/div[5]/div[1]/div[1]').text
        print(degree+" Derece")
        
        air = self.driver.find_element_by_xpath('//*[@id="pages"]/div/section/div[5]/div[1]/div[2]/div[2]').text
        print("Hava "+air)
        if air == "Yağmurlu" or air == "Karlı" :
            print("Hava "+air+" Kalın giymeni veya şemsiye almanı önerimim")
        
        humidity = self.driver.find_element_by_xpath('//*[@id="pages"]/div/section/div[5]/div[2]/div[1]/div[2]/div[2]').text
        print("Nem oranı %"+humidity)
        
        wind = self.driver.find_element_by_xpath('//*[@id="pages"]/div/section/div[5]/div[2]/div[2]/div[2]/div[2]').text
        print("Rüzgar "+wind+" km/sa")
        
        time.sleep(4)
        self.driver.close()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()

w = Weather()
w.getInfo()