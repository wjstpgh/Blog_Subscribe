# Blog_Subscribe

블로그 페이지를 두개로 나누어 ab테스트를 진행해 어떤 페이지가 더 구독자 수가 높은지 확인하며
이를 위해 이메일을 입력받는 구독기능과 사용자로그와 접속기록로그를 DB에 저장하여 관리하는 프로젝트

### 기능 소개

![image](https://user-images.githubusercontent.com/26988563/183300099-c09fd3f8-b0b2-43a9-8155-e8281cdfd73b.png)

> 해당 블로그 페이지에서 이메일을 입력하고 구독을 한다.
***

![image](https://user-images.githubusercontent.com/26988563/183300196-39e52e4f-1853-4b66-bfee-faa22ba628e3.png)

> 페이지의 세션은 사용자의 ip와 이메일을 기억하여 구독자가 접속 시 30일간 로그인된 페이지를 나타낸다.
***

![image](https://user-images.githubusercontent.com/26988563/183300437-bdb06852-f53c-4c5e-882a-7bcce15bf205.png)

> 구독취소 버튼을 누르면 사용자 정보와 세션정보는 다시 삭제되며 a,b페이지가 다시 번갈아 나타난다.
***

![image](https://user-images.githubusercontent.com/26988563/183300596-f270513c-a0c0-4047-8463-c893f31fc070.png)

> 접속 로그는 MongoDB에 저장되며 네 개의 속성을 가진다.
> * session_ip : 사용자가 접속한 ip 주소
> * user_email : 사용자의 이메일 주소, 만약 구독하지 않는 사용자라면 'anonymous'로 표현
> * page : abtest를 위한 속성, 어떤 페이지에서 구독자가 더 많이 나왔는지 확인가능
> * access_time : 접속시간
***

![image](https://user-images.githubusercontent.com/26988563/183301212-07da41b8-7c7d-43c5-a229-ed89d5fc9f7b.png)

> 구독자 정보는 Mysql에 저장되며 이메일 주소와 블로그 페이지 두 필드를 가진다.

***

### 배포

* 배포를 위한 ngrok실행

![image](https://user-images.githubusercontent.com/26988563/183256720-ff439d84-1778-4e6a-9353-8fdd3cbfe4c9.png)

* 로컬서버를 실행시켜 둔 상태에서

![image](https://user-images.githubusercontent.com/26988563/183256838-e486657e-219d-4020-ba89-e4e105451309.png)

* ngrok실행에서 나온 포워딩 주소와 라우팅경로를 입력

![image](https://user-images.githubusercontent.com/26988563/183256880-2292c941-01ca-44f3-9f77-000f33f7eb26.png)

* ngrok을 통해 배포 테스트가 완료된 상태

![image](https://user-images.githubusercontent.com/26988563/183257206-ff204fe5-bd03-411e-a26f-95718e0d4fdc.png)

