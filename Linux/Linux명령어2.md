# Linux 명령어2

- history : 지금까지 입력한 명령어들을 다 나오게됨

- ehco $HISTSIZE 로 몇개까지 history 볼 수 있는지 나옴

- 기본적으로 1000개, .bash_history 저장되어있음

# 파이프사용하기

- grep : 특정 패턴 검색(정규표현식 가능)

단어 찾기 같은 것, 파일명, 파일 내용 등등 다 단어 있는지 찾아줌

파이프는 중첩해서 사용 가능

- wc : 줄, 단어, byte 를 세어서 알려준다.

- cat hello.txt | grep -i hello | wc -;

- cat /etc/passwd |grep ubuntu

- cat /var/log/syslog |grep -i error : 오류메세지를 찾고 싶다.

- cat /var/log/syslog |grep -i start

- cat /var/log/syslog | more

- more /var/log/syslog | grep -i error |more

- /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

## 환경변수

- bin : 사용자 binary

- sbin: superuser 용 binary, sudo 권한있어야 사용 가능

echo $PWD, echo $PATH 등등 환경변수 볼 수 있음

- env, pretenv : 환경변수들 한번에 보는 법 (그냥 치면 나옴)

- ^user : user로 시작하는 라인을 찾음

ex) printenv | grep -i ^user : 유저가 써진 환경 변수 라인을 찾을 수 있음

ex) printenv | grep -i user |wc -l : 유저가 써진 라인의 수를 보여줌

- user$ : user로 끝나는 라인

- which [명령어 혹은 라이브러리]: binary 저장된 위치를 보여줌

.bashrc

.profile

BASH 기본적인 표준적으로 생성되는 환경변수 역사적으로 길다보니 같은거지만 같이 표준적으로 생성됨

 

- alias : 현재 정의된 alias 보여줌 , 축약어 임, cd .. 이 아니라 ..으로 뒤로갈 수 잇음

ex) alias .. = ”cd ..”

ex) alias ... = "cd ../..” : 한번에 두칸 이동 가능 

하지만, 서버 종료후 다시들어올 시 초기화됨 .bashrc 에 저장해야지 다시켜도 저장됨

.bashrc 수정은 위험이 크기 때문에 ~/ .bash_aliases 를 만들어 위험성을 줄이자

cat << eof > .bash_aliases : 글을 계속 쓸꺼고 eof 쓰면 끝나고 끝나면 쓴것들 .bash_aliases에 넣어줘

- cd /home : 공통홈

- cd : 나의 홈

# **쉘 스크립트 만들기**

쉘 스크립트 종류

- sh : /bin/sh, /bin/bash, /usr/bin/python 등등 기본적으로 3가지

touch test1.sh

cat << eof > test1.sh

echo “hello”

echo “ hello again”

어떤 종류 쉘 스크립트인지 정의해줘야함

#!/bin/sh

#!/bin/bash

#!/usr/bin/python

#!/usr/bin/perl

이렇게 cat 등으로 실행시켜줘야 함

쉘 실행 방법

sh test1.sh

bash 면 bash 실행

## VI

단, alias와 env 같은 환경변수는 편집하지 못한다.

export로만 가능

i : 편집

esc : 편집모드 탈출

: : 명령모드

w : write 저장

q : quit 종료

:q! : 저장하지 않고 무시하고 종료

! : 변경을 무시

vimtutor : 입력하면 vi 학습할 수 있게 튜토리얼 해볼 수 있음

## vi와 같은 편집기 종류

vim, nano

## nano

nano는 화면 하단에 모드와 명령어가 표신 됨

nano에서 ^는 ctrl 의미

- ^x : 종류

- ^o : 저장

## 기타 명령어

- /tmp/ : 임시폴더, 잠시 만들었다가 삭제될 수 있음

- /var/ : 동적으로 생성되서 고정/가변

- find : 파일을 찾아줌

- find . -name "*.txt”: txt 이름인 것을 다 찾아 줘라

- find . -name "*.txt" | grep hello : hello가 포함된 것만 찾아 줌

- find . -name "*.txt" | grep -v "hello” : hello를 뺀것 만 찾아줘

- stat [파일] : 파일의 날짜, 기타 정보를 알려줌

- file [파일] : 파일의 속성 값, 접근 방법을 알려 줌

- find / -size 100M -exec ls -l {} \;       : find를 루트로 해서 파일 사이즈가 100m 이상인 것들의 결과들의 인자를 {} 넣어서 알려줘라 

## sort

n : 숫자, 안넣으면 영문순

-r : 역순

k : 컬럼

- ls -l | sort -k 5 : 5번째 컬럼 문자순으로

- ls -l | sort -k 9 : 9번째 컬럼 문자순으로

- ls -l | sort -k 2n -k 9 : 두번째 컬럼은 숫자 9번째 컬럼은 글자(영문)로 정렬해라

- sort -k 2 -r < file.txt : 입력받아서 정렬(-r은 역순 reverse)

csv, txt, 파일 잔득있을 때 sort 가능

특정 컬러만 골라내고 싶으면 awk

- ls -l | awk ‘{print $1}’

- ls -l | awk ‘{sum += $5 } END {print sum}

- -l | awk ‘{print $5}’

## **압축파일 관련 명령어**

tar 묶음…

a b c ⇒ abc.tar

sudo apt update

sudo apt install tree

### **압축 방법**

1. tar로 트리기반으로 묶는다(용량 아직 안줄음)
2. gzip은 용량을 줄이는 것

### **축약 방법**

- tar cvfz [저장 할 파일명.tgz] [아카이브하고 압축할 path] : tar cvf 과 gzip dir1.tgz

- tar xvfz [압축풀고 아카이브 해제할 파일명] : tar xvf 과 gzip -d 동시 에 진행한 것 

**원래 방법**

- tar cvf [파일명.tar] [아카이브할 주소]:아카이브 묶기

- gzip [압축할 파일명.tar.gz] :압축하기

- gzip -d [압축 풀 파일명.tar.gz] : 압축품

- tar xvf [파일명.tar] : 아카이브를 품

**gzip option**

-9 : 가장 압축 많이

-5 : 보통 압축

-0 : 압축 x 그냥 묶기만한게됨