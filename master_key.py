from bs4 import BeautifulSoup as bs#html
import requests
import time
from datetime import datetime

#datetime.today().strftime("%Y/%m/%d %H:%M:%S")  # YYYY/mm/dd HH:MM:SS 형태의 시간 출력




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
        

#li = document.select('escape_view')
#print(li)

#print(master_key_list())

#split('=') #=의 앞뒤로 자른다
#for cafe in master_key_list() :
#    print('{} : {}'.format(cafe["title"],cafe["link"].split('=')[1]))
    
#print(master_key_info(2))

#사용자로부터 '마스터키 ****점' 이라는 메시지를 받으면 공백으로 스플릿해서 지점명을 얻어낸다

#해당 지점에 대한 오늘의 정보를 요청하고(크롤링),
#메시지(예약정보)를 보내준다.



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
    
print(master_key_list())