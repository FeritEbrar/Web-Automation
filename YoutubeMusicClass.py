from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class YoutubeVideoPlayer:
    def __init__(self):
        
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.youtube.com/")
        self.driver.switch_to.window(self.driver.window_handles[1])

    def search(self):
        query = input("Enter the word you want to search : ")
        
        searcBox = self.driver.find_element_by_xpath('//*[@id="search"]')
        searcBox.send_keys(query)
        searcBox.send_keys(Keys.ENTER)
        time.sleep(2)
        
        order = int(input("Index : "))
        #elements = driver.find_elements_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]')
        time.sleep(2)
        element = self.driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{}]/div[1]/div/div[1]/div/h3/a'.format(order))
        ActionChains(self.driver).click(element).perform()
        
        time.sleep(400)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.close()
        
      
            
y = YoutubeVideoPlayer()
y.search()