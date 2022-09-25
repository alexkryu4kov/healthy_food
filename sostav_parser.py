import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver

from links.nuts import links as nuts_links

GECKODRIVER_PATH = 'geckodriver'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
}
for key in headers:
    webdriver.DesiredCapabilities.FIREFOX['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]

for links in (
    'nuts_links',
):
    for link in globals()[links]:
        browser = webdriver.Firefox(executable_path=GECKODRIVER_PATH)
        browser.get(f'https://health-diet.ru/base_of_food/sostav/{link}.php')
        results_page = BeautifulSoup(browser.page_source, 'html.parser')
        d = {}
        name = results_page.find('div', {'class': 'mzr-block-content uk-margin-bottom'}).find('h4').getText().split('"')[1]
        d['name'] = name
        columns = results_page.find('table', {'class': 'mzr-table mzr-table-border mzr-tc-chemical-table'})
        for column in columns.findAll('tr'):
            cols = column.findAll('td')
            mineral = cols[0].getText().split(',')[0]
            val = cols[1].getText().split(' ')[0]
            if any(elem.isdigit() for elem in val):
                d[mineral] = float(val)
        directory = links.split('_links')[0]
        with open(f'data/{directory}/{link}.json', 'w', encoding='utf-8') as outfile:
            json.dump(d, outfile, ensure_ascii=False)
        print(f'{name} сохранены в json')
        time.sleep(0.1)
        browser.close()
