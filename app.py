from flask import Flask
from flask import render_template
from flask import request
import time
import string
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from collections import OrderedDict


app = Flask(__name__)
navs = OrderedDict()
amount = 0.0
expected_return = 0.0


@app.route('/')
def hello():
    return render_template('main.html')


@app.route('/tables', methods=['POST'])
def tab():
    sip_values = sip(navs, float(amount))
    tip_values = tip(navs, float(amount), 0.0)
    vip_values = vip(navs, float(amount), expected_return/12)

    tip_no_of_months = 0.0
    tip_amount_invested = 0.0
    tip_total_units = 0.0
    tip_maxSelf = 0.0
    for month, detail in tip_values.items():
        tip_no_of_months = tip_no_of_months + 1
        tip_amount_invested += float(detail.get("amount_invested"))
        tip_amount_return = float(detail.get("target_amount"))
        tip_total_units += float(detail.get("units_brought"))
        tip_maxSelf = float(detail.get("tip_maxSelf"))
    tip_return = ((tip_amount_return/tip_amount_invested)
                  ** (24/tip_no_of_months) - 1)*100

    vip_no_of_months = 0.0
    vip_amount_invested = 0.0
    vip_total_units = 0.0
    for month, detail in vip_values.items():
        vip_no_of_months = vip_no_of_months + 1
        vip_amount_invested += float(detail.get("amount_invested"))
        vip_amount_return = float(detail.get("target_amount"))
        vip_total_units += float(detail.get("units_brought"))
    vip_return = ((vip_amount_return/vip_amount_invested)
                  ** (24/vip_no_of_months) - 1)*100

    sip_no_of_months = 0.0
    sip_amount_invested = 0.0
    sip_amount_return = 0.0
    sip_total_units = 0.0
    for month, detail in sip_values.items():
        sip_no_of_months = sip_no_of_months + 1
        sip_amount_invested += float(detail.get("amount_invested"))
        sip_total_units += float(detail.get("units_brought"))
        latest_nav = float(detail.get("nav"))
    sip_amount_return = sip_total_units * latest_nav
    sip_return = ((sip_amount_return/sip_amount_invested)
                  ** (24/sip_no_of_months) - 1)*100

    conclusion = {}
    conclusion["vip_no_of_months"] = vip_no_of_months
    conclusion["vip_amount_invested"] = vip_amount_invested
    conclusion["vip_amount_return"] = vip_amount_return
    conclusion["vip_total_units"] = vip_total_units
    conclusion["vip_return"] = vip_return
    conclusion["tip_no_of_months"] = tip_no_of_months
    conclusion["tip_amount_invested"] = tip_amount_invested
    conclusion["tip_amount_return"] = tip_amount_return
    conclusion["tip_total_units"] = tip_total_units
    conclusion["tip_return"] = tip_return
    conclusion["tip_maxSelf"] = tip_maxSelf
    conclusion["sip_no_of_months"] = sip_no_of_months
    conclusion["sip_amount_invested"] = sip_amount_invested
    conclusion["sip_amount_return"] = sip_amount_return
    conclusion["sip_total_units"] = sip_total_units
    conclusion["sip_return"] = sip_return

    return render_template('table.html', vip_details=vip_values, tip_details=tip_values, sip_details=sip_values, result=conclusion)


@app.route('/results', methods=['POST'])
def index():
    count = ret()
    global navs
    global amount
    global expected_return
    fund_house = request.form['fund']
    category = request.form['category']
    scheme = request.form['scheme']
    amount = request.form['amount']
    expected_return = float(request.form['return'])
    stock = float(request.form['stock'])
    start = request.form['start']
    end = request.form['end']
    print(fund_house, category, scheme, amount, expected_return, start, end)
    navs = getNAVs(fund_house, category, scheme, amount, start, end)
    print(navs)
    return render_template('get_button.html', amount=amount, expected_return=expected_return)
    # sip_values = sip(navs, float(amount))
    # tip_values = tip(navs, float(amount), 0.0)
    # vip_values = vip(navs, float(amount), expected_return/12)

    # tip_no_of_months = 0.0
    # tip_amount_invested = 0.0
    # tip_total_units = 0.0
    # tip_maxSelf = 0.0
    # for month, detail in tip_values.items():
    #     tip_no_of_months = tip_no_of_months + 1
    #     tip_amount_invested += float(detail.get("amount_invested"))
    #     tip_amount_return = float(detail.get("target_amount"))
    #     tip_total_units += float(detail.get("units_brought"))
    #     tip_maxSelf = float(detail.get("tip_maxSelf"))
    # tip_return = ((tip_amount_return/tip_amount_invested)
    #               ** (24/tip_no_of_months) - 1)*100

    # vip_no_of_months = 0.0
    # vip_amount_invested = 0.0
    # vip_total_units = 0.0
    # for month, detail in vip_values.items():
    #     vip_no_of_months = vip_no_of_months + 1
    #     vip_amount_invested += float(detail.get("amount_invested"))
    #     vip_amount_return = float(detail.get("target_amount"))
    #     vip_total_units += float(detail.get("units_brought"))
    # vip_return = ((vip_amount_return/vip_amount_invested)
    #               ** (24/vip_no_of_months) - 1)*100

    # sip_no_of_months = 0.0
    # sip_amount_invested = 0.0
    # sip_amount_return = 0.0
    # sip_total_units = 0.0
    # for month, detail in sip_values.items():
    #     sip_no_of_months = sip_no_of_months + 1
    #     sip_amount_invested += float(detail.get("amount_invested"))
    #     sip_total_units += float(detail.get("units_brought"))
    #     latest_nav = float(detail.get("nav"))
    # sip_amount_return = sip_total_units * latest_nav
    # sip_return = ((sip_amount_return/sip_amount_invested)
    #               ** (24/sip_no_of_months) - 1)*100

    # conclusion = {}
    # conclusion["vip_no_of_months"] = vip_no_of_months
    # conclusion["vip_amount_invested"] = vip_amount_invested
    # conclusion["vip_amount_return"] = vip_amount_return
    # conclusion["vip_total_units"] = vip_total_units
    # conclusion["vip_return"] = vip_return
    # conclusion["tip_no_of_months"] = tip_no_of_months
    # conclusion["tip_amount_invested"] = tip_amount_invested
    # conclusion["tip_amount_return"] = tip_amount_return
    # conclusion["tip_total_units"] = tip_total_units
    # conclusion["tip_return"] = tip_return
    # conclusion["tip_maxSelf"] = tip_maxSelf
    # conclusion["sip_no_of_months"] = sip_no_of_months
    # conclusion["sip_amount_invested"] = sip_amount_invested
    # conclusion["sip_amount_return"] = sip_amount_return
    # conclusion["sip_total_units"] = sip_total_units
    # conclusion["sip_return"] = sip_return

    # return render_template('table.html', vip_details=vip_values, tip_details=tip_values, sip_details=sip_values, result=conclusion)


def ret():
    return 300


def sip(navs, initial):
    print("Month number\tNAV\t\tAmount Invested\tUnits Brought")
    n = len(navs)
    totalUnits = 0
    totalAmount = initial * n
    values = OrderedDict()
    for month, nav in navs.items():
        units = initial/nav
        totalUnits += units
        values[month] = OrderedDict()
        values[month]["nav"] = str(nav)
        values[month]["amount_invested"] = str(round(initial, 2))
        values[month]["units_brought"] = str(round(units, 2))
        values[month]["cumulative_units"] = str(round(totalUnits, 2))

        print(month + "\t\t" + str(nav) + "\t\t" +
              str(round(initial, 2)) + "\t\t" + str(round(units, 2)))
    print()
    print("Total Units Brought :" + str(round(totalUnits, 2)))
    print("Total Amount Invested :" + str(round(totalAmount, 2)))
    print("Average Cost Per Unit :" + str(round(totalAmount/totalUnits, 2)))
    # print("Market Value of Portfolio :" + str(round(totalUnits*navs[n-1], 2)))
    return values


def tip(navs, initial, stock):
    totalAmount = 0
    totalUnits = 0
    n = len(navs)
    maxSelf = 0.0

    values = OrderedDict()

    print("Month Number\tNAV\tTarget Amount\tAmount Invested\tUnits Brought")
    for i, (month, nav) in enumerate(navs.items()):
        target = (i+1)*initial
        currentValuation = totalUnits*nav
        amount = target - currentValuation
        amount_from_stock = min(amount, stock)
        stock = stock - amount_from_stock
        amount_from_stock = max(0.0, amount_from_stock)
        surplus_amount = max(0.0, amount - amount_from_stock)
        maxSelf = max(maxSelf, surplus_amount)
        units = amount/nav
        totalUnits += units
        totalAmount += amount
        values[month] = OrderedDict()
        values[month]["nav"] = str(nav)
        values[month]["target_amount"] = str(round(target, 2))
        values[month]["amount_invested"] = str(round(amount, 2))
        values[month]["units_brought"] = str(round(units, 2))
        values[month]["cumulative_units"] = str(round(totalUnits, 2))
        values[month]["amount_from_stock"] = str(round(amount_from_stock, 2))
        values[month]["surplus_amount"] = str(round(surplus_amount, 2))
        values[month]["stock"] = str(round(stock, 2))
        values[month]["tip_maxSelf"] = str(round(maxSelf, 2))

        print(month + "\t\t" + str(nav) + "\t\t" + str(round(target, 2)) +
              "\t\t" + str(round(amount, 2)) + "\t\t" + str(round(units, 2)))
    # values[maxSelf] = maxSelf
    print()
    print("Total Units Brought :" + str(round(totalUnits, 2)))
    print("Total Amount Invested :" + str(round(totalAmount, 2)))
    print("Average Cost Per Unit :" + str(round(totalAmount/totalUnits, 2)))
    # print("Market Value of Portfolio :" + str(round(totalUnits*navs[n-1], 2)))
    return values


def vip(navs, initial, expected_return):
    print("-------------------------VIP------------------------")
    totalAmount = 0
    totalUnits = 0
    n = len(navs)
    values = OrderedDict()
    target = 0
    print("Month Number\t\tNAV\tTarget Amount\tAmount Invested\tUnits Brought")
    for i, (month, nav) in enumerate(navs.items()):
        target = target + initial + float(expected_return/100)*target
        currentValuation = totalUnits*nav
        amount = target - currentValuation
        units = amount/nav
        totalUnits += units
        totalAmount += amount
        values[month] = {}
        values[month]["nav"] = str(nav)
        values[month]["target_amount"] = str(round(target, 2))
        values[month]["amount_invested"] = str(round(amount, 2))
        values[month]["units_brought"] = str(round(units, 2))
        values[month]["cumulative_units"] = str(round(totalUnits, 2))
        print(month + "\t\t" + str(nav) + "\t\t" + str(round(target, 2)) +
              "\t\t" + str(round(amount, 2)) + "\t\t" + str(round(units, 2)))

    print()
    print("Total Units Brought :" + str(round(totalUnits, 2)))
    print("Total Amount Invested :" + str(round(totalAmount, 2)))
    print("Average Cost Per Unit :" + str(round(totalAmount/totalUnits, 2)))
    # print("Market Value of Portfolio :" + str(round(totalUnits*navs[n-1], 2)))
    return values


def getNAVs(fund_house, category, scheme, amount, start, end):
    driver = webdriver.Chrome(
        '/home/sanchit/Desktop/Sanchit/VociqTraining/Scrapping/chromedriver')
    driver.get(
        'https://www.motilaloswal.com/markets/mutual-funds-overview/sip-calculator.aspx')

    el = driver.find_element_by_id('cmbSIFundHouse')
    print(el)
    for option in el.find_elements_by_tag_name('option'):
        print(option.text)
        if option.text.strip() == fund_house:
            print("match")
            option.click()
            break

    time.sleep(2)

    el = driver.find_element_by_id('cmbSICategory')
    print(el)
    for option in el.find_elements_by_tag_name('option'):
        print(option.text)
        if option.text.strip() == category:
            print("match")
            option.click()  # select() in earlier versions of webdriver
            break

    time.sleep(2)  # Let the user actually see something!

    el = driver.find_element_by_id('cmbSIScheme')
    print(el)
    for option in el.find_elements_by_tag_name('option'):
        print(option.text)
        if option.text.strip() == scheme:
            print("match")
            option.click()  # select() in earlier versions of webdriver
            break

    element = driver.find_element_by_id("txtInvestAmt")
    element.send_keys(amount)

    start_date = start
    end_date = end

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

    table = driver.find_element_by_id("tblSIPCalculator")
    rows = table.find_element_by_tag_name(
        "tbody").find_elements_by_tag_name("tr")
    print(len(rows))

    navs = OrderedDict()
    for tr in rows:
        tds = tr.find_elements_by_tag_name('td')
        print(tds[0].text + " " + tds[2].text)
        navs[tds[0].text] = float(tds[2].text)
        # navs.append(float(tds[2].text))

    time.sleep(2)  # Let the user actually see something!
    driver.quit()
    return navs


if __name__ == '__main__':
    app.run(debug=True)
