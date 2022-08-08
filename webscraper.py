from selenium import webdriver

url = 'https://youtube.com/kallehallden/videos' # Enter channel of the YouTuber you want to to get the latest content from 

# Replace with your browser's webdriver
browser = webdriver.Chrome(
    executable_path='D:\\DEV\\Projects\\Basic-Web-Scraper\\chromedriver.exe') # Replace with path to webdriver
browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()
