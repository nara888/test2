# -*- coding: utf-8 -*-
loopFlag = 1
from LbrrySerchInfoService import *


#### Menu  implementation
def printMenu():
    print("\n전국 전문도서관 위치 검색 서비스입니다.")
    print("========Menu==========")
    print("오픈API에서 데이터 로드:  l")
    print("xml 스타일로 출력: x")
    print("모든 데이터 출력: p")
    print("데이터 검색 출력: s")
    print("프로그램 종료: q")
   # print("print fishing place list: b")
    #print("Add new fishing place: a")
    #print("sEarch Fishing Place name: e")
    #print("Make html: m")
    #print("----------------------------------------")
    #print("Get fishing place data : g")
    #print("send maIl : i")
    #print("sTart Web Service: t")
    #print("========Menu==========")
    
def launcherFunction(menu):
    if menu ==  'l':
        getDataFromOpenAPI()
    elif menu == 'q':
        QuitProgram()
    elif menu == 'x':
        PrintDOMtoXML()
    elif menu == 'p':
        PrintData()
    elif menu == 's':
        print("========Menu==========")
        print("ID로 검색:  i")
        print("주소로 검색:  a")
        print("이름으로 검색:  n")
        m = input("검색할 항목을 입력하세요: ")
        if m == 'i':
             s = input("검색할 ID: ")
        elif m == 'a':
             s = input("검색할 주소: ")
        elif m == 'n':
             s = input("검색할 도서관 이름: ")
        else:
            print("에러!! 올바른 메뉴키를 입력하세요")
        PrintSearchData(s, m)
    else:
        print("에러!! 올바른 메뉴키를 입력하세요")
        
"""
    elif menu == 'b':
        PrintBookList(["title",])
    elif menu == 'a':
        ISBN = str(input ('insert ISBN :'))
        title = str(input ('insert Title :'))
        AddBook({'ISBN':ISBN, 'title':title})
    elif menu == 'e':
        keyword = str(input ('input keyword to search :'))
        printBookList(SearchBookTitle(keyword))
    elif menu == 'g': 
        isbn = str(input ('input isbn to get :'))
        #isbn = '0596513984'
        ret = getBookDataFromISBN(isbn)
        AddBook(ret)
    elif menu == 'm':
        keyword = str(input ('input keyword code to the html  :'))
        html = MakeHtmlDoc(SearchBookTitle(keyword))
        print("-----------------------")
        print(html)
        print("-----------------------")
    elif menu == 'i':
        sendMain()
    elif menu == "t":
        startWebService()
    
"""
def QuitProgram():
    global loopFlag
    loopFlag = 0
    DocFree()
    
##### run #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("프로그램이 종료되었습니다.")
