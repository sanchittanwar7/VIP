vip_values = {'17-Jul-2018': {'nav': '99.39', 'target_amount': '5000', 'amount_invested': '5000.0', 'units_brought': '50.31'}, '17-Aug-2018': {'nav': '103.76', 'target_amount': '10000', 'amount_invested': '4780.16', 'units_brought': '46.07'}, '17-Sep-2018': {'nav': '102.96', 'target_amount': '15000', 'amount_invested': '5077.1','units_brought': '49.31'}, '17-Oct-2018': {'nav': '94.59', 'target_amount': '20000', 'amount_invested': '6219.41', 'units_brought': '65.75'}, '19-Nov-2018': {'nav': '97.48', 'target_amount': '25000', 'amount_invested': '4388.94', 'units_brought': '45.02'}, '17-Dec-2018': {'nav': '98.57', 'target_amount': '30000', 'amount_invested': '4720.46', 'units_brought': '47.89'}, '17-Jan-2019': {'nav': '98.76', 'target_amount': '35000', 'amount_invested': '4942.17', 'units_brought': '50.04'}, '18-Feb-2019': {'nav': '96.45', 'target_amount': '40000', 'amount_invested': '5818.65', 'units_brought': '60.33'}, '18-Mar-2019': {'nav': '103.96', 'target_amount': '45000', 'amount_invested': '1885.43', 'units_brought': '18.14'}, '18-Apr-2019': {'nav': '106.58', 'target_amount': '50000', 'amount_invested': '3865.91', 'units_brought': '36.27'}, '17-May-2019': {'nav': '103.43', 'target_amount': '55000', 'amount_invested': '6477.76', 'units_brought': '62.63'}, '17-Jun-2019': {'nav': '106.08', 'target_amount': '60000', 'amount_invested': '3590.83', 'units_brought': '33.85'}}
sip_values = {'17-Jul-2018': {'nav': '99.39', 'amount_invested': '5000', 'units_brought': '50.31'}, '17-Aug-2018': {'nav': '103.76', 'amount_invested': '5000', 'units_brought': '48.19'}, '17-Sep-2018': {'nav': '102.96', 'amount_invested': '5000', 'units_brought': '48.56'}, '17-Oct-2018': {'nav': '94.59', 'amount_invested': '5000', 'units_brought': '52.86'}, '19-Nov-2018': {'nav': '97.48', 'amount_invested': '5000', 'units_brought': '51.29'}, '17-Dec-2018': {'nav': '98.57', 'amount_invested': '5000', 'units_brought': '50.73'}, '17-Jan-2019': {'nav': '98.76', 'amount_invested': '5000', 'units_brought': '50.63'}, '18-Feb-2019': {'nav': '96.45', 'amount_invested': '5000', 'units_brought': '51.84'}, '18-Mar-2019': {'nav': '103.96', 'amount_invested': '5000', 'units_brought': '48.1'}, '18-Apr-2019': {'nav': '106.58', 'amount_invested': '5000', 'units_brought': '46.91'}, '17-May-2019': {'nav': '103.43', 'amount_invested': '5000', 'units_brought': '48.34'}, '17-Jun-2019': {'nav': '106.08', 'amount_invested': '5000', 'units_brought': '47.13'}}

# print(vip_values)

vip_no_of_months = 0
vip_amount_invested = 0
vip_total_units = 0
for month, detail in vip_values.items():
    vip_no_of_months = vip_no_of_months + 1
    vip_amount_invested += float(detail.get("amount_invested"))
    vip_amount_return = detail.get("target_amount")
    vip_total_units += float(detail.get("units_brought"))

sip_no_of_months = 0
sip_amount_invested = 0
sip_amount_return = 0
sip_total_units = 0
for month, detail in sip_values.items():
    sip_no_of_months = sip_no_of_months + 1
    sip_amount_invested += float(detail.get("amount_invested"))
    sip_total_units += float(detail.get("units_brought"))
    latest_nav = float(detail.get("nav"))
sip_amount_return = sip_total_units * latest_nav

print(vip_no_of_months)
print(vip_amount_invested)
print(vip_amount_return)
print(vip_total_units)

print(sip_no_of_months)
print(sip_amount_invested)
print(sip_amount_return)
print(sip_total_units)

