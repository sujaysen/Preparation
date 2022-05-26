from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
options = webdriver.ChromeOptions()
options = options.to_capabilities()
driver.get("https://chegg-experts.us.auth0.com/login?state=hKFo2SA3RDF0bDNMZ19ycXNJbm5jYnFGdHlGdGc2d19MSEtfYqFupWxvZ2luo3RpZNkgUE9wWUNXVEp2U0EyVXZHNnRoZldMNHpQS3NXczBSR1ajY2lk2SA0ZXBLRnVXZm9MQ0RLMlhWWk9iTGxWaWRGOUFKTVI4QQ&client=4epKFuWfoLCDK2XVZObLlVidF9AJMR8A&protocol=oauth2&audience=https%3A%2F%2Fchegg-experts.us.auth0.com%2Fapi%2Fv2%2F&scope=openid%20profile%20email%20offline_access&redirect_uri=https%3A%2F%2Fexpert.chegg.com%2F&response_type=code&response_mode=query&nonce=MnlpRXd0QkhTUTFtLS1tUGVtZUsxaHRPcU9nS3N2UC1SdGZnTDlvTmhrfg%3D%3D&code_challenge=KDhxJiQoPArZEPn3Lh2OpRZI-EyCtpjIYNzeY2_2sl0&code_challenge_method=S256&auth0Client=eyJuYW1lIjoiYXV0aDAtcmVhY3QiLCJ2ZXJzaW9uIjoiMS4zLjAifQ%3D%3D")
driver.implicitly_wait(10)
Email = driver.find_element_by_id('1-email')
password = driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div/div/div/div[3]/div[2]/span/div/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div/input')
Email.send_keys("mita.eng88@gmail.com")
password.send_keys("Sujay@123")
#submit = driver.find_element_by_xpath('/html/body/div/div/div[2]/form/div/div/div/button')
driver.find_element_by_name("submit").click()
