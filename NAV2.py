from collections import OrderedDict


# navs = {'17-Jul-2018': 99.39, '17-Aug-2018': 103.76, '17-Sep-2018': 102.96, '17-Oct-2018': 94.59, '19-Nov-2018': 97.48, '17-Dec-2018': 98.57, '17-Jan-2019': 98.76, '18-Feb-2019': 96.45, '18-Mar-2019': 103.96, '18-Apr-2019': 106.58, '17-May-2019': 103.43, '17-Jun-2019': 106.08}
navs = OrderedDict([(u'17-Jul-2017', 88.67), (u'17-Aug-2017', 88.66), (u'18-Sep-2017', 90.93), (u'17-Oct-2017', 91.63), (u'17-Nov-2017', 92.15), (u'18-Dec-2017', 93.06), (u'17-Jan-2018', 96.59), (u'19-Feb-2018', 93.02), (u'19-Mar-2018', 90.56), (u'17-Apr-2018', 94.83), (u'17-May-2018', 96.02), (u'18-Jun-2018', 97.38),
                    (u'17-Jul-2018', 99.39), (u'17-Aug-2018', 103.76), (u'17-Sep-2018', 102.96), (u'17-Oct-2018', 94.59), (u'19-Nov-2018', 97.48), (u'17-Dec-2018', 98.57), (u'17-Jan-2019', 98.76), (u'18-Feb-2019', 96.45), (u'18-Mar-2019', 103.96), (u'18-Apr-2019', 106.58), (u'17-May-2019', 103.43), (u'17-Jun-2019', 106.08)])
initial = 5000
expected_return = 1.0  # monthly; yearly => 12%
print(navs)


def sip(navs, initial):
    print("--------------------------SIP------------------------")
    print("Month number\t\tNAV\t\tAmount Invested\tUnits Brought")
    n = len(navs)
    totalUnits = 0
    totalAmount = initial * n
    values = OrderedDict()
    for month, nav in navs.items():
        units = initial/nav
        totalUnits += units
        values[month] = {}
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


def vip(navs, initial):
    print("--------------------------VIP------------------------")
    totalAmount = 0
    totalUnits = 0
    n = len(navs)
    values = OrderedDict()
    print("Month Number\t\tNAV\tTarget Amount\tAmount Invested\tUnits Brought")
    for i, (month, nav) in enumerate(navs.items()):
        target = (i+1)*initial
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


def modified_vip(navs, initial, expected_return):
    print("-------------------------M-SIP------------------------")
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


print(sip(navs, initial))
print(vip(navs, initial))
print(modified_vip(navs, initial, expected_return))
