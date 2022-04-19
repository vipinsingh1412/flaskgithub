import json

bankfile=open('./jsonfile/bankDetail.json','rt')
bankdata=bankfile.read()
print(bankdata)
bankobj=json.loads(bankdata)
print(bankobj["bankDetail"]['name'])
bankobj["bankDetail"]['name']="vipinsinghrajput"
bankobjson=json.dumps(bankobj)
print(bankobjson)


