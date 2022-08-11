# Linux apt&daemon

AWS 고정ip주소 한달 이용료 4천원 정도

# 패키지 설치하기 업데이트 및 업그레이드

소스코드 → complie → install

패키지: 위 과정을 한번에 설치하기 쉽게 만들어 놓은 것

패키지 관리자 apt-get을 통해서 

- apt list :리포지토리 패키지 목록 출력 (로컬 캐쉬)

- apt update : 최신버전 목록을 가져오는 것 (버전 업 설치가 아니다!! )

- apt remove : apt를 지우는 것(설정 파일은 유지)
- apt purge : 설치된 패키지 삭제 + 설정파일 삭제

정말 안쓸거면 apt purge 해야 함

apt upgrade 할 때 설정파일은 유지하고 패키지만 삭제해야하므로 불필요한

자원 낭비를 안하기 위해서 remove와 purge 로 구분 됨

또한, 같은 라이브러리라도 재단 따라 다를 수 있음

# Daemon

nginx 와 같은 소프트웨어와는 다르게 웹서버를 동작시키기 위해서는

계속 라이브러리가 돌아가야됨

이러한 것들을 daemon 이라고 한다.

- systemctl status [데몬서비스]: 데몬 시스템이 잘 돌아가는 지 확인하는 것

ex) ststemctl status nginx 

- systemctl start [데몬서비스]: 서비스 시작
- systemctl stop [데몬서비스]: 서비스 중지
- systemctl restart [데몬서비스]: 서비스 재시작
- systemctl reload [데몬서비스]: 설정 재로드
- systemctl disable [데몬서비스]: 부팅시 서비스 자동 시작 삭제
- systemctl enable [데몬서비스]: 부팅시 서비스 자동 시작

데몬을 stop하더라도 껏다 키면 돌아가게 설정되어있음

이때 disable 을 써야 함 disable 하더라도 서비스가 꺼지지는 않음 왜냐하면 서버를 껏다 켰을 때 

상태를 말하는 것임

daemon 서비스는 4가지 상태가 있음 :  (active enable), (inactive enable), (active disable), (inactive disable)

패키지 설치는 관리자만 할 수 있음

- sudo apt install nginx : 웹서버를 사용하기위해서
- curl [localhost](http://localhost)  : 기본적인 웹 html이 출력됨

curl [localhost](http://localhost) 는 curl 127.0.01과 같은 것

나 자신의 호스트에 이 pc 내에서 접속하는 것 

10.0.2.2 xxxxx 내부(사설ip)

172.17.x.x 내부(사설ip)

- curl [ipconfig.io](http://ipconfig.io) : 현재 ip 주소

- systemctl status nginx : nginx 데몬에 대한 현재 서비스 확인
- sudo systemctl stop nginx : 데몬을 꺼버림

# symbolic link 활용

하나의 앱서버를 여러개의 웹페이지를 구성할 수 있음 이때 심링크 사용

ex) a,b,c 쇼핑몰이 있을 때 하나를 심링크를 만들고 서버점검을 하고 싶을 때 하나만 끌 수 있음

- ls -al /etc/nginx/sites-available/ : 활성화되어 있는 사이트
- ls -al /etc/nginx/sites-enabled/  : 비활성화 한 사이트

- tail /var/log/nginx/access.log : nginx의 로그를 볼 수 있음
- ls -al /etc/localtime : 시간을 보면 기본적으로 utc 기준으로 설정됨 →seoul 바꾸자
- ls -al /usr/share/zoneinfo : 모든 나라의 표준 시가 보임
- s -al /usr/share/zoneinfo/Asia/Seoul : 우리나라 표준시를 /etc/localtime 여기에 symbol 해줘야 함

이를 위해서 /etc/localtime 

- sudo ln -s /etc/localtime /usr/share/zoneinfo/Asia/Seoul : /etc/localtime 심볼릭을 /usr/share/zoneinfo/Asia/Seoul 로 변경한다.

이전 심볼릭 예시

ex) ln -s hello.txt hellosym

- sudo ln -s usr/share/zoneinfo/Asia/Seoul/etc/localtime : 서울 심볼릭 시간의 시간파일을 만듬
- sudo ln -sf usr/share/zoneinfo/Asia/Seoul/etc/localtime : 이미 존재한다면 덮어쓰기도 가능 -f는 강제실행
- git commit -f : 상대방 커밋한 것을 날려버릴 수 있음

nginx 와 비슷한 웹서비스 apache2

- sudo apt install apache2

nginx와 apache2와 같은 데몬 서비스

하지만, ftp 는 거의 사용 안됨(보안문제)

- sudo apt install vsftpd

# mysql

apt search mysql : mysql 패키지가 apt 서비스를 제공하는 지 확인

모든 log는 /var/log 쌓임

sudo apt install mysql-server : mysql 설치하기

## **mysql 접속 방법 두가지**

관리자 모드(설정 초기)

사용자 모드 db user

# 개발환경 구축하기

# 아나콘다

apt는 아나콘다 제공 안함

따라서 소스코드,컴파일,설치 직접해줘야 함

500mb 쉘스크립트 모두 바이너리

- **curl -O https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh**
- sh Anaconda3-2020.02-Linux-x86_64.sh
- export PATH=~/anaconda3/bin:$PATH :만약 init no 하면 환경변수 설정을 해줘야함

# 하둡

원래 EC2 접속할 때 비밀번호 필요하지만 aws 에서 없어도 접속하도록 설정해놔서 가능한 것이다

원래는 비밀번호 입력해야 함 

환경변수는 .bash_aliases 에다가 저장해도 적용된다.

source .bashrc를 불러야 지 적용 됨

# 기타 유용한 내용

- df -h : 인스턴스 현재 자원 확인
- htop : 자원 확인 가능
- vi 에서 / 입력 : 입력한 단어들을 찾을 수 있음

vscode 에서 포트를 자체적으로 열수도 있음 ,aws에서 sg 추가할 필요 없음

- cat /proc/cpuinfo | grep proce : cpu 확인하기
- cat /proc/meminfo | grep Total : 인스턴스 자원 확인하기