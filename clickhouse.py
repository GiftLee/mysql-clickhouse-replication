


import clickhouse_driver
from  decimal import Decimal
import datetime
sql ={'insert_sql': 'INSERT INTO mrtdb.sal_salesorder VALUES'}
insert_data = [{'ORG_CODE': '91231201', 'TENANT_ID': '231282161234', 'SHOP_ID': '231282161234', 'SALES_ID': 'CE36B480FAFA4BA0919DDE3567377722', 'GLIDE_NO': '12342103040100024', 'ORIGINAL_SALES_ID': 'CE36B480FAFA4BA0919DDE3567377722', 'SALES_DATE': '20210304', 'SALES_TYPE': '10', 'CLIENT_ID': None, 'CLIENT_TEL': None, 'IC_CARDNO': None, 'BANK_CARD': None, 'OPENID': None, 'UNION_ID': None, 'CHK_DATE': '20210304140337', 'CHK_USER': '231282161234', 'SALES_STYLE': '00', 'FROM_ID': None, 'FIG_ID': None, 'REFSALESID': None, 'SALE_AMT': Decimal('1.000000'), 'SALE_MNY': Decimal('10.000000'), 'SALE_MNY_NOTAX': Decimal('8.850000'), 'PAY_DIBS': Decimal('0.000000'), 'CASH_MNY': Decimal('10.000000'), 'PAY_ZERO': Decimal('0.000000'), 'GROSS_PROFIT': Decimal('1.200000'), 'TRADE_INFO': '现金 ￥10.00', 'IS_CALC_INTEGRAL': None, 'INTEGRAL': 0, 'BARTER_INTEGRAL': 0, 'REMARK': None, 'INVOICE_FLAG': None, 'TAX_RATE': None, 'CREA_DATE': '20210304140337', 'CREA_USER': '231282161234', 'GUIDE_USER': '231282161234', 'PLAN_DATE': '20210304', 'LINKMAN': None, 'TELEPHONE': None, 'SEND_ADDR': None, 'COMM': '00', 'TIME_STAMP': 1614838011}]
client = clickhouse_driver.Client(host='10.0.116.191', port='9000', database='mrtdb', user='default', password='qazwsx')
client.execute(sql['insert_sql'], insert_data, types_check=True)
print(datetime.datetime(1970, 1, 2, 14, 1))

