# 네이버영화용 UI실행
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 
import json # 검색결과를 json 타입으로 받음
import urllib.request # URL openAPI 검색 위해
from urllib.parse import quote
import webbrowser # 웹브라우저 열기위한 패키지

class MyApp(QWidget):
    def __init__(self):
        super(MyApp, self).__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('./windows/ui/navermovie.ui', self)
        self.setWindowIcon(QIcon('naver_icon.png'))
        
        # 시그널 연결
        self.btnSearch.clicked.connect(self.btnSearchclicked)
        self.txtSearch.returnPressed.connect(self.btnSearchclicked)
        self.tblResult.itemSelectionChanged.connect(self.tblResultSelected)
        self.show()

    def tblResultSelected(self):
        selected = self.tblResult.currentRow() # 현재 선택된 열의 인덱스
        url = self.tblResult.item(selected, 2).text()
        webbrowser.open(url)

    def btnSearchclicked(self):
        jsonResult = []
        totalResult = []
        keyword = 'news'
        serach_word = self.txtSearch.text()
        display_count = 50

        jsonResult = self.getNaverSearch(keyword, serach_word, 1, display_count)
        # print(jsonResult)

        for post in jsonResult['items']:
            totalResult.append(self.getPostData(post))
        
        self.makeTable(totalResult)

    def makeTable(self, result):
        self.tblResult.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tblResult.setColumnCount(3)
        self.tblResult.setRowCount(len(result)) # 50
        self.tblResult.setHorizontalHeaderLabels(['영화제목', '상영년도', '영화링크'])
        self.tblResult.setColumnWidth(0, 250)
        self.tblResult.setColumnWidth(1, 100)
        self.tblResult.setColumnWidth(2, 100)
        self.tblResult.setEditTriggers(QAbstractItemView.NoEditTriggers) # readonly
        #  테이블위젯 설정

        i = 0
        for item in result: # 50번 반복
            title = self.strip_tag(item[0]['title'])
            subtitle = item[0]['subtitle']
            self.tblResult.setItem(i,0,QTableWidgetItem(f'{title} / {subtitle}'))
            self.tblResult.setItem(i,1,QTableWidgetItem(item[0]['pubDate']))
            self.tblResult.setItem(i,2,QTableWidgetItem(item[0]['link']))
            i += 1

    def strip_tag(self, title):
        ret = title.replace('&lt;', '<')
        ret = ret.replace('&gt', '>')
        ret = ret.replace('&quot;', '"') 
        ret = ret.replace('<b>','')
        ret = ret.replace('</b>', '')
        return ret

    def getPostData(self, post):
        temp = []
        title = post['title']
        link = post['link']
        subtitle = post['subtitle']
        pubDate = post['pubDate']

        temp.append({'title':title, 'subtitle':subtitle,
                           'pubDate':pubDate, 'link':link})
        return temp
    
    # 핵심함수
    def getNaverSearch(self, keyword, search, start, display):
        url = f'https://openapi.naver.com/v1/search/movie' \
              f'?query={quote(search)}&start={start}&display={display}'
        print(url)
        req = urllib.request.Request(url)
        # 인증 추가
        req.add_header('X-Naver-Client-Id', 'yKRIr5k2_jKyaVg8Yr74')
        req.add_header('X-Naver-Client-Secret', 'q_caUwN1ph')

        res = urllib.request.urlopen(req) # request에 대한 response
        if res.getcode() == 200:
            print('URL request success')
        else:
            print('URL request failed')

        ret = res.read().decode('utf-8')
        if ret == None:
            return None
        else:
            return json.loads(ret)


if __name__=='__main__':
    app = QApplication(sys.argv)
    win = MyApp()
    app.exec()