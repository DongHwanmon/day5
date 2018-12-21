#20181220~20181221

## parameter란?

#### html form 을 이용해서 브라우저로 부터 서버로 데이터를 함께 전송하기!

#### ### 아파트 매매 내역 시스템을 이용해 내가 원하는 실거래가 검색하기

위치 : "JIBUN_NAME"

아파트 이름 : "BLDG_NM"

실거래가 : "SUM_AMT"

실거래월 실거래일 : "DEAL_MM", "DEAL_DD"

전용면적 : "BLDG_AREA"

### telegram 챗봇 코드 간단 리뷰!





환경변수 등록하기

vi ~/.bashrc 입력하면 환경변수 주르륵 나오는데 shitf +g 누르면 맨끝으로 감

그리고 i를 누르면 그자리에서 insert 모드

o를 누르면 다음줄에 insert 모드가 된다

그리고 끌때는 :wq여기서 w는 저장 q는 종료

등록된 환경변수를 쓰기 위해서 

source  ~/.bashrc 입력

확인하기 위해서

echo $등록한 환경변수이름

제대로 나오면 성공



서버동작 시킬때

flask run --host 0.0.0.0 --port 8080



 cd .. 상위폴더로 옮길때

rm 파일이름 - 파일 삭제할때 

git init
처음 폴더 만들고 폴더에 git.파일 없을때 만드는 명령어

git add README.md
이거 올릴준비 하라는 명령어

git status 
어느부분이 바뀌었는지 알려주는 명령어

git diff
구체적으로 어디가 바뀌었는지 알려주는 명령어

git commit -m "first commit"
첫번째 커밋이라는 것을 언급하고 깃에 생성한다. 새로운것을 올리고 싶을때마다 다시 명령해야한다.

git remote add origin (여기에는 깃헙주소~)
원격으로 어디에 저장을 할건지 연결을 시키는 명령어

git push -u origin master
등록한 허브에 올린다



html에서 클래스 별명일때는 .을 붙여서 검색

ID로 검색할떄는 #아이디로 검색
빈칸을 띄우면 그 클래스 안에 있는것에서 띄우고 쓴 것을 검색한다는 의미