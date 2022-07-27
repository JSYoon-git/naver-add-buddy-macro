import subprocess
import os
import time
import pyperclip
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller

from bs4 import BeautifulSoup
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from threading import Thread
from datetime import datetime
from delay_function import delay_function


def dialog(a, b, c):
    mbox = QtWidgets.QMessageBox()
    mbox.setWindowTitle("Yoon Company")
    mbox.setText("전체 포스팅 : %d개 \n매크로 블로그 : %d개 제거\n신청 블로그 : %d개 성공" % (a, b, c))

    mbox.setStandardButtons(QtWidgets.QMessageBox.Ok)

    mbox.exec_()


def dialog1():
    mbox = QtWidgets.QMessageBox()
    mbox.setWindowTitle("Yoon Company")
    mbox.setText("실패")
    mbox.setStandardButtons(QtWidgets.QMessageBox.Ok)

    mbox.exec_()


class LOGIN_THREAD(Thread):
    def __init__(self, driver, ID, PW):
        super().__init__()
        self.driver = driver
        self.ID = ID
        self.PW = PW

    def run(self):
        # [BTN] 로그인 창
        self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/aside/div/div[1]/div[1]/div/a'
        ).click()
        self.driver.implicitly_wait(10)
        delay_function(1)

        # [INPUT] ID
        pyperclip.copy(self.ID)
        self.driver.find_element(By.XPATH, '//*[@id="id"]').send_keys(
            Keys.CONTROL + "v"
        )
        self.driver.implicitly_wait(10)
        delay_function(1)

        # [INPUT] PW
        pyperclip.copy(self.PW)
        self.driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys(
            Keys.CONTROL + "v"
        )
        self.driver.implicitly_wait(10)
        delay_function(1)

        # [BTN] 로그인
        self.driver.find_element(By.XPATH, '//*[@id="log.login"]').click()
        self.driver.implicitly_wait(10)


class CRAWLING_THREAD(Thread):
    def __init__(self, driver, keyword, page, list_form):
        super().__init__()
        self.driver = driver
        self.keyword = keyword
        self.page = page
        self.list_form = list_form

        self.mobile_blog_url_list = []

    def run(self):
        blog_url_list = []
        distinct_blog_url = []

        # [INPUT] 검색창
        try:
            pyperclip.copy(self.keyword)
            self.driver.find_element(
                By.XPATH, '//*[@id="header"]/div[1]/div/div[2]/form/fieldset/div/input'
            ).send_keys(Keys.CONTROL + "v")
            self.driver.implicitly_wait(10)
            delay_function(1)
            # [BTN] 검색
            self.driver.find_element(
                By.XPATH, '//*[@id="header"]/div[1]/div/div[2]/form/fieldset/a[1]/i'
            ).click()
            self.driver.implicitly_wait(10)
            delay_function(1)
            # [CHECK] 최신순
            self.driver.find_element(
                By.XPATH,
                '//*[@id="content"]/section/div[1]/div[2]/div/span/a[2]/span/i',
            ).click()
            self.driver.implicitly_wait(10)
            delay_function(1)
        except:
            print("[ERROR] search")
            sys.exit()
        try:
            for _ in range(int(self.page)):
                for page in range(2, 12, 1):
                    # BS4
                    time.sleep(0.25)
                    req = self.driver.page_source
                    self.driver.implicitly_wait(10)
                    soup = BeautifulSoup(req, "html.parser")
                    blogs_latest = soup.find_all("div", {"class": "info_post"})
                    # 링크
                    for blog in blogs_latest:
                        blog_url = blog.find("a")["href"]
                        blog_url_list.append(blog_url)

                    # [BTN] 다음 페이지
                    if page != 11:
                        self.driver.find_element(
                            By.XPATH,
                            '//*[@id="content"]/section/div[3]/span[%d]/a' % page,
                        ).click()
                # 매크로 검출기 1
                day = self.driver.find_element(
                    By.XPATH,
                    '//*[@id="content"]/section/div[2]/div[1]/div/div[1]/div[2]/span[2]',
                ).text

                # [BTN]페이지 넘어가기
                self.driver.find_element(
                    By.XPATH, '//*[@id="content"]/section/div[3]/a'
                ).click()
                self.driver.implicitly_wait(10)
                delay_function(1)
        except:
            print("[ERROR] crawling")
            sys.exit()
        try:
            if "분" in day:
                diff = 1
            elif "시간" in day:
                diff = 1
            else:
                time1 = datetime(
                    int(day.split(".")[0]),
                    int(day.split(".")[1]),
                    int(day.split(".")[2]),
                )
                time2 = datetime.now()
                diff = (time2 - time1).days
            blog_url_list = set(blog_url_list)
            # 중복 제거
            for blog_url in blog_url_list:
                distinct_blog_url.append("/".join(blog_url.split("/")[0:-1]))
            # distinct_blog_url = set(distinct_blog_url)

            # 매크로 검출기
            b_count = {}  # 각 원소의 등장 횟수를 카운팅할 딕셔너리
            for i in distinct_blog_url:
                try:  # 이미 등장한 값의 경우
                    b_count[i] += 1
                except:  # 처음 등장한 값의 경우
                    b_count[i] = 1
            new_not_macro = []
            new_macro = []

            for k, v in b_count.items():
                if v * 0.75 > diff:  # n회 이상 등장한 원소로도 변경 가능
                    new_macro.append(k)
                else:
                    new_not_macro.append(k)
            # mobile 링크로 변환
            for blog_url in new_not_macro:
                self.mobile_blog_url_list.append(blog_url.replace("blog", "m.blog"))
                self.list_form.addItem(blog_url)
            dialog(len(blog_url_list), len(new_macro), len(new_not_macro))
        except:
            dialog1()


class BUDDY_THREAD(Thread):
    def __init__(
        self, driver, mobile_url, content, group_idx, wanted_buddy, form, status
    ):
        super().__init__()
        self.driver = driver
        self.mobile_url = mobile_url
        self.content = content
        self.group_idx = group_idx
        self.cnt = 1
        self.wanted_buddy = wanted_buddy
        self.form = form
        self.status = status

    def run(self):
        for url in self.mobile_url:
            if self.status == False:
                self.form.addItem("[시스템] 중단")
                break
            if self.cnt - 1 == self.wanted_buddy:
                break
            try:
                # BS4
                self.driver.get(url)
                time.sleep(0.25)
                req = self.driver.page_source
                self.driver.implicitly_wait(5)
                soup = BeautifulSoup(req, "html.parser")
                # 사업자 정보 체크
                try:
                    soup.find("span", {"class": "business_info__LW3yD"}).text
                    self.form.addItem("[시스템] 저품질 블로그 미신청 [사유1]")
                except:
                    buddy_cnt = int(
                        soup.find("span", {"class": "buddy___ckI_"}).text.replace(
                            ",", ""
                        )[:-5]
                    )
                    if buddy_cnt >= 25:
                        # [BTN] 이웃 추가
                        self.driver.find_element(
                            By.XPATH, '//*[@id="root"]/div[4]/div/div[3]/div[1]/button'
                        ).click()
                        self.driver.implicitly_wait(5)
                        # 하루인원초과
                        """
                        try:
                            ban = self.driver.find_element(By.XPATH, '//*[@id="root"]/div[8]/div/div/div/div[2]/button').text    
                            self.driver.implicitly_wait(5)
                        except:
                            pass
                        try:
                            print(self.driver.find_element(By.XPATH, '//*[@id="root"]/div[8]/div/div/div/div[2]/button').text )
                        except:
                            pass
                        if ban == '닫기':
                            self.form.addItem("[시스템] 오늘 하루 신청 인원 초과")
                            break
                        """
                        # [CHECK] 서로이웃을 신청합니다.
                        self.driver.find_element(
                            By.XPATH, '//*[@id="bothBuddyRadio"]'
                        ).click()
                        self.driver.implicitly_wait(5)
                        delay_function(5)
                        # [CHECK] 그룹 변경합니다.
                        try:
                            select = Select(
                                self.driver.find_element(
                                    By.XPATH, '//*[@id="buddyGroupSelect"]'
                                )
                            )
                            self.driver.implicitly_wait(5)
                            delay_function(5)
                            select.select_by_index(self.group_idx)
                            self.driver.implicitly_wait(5)
                            delay_function(5)
                        except:
                            self.form.addItem("[시스템] 그룹 없음")
                            self.status = False
                        # [INPUT] 서로이웃 신청 내용
                        if self.status == True:
                            self.driver.find_element(
                                By.XPATH,
                                '//*[@id="buddyAddForm"]/fieldset/div/div[2]/div[3]/div/textarea',
                            ).clear()
                            self.driver.implicitly_wait(5)
                            delay_function(3)
                            self.driver.find_element(
                                By.XPATH,
                                '//*[@id="buddyAddForm"]/fieldset/div/div[2]/div[3]/div/textarea',
                            ).send_keys(self.content)
                            self.driver.implicitly_wait(5)
                            delay_function(3)

                            # [BTN] 확인
                            self.driver.find_element(
                                By.XPATH, "/html/body/ui-view/div[2]/a[2]"
                            ).click()
                            self.driver.implicitly_wait(5)
                            delay_function(3)
                            state = "[시스템] %d번 째 이웃 신청 성공" % self.cnt
                            self.form.addItem(state)
                    else:
                        state = "[시스템] 저품질 블로그 미신청 [사유2]"
                        self.form.addItem(state)
            except:
                state = "[시스템] 이미 서이추, 신청, 혹은 금지 상태"
                self.form.addItem(state)

            if "성공" in state:
                self.cnt = self.cnt + 1
        self.form.addItem("[시스템] 끝")


def init_driver():
    NAVER_URL = "https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0"
    # chrome debug 폴더 생성
    # try:
    #    os.mkdir('debug')
    # except:
    #    print("[INFO] debug folder already exists")
    # chrome debug mode 실행
    try:
        # subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="%s"'%(os.getcwd()+"\debug"))  # 디버거 크롬 구동
        subprocess.Popen(
            'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"'
        )  # 디버거 크롬 구동
        "C:\chrometemp1"
    except:
        # subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="%s"'%(os.getcwd()+"\debug"))  # 디버거 크롬 구동
        subprocess.Popen(
            'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeDebug"'
        )
    # init selenium
    try:
        chromedriver_autoinstaller.install()
        co = Options()
        co.add_experimental_option(
            "debuggerAddress",
            "127.0.0.1:9222",
        )

        driver = webdriver.Chrome(options=co)
        driver.get(NAVER_URL)
        driver.implicitly_wait(10)
    except:
        print("[ERR] init_selenium")
        sys.exit()

    return driver


if __name__ == "__main__":
    print("test")
