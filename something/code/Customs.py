import requests
import json

# post_data ={"orderCnt":{"consignee":"张三",
#                     "consigneeAddress": "浙江省杭州市江干区1号大街052",
#                     "consigneeCity": "成都",
#                     "consigneeCounty": "锦江区",
#                     "consigneeProvince": "四川",
#                     "consigneeTel": "13811112222",
#                     "ecCode": "311376849",
#                     "tradeTime":"1992-2-10 10:10:10",
#                     "wayBillNo":"",
#                     "paperNumber":"",
#                     "paperName":"",
#                     "assureCode":"",
#                     "licenseNo":"",
#                     "companyCode":"123456",
#                     "companyName":"电商平台备案名称",
#                     "feeAmount":"",
#                     "insureAmount":"",
#                     "items": [
#                         {
#                             "codeTs": "01000000",
#                             "goodsCount": "3",
#                             "goodsItemNo": "101",
#                             "goodsModel": "尺码:L",
#                             "goodsName": "笔",
#                             "goodsUnit": "支",
#                             "grossWeight": "5.55",
#                             "netWeight": "6.55",
#                             "originCountry": "美国",
#                             "param1": "",
#                             "param2": "",
#                             "skuCode": "c002",
#                             "unitPrice": "20.1",
#                             "itemRecordNo":"",
#                             "itemName":"",
#                             "barCode":"",
#                             "note":""
#                         }
#                     ],
#                     "logisCompanyCode": "3301980093",
#                     "logisCompanyName": "test",
#                     "purchaserTelNumber": "test",
#                     "declareCompanyCode": "3301980100",
#                     "orderNo": "o201508080030",
#                     "param1": "",
#                     "param2": "",
#                     "sendAddress": "浙江省西湖区杭州市文三路90号501",
#                     "sendName": "李四",
#                     "sendTel": "13512341234",
#                     "batchNo": "132412341",
#                     "busiType": "1"}}

post_data = {
    # 'name': 'wjw',
    # 'idNo': '111111',
    'user_id': 141
}

# r = requests.post("http://www.gabeniscoming.com/codeigniter/php/Authen/appearance", data=post_data)

post_data = {
    # 'name': 'wjw',
    # 'idNo': '111111',
    'user_id': 1000,
    'authen_id':22
}

#r = requests.post("http://www.gabeniscoming.com/codeigniter/php/Authen/delete", data=post_data)

post_data = {
    'name': 'wjw',
    'idNo': '522701199310146224',
    'user_id': 1000,
    # 'authen_id': 23
}

r = requests.post("http://www.gabeniscoming.com/codeigniter/php/Authen/add", data=post_data)
print(r.text)
# print(r.cookies)
# print(r.url)
