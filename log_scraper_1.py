from bs4 import BeautifulSoup
from selenium import webdriver
import os

#https://medium.com/ymedialabs-innovation/web-scraping-using-beautiful-soup-and-selenium-for-dynamic-page-2f8ad15efe25
#To read log file
filepath = "file:///home/vidyayug-d7/Downloads/log-copy.html"
#filepath = "file:///home/vidyayug-d7/Downloads/log6.html"

driver = webdriver.Firefox()
driver.get(filepath)
page_source = driver.page_source
#print(page_source.encode('utf-8'))
#print("--------------------------------------------------------------------------")
"""
#items = driver.find_elements_by_xpath("//div[contains(@class, 'element-header-toggle')")
items = driver.find_elements_by_xpath('//div[@class="children"]')
#items = driver.find_elements_by_xpath('//div[@class="element-header-toggle"]')

#print(items)
for element in items:
    #item.click()
    #print(element)
    element_text = element.text
    driver.execute_script("arguments[0].setAttribute('style', 'display:block;')", element);
    element_attribute_value = element.get_attribute('style')
    #element_attribute_value = element.get_attribute('value')
    #print(element_text)
    print(element_attribute_value)
    #print(element.tag_name)
    #print(element.parent)
    #print(element.location)
    #print(element.size)
"""
items1 = driver.find_elements_by_xpath('//div[@class="element-header closed"]')
for element in items1:
    element.click()
    #print(element)
    #element_text = element.text
    #driver.execute_script("arguments[0].setAttribute('style', 'display:block;')", element);
#print(items1)
page_source = driver.page_source
#print("--------------------------------------------------------------------------")
#print(page_source.encode('utf-8'))
soup = BeautifulSoup(page_source, "lxml")
'''
#pure selenium
test_cases = soup.find('div', attr={"class":"element-header"})

items = len(driver.find_elements_by_class_name("element-header"))
test_cases = driver.find_elements_by_class_name("element-header")
print(items)

for test in test_cases:
    print(test)
'''
# click radio button
test_suites = soup.find_all('div', attrs={"class":["suite"]})
#test_cases = soup.find_all('div', class_='test')
#print(test_suites)
print("There are {} Test cases.".format(len(test_suites)))
#Extract information
for suit in test_suites[1:]:
    print("--------------------------------------------------------------------------")
    test_case=" "
    d_id = ""
    d_dir = ""
    result = "<i></i>"
    status = "<i></i>"
    try:
        if suit.find('span', class_='name'):
            test_case = suit.find('span', class_='name')
        if len(suit.find_all('td', class_='doc')) > 0:
            raw_id = suit.find_all('td', class_='doc')[1]
            d_id = raw_id.find('p').text
            #print(d_id)
            str_split = d_id.split(":")
            d_did = str_split[0]
            d_dir = str_split[1]
        
        dcase = suit.find_all("th", string="Tags:")
        print("Tags :", dcase[0].find_next('td').text)
        tags = suit.find_all("th", string="Status:")      
        #print("Status :", tags[1].find_next('span', class_='label').text)
        if len(suit.find_all('tr')) > 0:
            result_row = suit.find_all('tr') 
            if dcase[0].find_next('td').contents[0]:
                result = dcase[0].find_next('td')           
            
            if tags[1].find_next('span', class_='label'):                
                status = tags[1].find_next('span', class_='label')
            
        
        print("Test case: {}".format(test_case.text))
        print("Design Input ID: {}".format(d_did))
        print("Design Input Requirement: {}".format(d_dir))
        print("Defect case: {}".format(result.text))
        print("Status: {}".format(status.text))
    except:
        pass

#print("{}".format(test_suites[2]))
#test_cases = soup.find_all('div', attrs={"class":"name"})
#print(test_cases)

#test_cases = soup.find_all('div', attr={"class":"element-header"})
#tests = soup.find_all('div', class_='element-header-left')
#print(tests)

#print(test_cases)
#table = soup.find('div') 

#print(soup.prettify())
#text = soup.find_all("table")
#test_cases = soup.find('div', attr={"class":"element-header"})
#print(table)
 
#driver.quit()
#driver.close()

