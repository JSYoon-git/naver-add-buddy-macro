import subprocess
import os
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import chromedriver_autoinstaller

from bs4 import BeautifulSoup

from pyfiglet import Figlet


class NAVER_ADD_BUDDY:
    def __init__(self):
        NAVER_URL = 'https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0'
        # chrome debug 폴더 생성
        try:
            os.mkdir('debug')
        except:
            print("[INFO] debug folder already exists")
        # chrome debug mode 실행
        try:
            subprocess.Popen('C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="%s"'%(os.getcwd()+"\debug"))  # 디버거 크롬 구동
        except:
            subprocess.Popen('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="%s"'%(os.getcwd()+"\debug"))  # 디버거 크롬 구동
        # init selenium 
        try:
            chromedriver_autoinstaller.install()
            co = Options()
            co.add_experimental_option('debuggerAddress', '127.0.0.1:9222', )
            #co.add_experimental_option('detach', True)

            self.driver = webdriver.Chrome(options=co)
            self.driver.get(NAVER_URL) 
            self.driver.implicitly_wait(10)
        except:
            print("ERR0")
        
    #def __del__(self):
    #    self.driver.quit()
        
    def login(self, ID, PW):
        try:
            # [BTN] 로그인 창
            self.driver.find_element(By.XPATH, '//*[@id="container"]/div/aside/div/div[1]/div[1]/div/a').click() 
            self.driver.implicitly_wait(10)
            # [INPUT] ID
            pyperclip.copy(ID) 
            self.driver.find_element(By.XPATH, '//*[@id="id"]').send_keys(Keys.CONTROL + 'v')
            self.driver.implicitly_wait(10)
            # [INPUT] PW
            pyperclip.copy(PW) 
            self.driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys(Keys.CONTROL + 'v')
            self.driver.implicitly_wait(10)
            # [BTN] 로그인
            self.driver.find_element(By.XPATH, '//*[@id="log.login"]').click() 
            self.driver.implicitly_wait(10)

        except:
            print("ERR1")
            

    def get_blogs_url(self, keyword="블로그", page_cnt=1):
        blog_url_list = []
        distinct_blog_url = []
        mobile_blog_url_list = []

        # [INPUT] 검색창
        try:
            pyperclip.copy(keyword) 
            self.driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/div[2]/form/fieldset/div/input').send_keys(Keys.CONTROL + 'v')
            self.driver.implicitly_wait(10)
            # [BTN] 검색
            self.driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/div[2]/form/fieldset/a[1]/i').click() 
            self.driver.implicitly_wait(10)
            # [CHECK] 최신순
            self.driver.find_element(By.XPATH, '//*[@id="content"]/section/div[1]/div[2]/div/span/a[2]/span/i').click() 
            self.driver.implicitly_wait(10)
        except:
            print("ERR2-1")
            return None, None, None
        try:
            for _ in range(int(page_cnt)):
                for page in range(2, 12, 1):
                    # beautifulsoup
                    time.sleep(0.25)
                    req = self.driver.page_source 
                    self.driver.implicitly_wait(10)

                    soup = BeautifulSoup(req, 'html.parser')
                    blogs_latest = soup.find_all('div', {"class":"info_post"})
                    # 링크
                    for blog in blogs_latest:
                        blog_url = blog.find('a')['href']
                        blog_url_list.append(blog_url)
                    # [BTN] 다음 페이지
                    if page != 11:
                        self.driver.find_element(By.XPATH, '//*[@id="content"]/section/div[3]/span[%d]/a'%page).click()       
                # [BTN]페이지 넘어가기
                self.driver.find_element(By.XPATH, '//*[@id="content"]/section/div[3]/a').click() 
                self.driver.implicitly_wait(10)
        except:
            print("ERR2-2")
            return None, None, None
        try:
            # 중복 제거
            for blog_url in blog_url_list:
                distinct_blog_url.append('/'.join(blog_url.split('/')[0:-1]))
            distinct_blog_url = set(distinct_blog_url)

            # mobile 링크로 변환
            for blog_url in distinct_blog_url:
                mobile_blog_url_list.append(blog_url.replace('blog', 'm.blog'))
            return len(blog_url_list), len(mobile_blog_url_list), mobile_blog_url_list
        except:
            print("ERR2-3")
            return None, None, None
                
        
    def add_buddy(self, mobile_url, content, group_idx, cnt):
        try:
            self.driver.get(mobile_url)
            time.sleep(0.25)
            req = self.driver.page_source 
            self.driver.implicitly_wait(5)
            soup = BeautifulSoup(req, 'html.parser')
            buddy_cnt = int(soup.find('span', {"class":"buddy___ckI_"}).text.replace(',','')[:-5])
            if buddy_cnt >= 100:
                # [BTN] 이웃 추가
                self.driver.find_element(By.XPATH, '//*[@id="root"]/div[4]/div/div[3]/div[1]/button').click() 
                self.driver.implicitly_wait(5)
                # [CHECK] 서로이웃을 신청합니다.
                self.driver.find_element(By.XPATH, '//*[@id="bothBuddyRadio"]').click() 
                self.driver.implicitly_wait(5)
                # [CHECK] 그룹 변경합니다.
                select = Select(self.driver.find_element(By.XPATH, '//*[@id="buddyGroupSelect"]'))
                self.driver.implicitly_wait(5)

                select.select_by_index(group_idx)
                self.driver.implicitly_wait(5)

                # [INPUT] 서로이웃 신청 내용
                self.driver.find_element(By.XPATH, '//*[@id="buddyAddForm"]/fieldset/div/div[2]/div[3]/div/textarea').clear()
                self.driver.find_element(By.XPATH, '//*[@id="buddyAddForm"]/fieldset/div/div[2]/div[3]/div/textarea').send_keys(content)
                self.driver.implicitly_wait(5)
                # [BTN] 확인
                self.driver.find_element(By.XPATH, '/html/body/ui-view/div[2]/a[2]').click()
                self.driver.implicitly_wait(5)
            #print("[INFO] 서로 이웃 추가 %d 성공!"%cnt)
            state = "[log] %d번 째 이웃 신청 성공"%cnt
        except: 
            state = "[log] 이미 서이추 상태, 혹은 금지 상태"
        
            
        return state

            
if __name__ == "__main__":
    naver_macro = NAVER_ADD_BUDDY()
    naver_macro.login(ID="jungsun1996", PW="go22132213!")
    a, b, list_d = naver_macro.get_blogs_url(keyword="파트너스", page_cnt=1)
    cnt = naver_macro.add_buddy(url_list= list_d, content="서이추해요", max_buddy=100, wanted_buddy=2)
    print(cnt)