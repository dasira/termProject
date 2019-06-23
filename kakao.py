import requests, json

def xyAddress(x,y):
    url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x="+str(x)+"&y="+str(y)
    headers = {"Authorization": "KakaoAK 9e417ab9221917a776c0a805a8ac51c4"}
    result = json.loads(str(requests.get(url, headers=headers).text))
    match_first = result['documents'][0]
    gooName = match_first['region_2depth_name']
    return gooName

#xyAddress(127.124718,37.541805)