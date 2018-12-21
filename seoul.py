import requests
import time
import json
from datetime import datetime

def get_total_info():
    
    url = "http://www.seoul-escape.com/reservation/change_date/"
    params = {
        'current_date' : '2018/12/21'
    }
    response = requests.get(url,params = params).text
    document = json.loads(response)
    
    cafe_code = {
        '강남1호점':3,
        '홍대1호점':1,
        '부산 서면점':5,
        '인천 부평점':4,
        '강남2호점':11,
        '홍대2호점':10
    }
    total = {}
    game_room_list = document["gameRoomList"]
    #print(game_room_list)
    
    #기본틀 만들기
    for cafe in cafe_code :
        total[cafe] = []
        for room in game_room_list :
            if(cafe_code[cafe]==room["branch_id"]):
                total[cafe].append({"title":room["room_name"],"info":[]})
    
    #print(total)
    #앞에서 만든 틀에 데이터 집어넣기
    book_list = document["bookList"]
    booked = ""
    for cafe in total :
        for book in book_list :
            if(cafe == book["branch"]):
                for theme in total[cafe]:
                    if theme["title"]==book["room"]:
                        if(book["booked"]):
                            booked = "예약완료"
                        else :
                            booked = "예약가능"
                        theme["info"].append("{} - {}".format(book["hour"],booked))
                    
    return total
    #print(document)
    #print(document["gameRoomList"])
    #print(document["bookList"])
    #for book in document["bookList"] :
     #   print(d["room"])
    '''
    cafe_info=[]
    for d in document["bookList"]:
        cafe = {
            "booked": d["booked"],#true이면 예약완료
            "branch": d["branch"],
            "hour": d["hour"],
            "room": d["room"]}
        cafe_info.append(cafe)    
    #cafe_info["hour"].sort()
    print(cafe_info)
    '''
    
def seoul_escape_list():
    total = get_total_info()
    return total.keys()
    
def seoul_escape_info(cd):
    total = get_total_info()
    cafe = total[cd]
    tmp = []
    for theme in cafe:
        tmp.append("{}\n{}".format(theme["title"],'\n'.join(theme["info"])))
    
    return tmp




print(seoul_escape_info("홍대1호점"))