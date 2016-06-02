# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:39:22 2016

@author: Administrator
"""
import urllib
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
from http.client import HTTPConnection
from http.server import BaseHTTPRequestHandler, HTTPServer


##global
BooksDoc = None
conn = None
itemNum = 1
#regKey = 인증키
regKey = '49092c674db144d3b18029e0009d7493'
# 경기도 공공데이터 OpenAPI 접속 정보 information
server = "dev.ndsl.kr"
#server = "openapi.gg.go.kr"


def getDataFromOpenAPI():
    global server, regKey, conn, BooksDoc
    if conn == None :
        conn = HTTPConnection(server)
    url = "http://dev.ndsl.kr/openapi/service/rest/LbrrySerchInfoService/getLbrryInfoList?ServiceKey=tBrnF05c4mI6U%2FG750oYKMThYei0oJeb%2BnmcHTkN0Q8MGlF7dRMgrURjbgKo8WBVy%2FucKgNW55vmHr0CyjuaDQ%3D%3D&numOfRows=487"
    #url = "http://openapi.gg.go.kr/FishingPlaceStatus?KEY=49092c674db144d3b18029e0009d7493&xml&1&100" # API에 맞는 키값
    conn.request("GET", url)
    
    req = conn.getresponse()
    print(req.status, req.reason)
    if int(req.status) == 200 :
        global BooksDoc 
        dom = req.read().decode('utf-8')
        BooksDoc = parseString(dom)
        print("오픈 API에서 자료를 성공적으로 로드했습니다")
    else:
        print("로드를 실패했습니다")
        
def PrintDOMtoXML():
    global BooksDoc
    if checkDocument():
        print(BooksDoc.toxml())
        
def PrintData():
#def SearchPrintData():
    global BooksDoc, ItemNum
    if not checkDocument():
        return None
    
    response = BooksDoc.childNodes
    body = response[0].childNodes
    items = body[1].childNodes
    item = items[0].childNodes
    
    for i in item:
        if i.nodeName == "item":
            subitems = i.childNodes
            for atom in subitems:
               if atom.nodeName in ["libname",]:
                   print("도서관 이름 :",atom.firstChild.nodeValue)
               if atom.nodeName in ["libid",]:
                   print("ID :",atom.firstChild.nodeValue)
               if atom.nodeName in ["address1",]:
                   print("주소 :",atom.firstChild.nodeValue)
               if atom.nodeName in ["address2",]:
                   print("상세 주소 :",atom.firstChild.nodeValue)
                       
def PrintSearchData(keyword, menu):
    global BooksDoc
    if not checkDocument():
        return None
    
    try:
        tree = ElementTree.fromstring(str(BooksDoc.toxml()))
    except Exception:
        print ("Element Tree parsing Error : maybe the xml document is not corrected.")
        return None
    
    #get Book Element
    itemElements = tree.getiterator("item")  # return list type
    for i in itemElements:
         if(menu == 'n'):
            if (i.find("libname").text.find(keyword) >=0 ):
                print("도서관 이름 :",i.find("libname").text, "/ ID :",i.find("libid").text, "/ 주소 :", i.find("address1").text, i.find("address2").text)
         if(menu == 'i'):
            if (i.find("libid").text.find(keyword) >=0 ):
                print("도서관 이름 :",i.find("libname").text, "/ ID :",i.find("libid").text, "/ 주소 :", i.find("address1").text, i.find("address2").text)
         if(menu == 'a'):
            if (i.find("address1").text.find(keyword) >=0):
                print("도서관 이름 :",i.find("libname").text, "/ ID :",i.find("libid").text, "/ 주소 :", i.find("address1").text, i.find("address2").text)
                    
def DocFree():
    if checkDocument():
        BooksDoc.unlink()
        
        
def checkDocument():
    global BooksDoc
    if BooksDoc == None:
        print("에러!! 로드된 데이터가 없습니다")
        return False
    return True