import pandas as pd
import sys
from selenium import webdriver as wd
import time
from bs4 import BeautifulSoup
import random


def term_make(x, y): return random.randint(x, y)*0.1  # 0.1 ~ 0.9


driver = wd.Chrome(
    'C://Users//USER//Desktop//Py_Projects//selenium_level4//chromedriver.exe')
#driver = wd.Chrome('.//chromedriver.exe')

# 모든 지점의 정보를 담는 그릇
starbucks_store_infos = list()

for sido_idx in range(1, 17+1):
    # 초기 진입 사이트 접속
    driver.get('https://www.starbucks.co.kr/store/store_map.do?disp=locale')
    time.sleep(1*10 + term_make(1, 5))

    # 시도 선택
    css_sel = f'div.loca_step1_cont > ul > li:nth-child({sido_idx}) > a'
    si_do_a_tag = driver.find_element_by_css_selector(css_sel)
    si_do_a_tag.click()
    time.sleep(1*10 + term_make(1, 5))

    if sido_idx<17:# 세종시 이전까지만 전체 클릭
        # 전체 선택, 1번 맴버가 무조건 전체이다 -> 고정
        css_sel = '#mCSB_2_container > ul > li:nth-child(1) > a'
        driver.find_element_by_css_selector(css_sel).click()
        # 로딩 속도에 따라 반응이 다르게 온다 => 보수적으로 10초 결정
        time.sleep(1*10 + term_make(1, 5))

    # soup(DOM Tree) 생성
    src = driver.page_source  # 현재 페이지의 HTML 소스
    soup = BeautifulSoup(src, 'html5lib')
    # 정보추출
    starbucks_store_local_infos = [{
        'name': li.get('data-name'),  # 지점명, 속성값 추출 => 요소.get('속성이름')
        'lat': float(li.get('data-lat')),   # 위도 -> float()
        'long': float(li.get('data-long')),   # 경도 -> float()
        'code': li.get('data-code'),  # 지점코드
        'storecd': li.get('data-storecd'),                 # 관리코드(?)
        'addr': li.p.text.strip()[:len('1522-3232')*-1],   # 전화번호가 모두 동일하다
        # class는 속성값으로 뽑으면 리스트로 나온다(특징), pin_ 제거
        'spec': li.i.get('class')[0][len('pin_'):]
    } for li in soup.select('.quickSearchResultBoxSidoGugun > li')]

    # starbucks_store_infos에 starbucks_store_local_infos값 하나하나를 맴버로 추가한다
    starbucks_store_infos.extend(starbucks_store_local_infos)

    # 샘플 1개만 작동잘되는지 체크
    # if sido_idx == 1:
    #     print( len(starbucks_store_infos) )
    #     break

# 브라우저 닫기
driver.close()
driver.quit()

# csv에 저장
# [{},{},..] => DataFrame => csv 저장
# df 생성
df = pd.DataFrame.from_dict(starbucks_store_infos)
#df.to_csv('starbucks_store.csv', index=False)
df.to_excel('starbucks_store_full.xlsx', index=False)

# 파이썬 파일에서 사용
sys.exit(0)
