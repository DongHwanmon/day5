from flask import Flask, request
from bs4 import BeautifulSoup as bs
from datetime import datetime
import requests
import json
import time
import os



app = Flask(__name__)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN') 
TELEGRAM_URL = 'https://api.hphk.io/telegram'

CAFE_LIST = {
    "전체" : -1,
    "부천점" : 15,
    "안양점" : 13,
    "대구동성로2호점" : 14,
    "대구동성로점" : 9,
    "궁동직영점" : 1,
    "은행직영점" : 2,
    "부산서면점" : 19,
    "홍대상수점" : 20,
    "강남점" : 16,
    "건대점" : 10,
    "홍대점" : 11,
    "신촌점" : 6,
    "잠실점" : 21,
    "부평점" : 17,
    "익산점" : 12,
    "전주고사점" : 8,
    "천안신부점" : 18,
    "천안점" : 3,
    "천안두정점" : 7,
    "청주점" : 4}

@app.route('/{}'.format(os.getenv('TELEGRAM_TOKEN')),methods = ['POST'])
def telegram():
    #텔레그램으로부터 요청이 들어올 경우, 해당 요청을 처리하는 코드
    
    token = os.getenv('TELEGRAM_TOKEN')

    #url = 'https://api.hphk.io/telegram/bot{}/getUpdates'.format(token)
    #getUpdates을 이용하여 c9에서 getupdates라는 메소드를 보내면
    #msg가 우리에게 응답으로 돌아온다(c9으로)
    #response = json.loads(requests.get(url).text)
    response = request.get_json()
    chat_id = response["message"]["from"]["id"]
    msg = response["message"]["text"]
    
    
    if msg == "안녕" :
        msg = "첫만남에는 존댓말을 하셔야죠"
    elif msg == "안녕하세요" :
        msg = "ㅋㅋㅋㅋㅋㅋ"
    elif msg.startswith("서이룸") :
        cafe_name = msg.split(" ")
        if(len(cafe_name)>2):
            #python how to join from 2 to 4
            #x[3:6]= ' '.join(x[3:6])
            cafe_name = ' '.join(cafe_name[1:3])
            data = seoul_escape_info(cafe_name)
            print(cafe_name)
        else:
            cafe_name = cafe_name[-1]
            if cafe_name =="전체" :
                data = seoul_escape_list()
            else :
                data = seoul_escape_info(cafe_name)
        
        msg = '\n'.join(data)
        
    elif msg.startswith("마스터키") :
        cafe_name = msg.split(" ")[1]
        cd = CAFE_LIST[cafe_name]
        
        if cd > 0:
            data = master_key_info(cd)
        else :
            data = master_key_list()
        msg = []
        
        for d in data :
            msg.append('\n'.join(d.values()))
                
        msg = '\n'.join(msg)
        
        
    else :
        msg = '등록되지 않은 지점입니다.'
    #마스터키 전체
    #마스터키 ****점
    
    '''
    
    if msg == "안녕" :
        msg = "첫만남에는 존댓말을 하셔야죠"
    elif msg == "안녕하세요" :
        msg = "ㅋㅋㅋㅋㅋㅋ"
    elif msg == "환율" :
        money_url = 'http://finance.daum.net/api/exchanges/summaries'
        money_headers = {
            "Host": "finance.daum.net"
            ,"Referer": "http://finance.daum.net/exchanges"
            ,"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
                }
        money_response = requests.get(money_url,headers = money_headers).text
        money_document = json.loads(money_response)
            
        money_info=[]
            
        for d in money_document["data"]:
            money_info.append({"name":d["name"],
                        "basePrice":d["basePrice"]})
            
        msg =""
        #msg = money_info
        
        for m in money_info:
            msg = msg + str(m["name"])+" : "+str(m["basePrice"])+"\n"
       '''     
   #''.join(l)
   #여러개의 배열이 있을때 문자열로 바꿔준다.
   #'\n'.join(l)
   #\이 삽입되서 연결된 문자열로 바꿔준다.
   
    url = 'https://api.hphk.io/telegram/bot{}/sendMessage'.format(token)
    #위 주소에 해피해킹인 이유는  c9서버에서 텔레그램서버에 신호보내는 것을 막았기 때문에
    #한번 우회하여 해피해킹 서버에서 텔레그램으로 대신 보내게 된다.
    #sendmessage를 통해서 텔레그램에서 사용자에게 보내게 된다.
    chat_id = response["message"]["from"]["id"]
    #아이디가 있어야 응답을 보내게 요청할 수 있다.
    requests.get(url,params = {"chat_id":chat_id,"text":msg})
    #get이지만 요청을 보낸다!
    #requests를 했기때문에 
    #requests와 request는 다르다 request는 들어온 요청을 의미
    #requests는 요청을 해서 돌아오게 되는 값? 링크를 보여줌?
    
    return '',200
    #이것은 응답코드
    
@app.route('/set_webhook')
def set_webhook():
    url = TELEGRAM_URL+'/bot'+TELEGRAM_TOKEN+'/setWebhook'
    #텔레그램웹에서 내가 만든 봇이 메시지를 받으면 그때 그때마다
    #내가 등록한 url로 alert를 보내기 위해서 웹훅을 이용
    #위 주소는 텔레그램에서 지정된 형식!
    params = {
        'url':'https://ssafy-week2-donghwanmon.c9users.io/{}'.format(TELEGRAM_TOKEN)
    }
    
    response = requests.get(url,params = params).text
    return response


def master_key_info(cd):
    today = datetime.today().strftime("%Y-%m-%d")
    print(today)
    url = "http://www.master-key.co.kr/booking/booking_list_new"
    requests.post(url)
    params = {
        "date": today,
        "store": cd
    }
    
    response = requests.post(url,params).text
    document = bs(response,'html.parser')
    ul = document.select('.reserve .escape_view')#별명의 종류가 클래스니까 . 
    
    theme_list = []
    for li in ul :
        title = li.select('p')[0].text#여러개면 .text가 안되고 몇번째인지 정해줘야지 .text가 된다.
        #print(li.select('.col'))
        info = ''
        for col in li.select('.col'):
            info = info +'{} - {}\n'.format(col.select_one('.time').text,col.select_one('.state').text)
        theme={
            "title" : li.select('p')[0].text,
            "info" : info
        }
        theme_list.append(theme)
    
    
    return theme_list

def master_key_list():
        
    url = "http://www.master-key.co.kr/home/office"
    response = requests.get(url).text
    document = bs(response,'html.parser')
    lis = document.select('.escape_list .escape_view')#별명의 종류가 클래스니까 . 
                                        #별명의 종류가 아이디인경우에는 #을 붙인다.
    #print(lis)
    #print(len(lis))
    cafe_lists=[]
    
    for li in lis :
        #python how to eliminate string from string
        title = li.select_one('p').text
        if(title.endswith('NEW')):#문자열에 NEW로 끝나면 문자열 뒤에 3개를 자름
            title = title[:-3]
        
        address = li.select('dd')[0].text
        tel = li.select('dd')[1].text
        link = 'http://www.master-key.co.kr'+ li.select_one('a')["href"]
    
        '''
        cafe_list = {
            'title': title,
            'tel':li.select('dd')[1].text,#text를 안붙이면<dd></dd>도 나오게 된다.
            'address':li.select('dd')[0].text,
            'link':'http://www.master-key.co.kr'+li.select_one('a')["href"]
        }
        '''
        cafe_list = {
            'title': title,
            'tel':tel,
            'address':address,
            'link':link
        }
        
        cafe_lists.append(cafe_list)
    return cafe_lists
    
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
