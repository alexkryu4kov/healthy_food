from bs4 import BeautifulSoup
from selenium import webdriver

GECKODRIVER_PATH = 'geckodriver'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
for key in headers:
    webdriver.DesiredCapabilities.FIREFOX['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]

browser = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
browser.get('https://health-diet.ru/base_of_meals/meals_21243')
results_page = BeautifulSoup(browser.page_source, 'html.parser').encode('latin-1')
print(results_page)
browser.close()
