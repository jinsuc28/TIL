# AWS ubuntu

# First, EC2 사용하여 ubuntu 서버 생성하기

1. 인스턴스 시작하여 만들기
- 이름, os, 인스턴스 유형 정하기
- 키 페어 생성 : ec2와 매칭 될 수 있는 키파일명

생성하면 .pem 파일 형식으로 다운이 되며 잃어버릴 경우 키를 재발급 받아야한다.

- 보안그룹생성

혼자 사용할 경우 **보안 그룹 생성**(기본)해도 되지만 여러사람이 쓰는 서버의 경우 **기존 보안 그룹** 선택하자(보안그룹에서 만들어야함! )

2. ec2 메뉴 중 보안그룹에 들어가서 **보안그룹 생성**하자
- 보안 그룹 이름, 설명 입력
- 인바운드 규칙

유형: **ssh**, 소스: anywhrere ipv4 설정하면 됨

- ip를 공개하여 **웹 배포**를 하고 싶다면 **인바운드 규칙에서 규칙 추가**해줘야함

유형: **http**, 소스: anywhere ipv4 설정하자(anywhere하면 보안이 약하지만 실습용으로 괜찮다.)

- 보안 그룹 생성

3. 인스턴스 생성으로 돌아가서 보안 그룹 선택
4. 인스턴스 생성

# Second, 터미널에서 서버 연결

1. **ssh -i [파일명].pem ubuntu@[퍼블릭ipv4 주소]**    >입력하자
2. 최초 접속시 **yes** 입력

***주의** 

- 키 파일은 폴더 안에 있어야 접속가능(폴더 x 경우 안전하지 않아서 permision denied )
- permission 권한을 낮게 준 경우 **chmod 600 [파일명].pem**     입력
- 너무 넓게 공개된 경우도 안됨 (-rw-rw-rw-)

# Third, 서버 제어 실습

## **AWS 서버 메모리 늘려보기**

1. 인스턴스 상태 (종료는 서버 삭제를 의미)
- 종료 눌러도 삭제 안되도록 **인스턴스 설정**에서 **종료 동작 변경** →**중지로 변경**
2. 파티션(디스크) 용량 늘리기

- **물리적으로(HW)** 디스크 확장과 **SW 적**으로 디스크를 확장해야함 

3. EBS(Elastic Block Store)의 볼륨 들어가기
- 인스턴스에 맞게 생성된 볼륨을 찾고 **볼륨수정**
- 크기 늘리기
- **물리적 용량 증설 완료**됨
4. 터미널에서 용량 확인

- dmesg -T 혹은 sudo dmesg -T

ex) nvme(storage는 hdd,ssd 그리고 nvme 있음) : detected capacity change from 20971520 to 31457280

5. SW 적 용량 증가
- df -h   : SW적 용량 확인(처음만 보면 됨)
- sudo growpart /dev/nvme0n1 1   : 어느 위치 확장 할 것인지 알려줌
- df -h 와 lsblk  : 확장될 용량 확인

- sudo resize2fs /dev/nvme0n1p1
- sudo resize2fs /dev/nvme1n1

위 두 명령을 통해 디스크 용량 증가 완료

## **인스턴스 유형 변경**

1. 인스턴스 상태 중지로 변경
2. 인스턴스 유형 변경
3. 인스턴스 상태 실행으로 변경
4. 보안을 anywhere로 했기 때문에 고정ip 아님 따라서 ip주소가 중지 실행마다 바뀜

퍼블릭 ipv4 주소 복사 및 복사 주소로 재접속

5. 서버의 프로세스(core개수) 및 메모리(ram) 용량 확인

- cat /proc/cpuinfo | grep processor

- cat /proc/meminfo | grep Total

- 또는 htop으로 확인 가능


## **서버 웹서버 설치**

1. sudo apt update && sudo apt install nginx -y   :필요 라이브러리 설치
2. curl [localhost](http://localhost)  :웹서버 동작 확인
3. 퍼블릭 ipv4 주소 검색창에 입력
- 이전 보안 설정에서 유형: http 설정했기 때문에 들어가짐 http 없으면 보안 거부됨
4. 웹페이지 수정해서 열어보자
- sudo sh -c “echo ‘Hello YearDreamSchool from shpark’ > /var/www/html/index.html”
- curl [localhost](http://localhost)    :입력확인
5. ip주소 인터넷 검색창에 입력하면 잘 나옴