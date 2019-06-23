import urllib.request, json, urllib.parse
from kakao import *

def GetInfo():
    server1="http://openapi.seoul.go.kr:8088/544a4442516461733935616e584271/json/bikeList/1/1000/"
    response = urllib.request.urlopen(server1)
    data1 = json.loads(response.read())
    server2="http://openapi.seoul.go.kr:8088/544a4442516461733935616e584271/json/bikeList/1001/2000/"
    response = urllib.request.urlopen(server2)
    data2 = json.loads(response.read())
    data1.update(data2)

    rent = data1['rentBikeStatus']
    row = rent['row']
    #한 번에 받아오기 성공

    # stationLatitude
    # stationLongitude
    # 받아온 정보들에 지역구 정보 추가
    del row[-2:] #끝에 위트콤 위트콤 공장 삭제

    for i in row:
        i['gooName'] = xyAddress(i.get('stationLongitude'),i.get('stationLatitude'))
        print(i)


    return row



   ##while(1):
    #   choose = int(input("1.지역구 검색  2.대여소명 검색 "))
    ##    if choose == 1:
    #       name = (input("찾으시는 지역구를 입력하시오: "))
    #       if name[-1]!='구':
    #           name+='구'
    #           print(name)
    #       for i in row:
    #           if name == str(i.get('gooName')):
    #               print(i)
    #   elif choose == 2:
    #       name = (input("찾으시는 대여소명을 입력하시오: "))
    #       if name==' ':
    #           print("잘못된 입력")
    #           pass
    #       for i in row:
    #           #str(i.get('stationName'))
    #           if name in str(i.get('stationName')):
    #               print(i)

GetInfo()


