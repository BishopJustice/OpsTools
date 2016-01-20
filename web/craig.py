from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://sfbay.craigslist.org/sfc/')
search = browser.find_element_by_id("query")
search.send_keys("computer")
