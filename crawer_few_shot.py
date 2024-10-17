import json
import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver

# 크롤링 할 URL
# URL = 'https://www.yanolja.com/reviews/domestic/1000102261?sort=HOST_CHOICE'

def crawl_yanolja_reviews(name, url):
    review_list=[]
    driver = webdriver.Chrome()
    driver.get(url)
    # driver.get(URL)

    # 페이지 로드 대기
    time.sleep(3)

    # 페이지 스크롤
    scroll_count = 20
    for i in range(scroll_count):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(2)
    
    # 파싱
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    review_containers = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div')
    review_date = soup.select('#__next > section > div > div.css-1js0bc8 > div > div > div > div.css-1toaz2b > div > div.css-1ivchjf > p')

    for i in range(len(review_containers)):
        review_text = review_containers[i].find('p',class_='content-text').text
        # 별점정보가 이미지기 때문에 색칠해저 있는 갯수로 확인
        review_stars = review_containers[i].find_all('path', {'fill': '#FDBD00'})
        star_cnt = len(review_stars)
        date = review_date[i].text

        review_dict = {
            'review' : review_text,
            'stars' : star_cnt,
            'date': date
        }

        review_list.append(review_dict)

# 윈도우는 인코딩 필요
    # with open('./res/reviews.json', 'w') as f:
    # with open('./res/reviews.json', 'w', encoding='utf-8') as f:
    with open(f'./res/{name}.json', 'w', encoding='utf-8') as f:
        json.dump(review_list, f, indent=4, ensure_ascii=False)

if __name__=='__main__':
    # sys.argv[0]은 파일 이름 들어감
    name, url = sys.argv[1], sys.argv[2]
    crawl_yanolja_reviews(name=name, url=url)