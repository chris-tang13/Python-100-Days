""""
传入组织id获取组织下的所有班次
然后遍历并且修改组织下的所有班次
"""
import requests as rq
import json
from datetime import *

rawdata=[{"name":"10:00-21:30","允许上班开始打卡时间":"09:30","允许上班结束打卡时间":"11:59","允许下班打卡开始时间":"21:00","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"10:00","workEndTime":"21:30","restStartTime":"14:00","restEndTime":"15:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"10:30-21:30","允许上班开始打卡时间":"09:30","允许上班结束打卡时间":"11:59","允许下班打卡开始时间":"21:00","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"10:30","workEndTime":"21:30","restStartTime":"14:00","restEndTime":"15:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"11:00-21:30","允许上班开始打卡时间":"09:30","允许上班结束打卡时间":"11:59","允许下班打卡开始时间":"21:00","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"11:00","workEndTime":"21:30","restStartTime":"14:00","restEndTime":"15:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"11:30-21:30","允许上班开始打卡时间":"09:30","允许上班结束打卡时间":"11:59","允许下班打卡开始时间":"21:00","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"11:30","workEndTime":"21:30","restStartTime":"14:00","restEndTime":"15:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"12:00-20:30","允许上班开始打卡时间":"11:30","允许上班结束打卡时间":"13:59","允许下班打卡开始时间":"20:00","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"12:00","workEndTime":"20:30","restStartTime":"14:00","restEndTime":"15:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"12:00-21:00","允许上班开始打卡时间":"11:30","允许上班结束打卡时间":"13:59","允许下班打卡开始时间":"20:30","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"12:00","workEndTime":"21:00","restStartTime":"14:00","restEndTime":"15:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"12:00-22:00","允许上班开始打卡时间":"11:30","允许上班结束打卡时间":"13:59","允许下班打卡开始时间":"21:30","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"12:00","workEndTime":"22:00","restStartTime":"14:00","restEndTime":"15:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"12:30-22:00","允许上班开始打卡时间":"11:30","允许上班结束打卡时间":"13:59","允许下班打卡开始时间":"21:00","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"12:30","workEndTime":"22:00","restStartTime":"14:00","restEndTime":"15:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"13:00-21:00","允许上班开始打卡时间":"11:30","允许上班结束打卡时间":"13:59","允许下班打卡开始时间":"20:30","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"13:00","workEndTime":"21:00","restStartTime":"14:00","restEndTime":"15:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"13:00-22:00","允许上班开始打卡时间":"11:30","允许上班结束打卡时间":"13:59","允许下班打卡开始时间":"21:30","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"13:00","workEndTime":"22:00","restStartTime":"14:00","restEndTime":"15:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"14:30-23:00","允许上班开始打卡时间":"14:00","允许上班结束打卡时间":"15:59","允许下班打卡开始时间":"22:30","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"14:30","workEndTime":"23:00","restStartTime":"16:00","restEndTime":"17:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""},
         {"name":"15:30-23:30","允许上班开始打卡时间":"14:00","允许上班结束打卡时间":"15:59","允许下班打卡开始时间":"22:30","允许下班打卡结束时间":"23:59","multipleStatus":"0","absenteeismLateMinutes":"29","remarks":"","workStartTime":"15:30","workEndTime":"23:30","restStartTime":"16:00","restEndTime":"17:00","endAdvanceTime":"","endDelayTime":"","startAdvanceTime":"","startDelayTime":""}]
for i in rawdata:
    i['shiftDetails']=[{'a':13}]
    i['shiftDetails'][0]['workEndTime']=i['workEndTime']
    i['shiftDetails'][0]['workStartTime']=i['workStartTime']
    date2 =i['允许上班开始打卡时间']
    date3=i['workStartTime']
    date4=i['允许上班结束打卡时间']
    date2 = datetime.strptime(date2, "%H:%M")
    date3 = datetime.strptime(date3, "%H:%M")
    date4 = datetime.strptime(date4, "%H:%M")

    i['shiftDetails'][0]['startAdvanceTime']=(date3 - date2).seconds/60
    i['shiftDetails'][0]['startDelayTime']=(date4 - date3).seconds/60
    date5 =i['允许下班打卡开始时间']
    date6=i['workEndTime']
    date7=i['允许下班打卡结束时间']
    date5 = datetime.strptime(date5, "%H:%M")
    date6 = datetime.strptime(date6, "%H:%M")
    date7 = datetime.strptime(date7, "%H:%M")
    i['shiftDetails'][0]['endAdvanceTime']=(date6 - date5).seconds/60
    i['shiftDetails'][0]['endDelayTime']=(date7 - date6).seconds/60
    i['shiftDetails'][0]['restStartTime']=i['restStartTime']
    i['shiftDetails'][0]['restEndTime']=i['restEndTime']
    del i['shiftDetails'][0]['a']
    del i['workEndTime']
    del i['workStartTime']
    del i['startAdvanceTime']
    del i['startDelayTime']
    del i['endAdvanceTime']
    del i['endDelayTime']
    del i['restStartTime']
    del i['restEndTime']
    i['absenteeismLateMinutes']=int(i['absenteeismLateMinutes'])








print(rawdata)




















        # i["organizationId"]=int(orgId)
        # i["multipleStatus"]=str(i["multipleStatus"])
        # i.pop('seriousLateMinutes')
        # date2 =i["shiftDetails"][0]['workEndTime']
        # date2 = datetime.strptime(date2, "%H:%M")
        # duration = date1 - date2
        # i["shiftDetails"][0]["endDelayTime"]=int(duration.seconds/60)
        # i["shiftDetails"][0].pop('id')





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

url='https://oretail-ind.myoppo.com/biz-hr/attendance/web/shift/saveShift'
header={'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRUeXBlIjoiMSIsImFjY291bnRJZCI6Ijg4NjE5IiwidGVuYW50R3JvdXBJZCI6IjciLCJ1c2VyX25hbWUiOiIxMjMxeSIsInNjb3BlIjpbInJlYWQiXSwibG9naW5OYW1lIjoiMTIzMXkiLCJsb2dpbkNvZGUiOiIxMjMxIiwidGVuYW50Q29kZSI6IjEyMzEiLCJleHAiOjE2NTYyNjUzNzYsImp0aSI6IjFjMzI0NzBkLTA4MDAtNGQ2NS04NDM0LTdhNGI4Yjc4MWFmZiIsImNsaWVudF9pZCI6IlNTT19QQyJ9.EAFZ6MrqukNJmBh1qE49Vx_JGK01SpBcb03RZQJ0-_13NH9nNcvxCy0PKyvxlpgqxH5NMOg2bRSs7GzH8rlq_zfQ7FiZX520UVsMBDwM7O-bVJPck-XRoRFRlcAFbKMss476UEGxobpj4A7mnu3MHNjdJSCkVn1GktkhOPQGXr5-ESKajJynvD4KOCKcbfbOxW1aglqRFU0FE4Wx4g1Wus_BcQI3Oz8-iN2U14tiJNxPQkJHEatV5EgvgmOeSJchHdUty4jcoujbRv8iP57Sl-6ywK_nvvbJtfd8YrGodGkoEKoxEdpLNLOatjjwtqrRrYp1ROXru_n_SFcFZG1MmA','Content-Type':'application/json'}
for i in allorgs:
    for j in rawdata:
        j['organizationId']=int(i)
        body=json.dumps(j)
        rq.post(url=url,data=body,headers=header)
        print(i)