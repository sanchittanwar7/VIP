import time
import string
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


# Optional argument, if not specified will search path.
driver = webdriver.Chrome(
    '/home/sanchit/Desktop/Sanchit/VociqTraining/Scrapping/chromedriver')
driver.get(
    'https://www.motilaloswal.com/markets/mutual-funds-overview/sip-calculator.aspx')
# time.sleep(5) # Let the user actually see something!
# select = Select(driver.find_element_by_id('cmbSIFundHouse'))


el = driver.find_element_by_id('cmbSIFundHouse')
print(el)
for option in el.find_elements_by_tag_name('option'):
    print(option.text)
    if option.text.strip() == "HDFC Mutual Fund":
        print("match")
        option.click()  # select() in earlier versions of webdriver
        break

time.sleep(2)  # Let the user actually see something!

el = driver.find_element_by_id('cmbSICategory')
print(el)
for option in el.find_elements_by_tag_name('option'):
    print(option.text)
    if option.text.strip() == "Equity - Index":
        print("match")
        option.click()  # select() in earlier versions of webdriver
        break
time.sleep(2)  # Let the user actually see something!


el = driver.find_element_by_id('cmbSIScheme')
print(el)
for option in el.find_elements_by_tag_name('option'):
    print(option.text)
    if option.text.strip() == "HDFC Index Fund-Nifty 50 Plan":
        print("match")
        option.click()  # select() in earlier versions of webdriver
        break
# select.select_by_value('5946')


element = driver.find_element_by_id("txtInvestAmt")
element.send_keys("25000")


start_date = '11/06/2007'
end_date = '11/05/2019'

element = driver.find_element_by_id("inputjqxWidgetFromDate")
element.send_keys(start_date)


element = driver.find_element_by_id("inputjqxWidgetToDate")
element.send_keys(end_date)

element = driver.find_element_by_id("btnGo")
element.click()

time.sleep(2)

el = driver.find_element_by_name("tblSIPCalculator_length")
print(el)
for option in el.find_elements_by_tag_name('option'):
    print(option.text)
    if option.text.strip() == "100":
        print("match")
        option.click()  # select() in earlier versions of webdriver
        break
time.sleep(2)

next_button = driver.find_element_by_id("tblSIPCalculator_next")
table = driver.find_element_by_id("tblSIPCalculator")
print("next button : " + str(next_button))

while next_button.is_enabled():
    rows = table.find_element_by_tag_name(
        "tbody").find_elements_by_tag_name("tr")
    print(len(rows))

    for tr in rows:
        tds = tr.find_elements_by_tag_name('td')
        print(str(tds[0].text) + "," + str(tds[2].text) + ",")

    time.sleep(5)
#     next_button.send_keys(Keys.CONTROL + 't')
#     time.sleep(2)
    try:
        iframe = driver.find_element_by_id('__ta_notif_frame_1')
        print("iframe : " + str(iframe))
        driver.switch_to.frame(iframe)
        close_button = driver.find_element_by_class_name("close")
        print("close button : " + str(close_button))
        close_button.click()
        driver.switch_to.default_content()
    except:
        print("no ad")
    time.sleep(2)
    next_button = driver.find_element_by_id("tblSIPCalculator_next")
    print("next button : " + str(next_button))
    next_button.click()


time.sleep(5)  # Let the user actually see something!
driver.quit()
