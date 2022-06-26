""""
传入组织id获取组织下的所有班次
然后遍历并且修改组织下的所有班次
"""
import requests as rq
import json
from datetime import *
date1 = "23:59"
date1 = datetime.strptime(date1, "%H:%M")
def getShifts(orgId):
    url='https://oretail-ind.myoppo.com/biz-hr/attendance/web/shift/searchShift?page=1&size=10&organizationId='+orgId+'&type=0'
    header={'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRUeXBlIjoiMSIsImFjY291bnRJZCI6Ijg4NjE5IiwidGVuYW50R3JvdXBJZCI6IjciLCJ1c2VyX25hbWUiOiIxMjMxeSIsInNjb3BlIjpbInJlYWQiXSwibG9naW5OYW1lIjoiMTIzMXkiLCJsb2dpbkNvZGUiOiIxMjMxIiwidGVuYW50Q29kZSI6IjEyMzEiLCJleHAiOjE2NTYyNjUzNzYsImp0aSI6IjFjMzI0NzBkLTA4MDAtNGQ2NS04NDM0LTdhNGI4Yjc4MWFmZiIsImNsaWVudF9pZCI6IlNTT19QQyJ9.EAFZ6MrqukNJmBh1qE49Vx_JGK01SpBcb03RZQJ0-_13NH9nNcvxCy0PKyvxlpgqxH5NMOg2bRSs7GzH8rlq_zfQ7FiZX520UVsMBDwM7O-bVJPck-XRoRFRlcAFbKMss476UEGxobpj4A7mnu3MHNjdJSCkVn1GktkhOPQGXr5-ESKajJynvD4KOCKcbfbOxW1aglqRFU0FE4Wx4g1Wus_BcQI3Oz8-iN2U14tiJNxPQkJHEatV5EgvgmOeSJchHdUty4jcoujbRv8iP57Sl-6ywK_nvvbJtfd8YrGodGkoEKoxEdpLNLOatjjwtqrRrYp1ROXru_n_SFcFZG1MmA','Content-Type':'application/json'}
    back=rq.get(url=url,headers=header)
    for i in json.loads(back.text)["content"]:

        # i["organizationId"]=int(orgId)
        # i["multipleStatus"]=str(i["multipleStatus"])
        # i.pop('seriousLateMinutes')
        # date2 =i["shiftDetails"][0]['workEndTime']
        # date2 = datetime.strptime(date2, "%H:%M")
        # duration = date1 - date2
        # i["shiftDetails"][0]["endDelayTime"]=int(duration.seconds/60)
        # i["shiftDetails"][0].pop('id')
        # url1='https://oretail-ind.myoppo.com/biz-hr/attendance/web/shift/saveShift'
        # body=json.dumps(i)
        # rq.post(url=url1,data=body,headers=header)
        url1='https://oretail-ind.myoppo.com/biz-hr/attendance/web/shift/deleteShift?id='+i['id']
        rq.get(url=url1,headers=header)
        print(i['name']+'被删除')


        # print(json.dumps(i))






allorgs=["6150",
         "6149",
         "6148",
         "6147",
         "6146",
         "6029",
         "6145",
         "6144",
         "6143",
         "6142",
         "6141",
         "6140",
         "6139",
         "6138",
         "6137",
         "6136",
         "6135",
         "6134",
         "6133",
         "6132",
         "6131",
         "6130",
         "6129",
         "6128",
         "6127",
         "6126",
         "6125",
         "6124",
         "6123",
         "6122",
         "6121",
         "6120",
         "6119",
         "6118",
         "6117",
         "6116",
         "6115",
         "6114",
         "6113",
         "6112",
         "6111",
         "6110",
         "6109",
         "6108",
         "6107",
         "6106",
         "6105",
         "6104",
         "4062",
         "6103",
         "6102",
         "6023",
         "6025",
         "6026",
         "6101",
         "6100",
         "6099",
         "6098",
         "6097",
         "6096",
         "6095",
         "6094",
         "6093",
         "6092",
         "6091",
         "6090",
         "6089",
         "6088",
         "6086",
         "6085",
         "6084",
         "6083",
         "6082",
         "6081",
         "6080",
         "6079",
         "6078",
         "6077",
         "6076",
         "6075",
         "6074",
         "6073",
         "6071",
         "6070",
         "6069",
         "6068",
         "6067",
         "6066",
         "6065",
         "4017",
         "6064",
         "6063",
         "6062",
         "6061",
         "6060",
         "6059",
         "6058",
         "6057",
         "6056",
         "6055",
         "6054",
         "6053",
         "6052",
         "6051",
         "6050",
         "6049",
         "6048",
         "6047",
         "6046",
         "6045",
         "6044"
         ]
for aa in allorgs:
    getShifts(aa)

