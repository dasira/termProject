from kakao import *

dict = {}
#찾는 주소들
def FindAddress(i):
    return str[i]

row = ['강서구', '양천구', '구로구', '금천구', '영등포구', '동작구', '관악구', '서초구', '강남구'
'송파구', '강동구', '마포구', '은평구', '서대문구', '종로구', '중구', '용산구', '강북구'
'성북구', '동대문구', '성동구', '도봉구', '노원구', '중량구', '광진구']
#구 이름

for i in row:
    if FindAddress(i) in dict:
        dict[FindAddress(i)].append(i)
    else:
        dict[FindAddress(i)] = [i]

for i in dict['마포구']:
    print(i)

print(dict)