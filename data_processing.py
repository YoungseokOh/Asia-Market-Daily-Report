import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def fetch_japan_headlines(html_content, max_items=15):
    """
    일본 야후 파이낸스에서 헤드라인을 크롤링하는 함수.
    
    Args:
        html_content (str): HTML 콘텐츠.
        max_items (int): 최대 가져올 뉴스 항목 수.
    
    Returns:
        list: 뉴스 제목과 링크의 리스트.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    news_list = soup.select('ul.container__2U3C li a')
    headlines = []

    for item in news_list[:max_items]:
        title_tag = item.select_one('span.title__36K6')
        if title_tag:
            title = title_tag.text.strip()
            link = item['href']
            headlines.append({'title': title, 'link': link})
    
    return headlines

def clean_text(text):
    """
    텍스트 정리 함수.
    """
    return text.strip()

def convert_to_dataframe(data):
    """
    데이터를 DataFrame으로 변환.
    """
    return pd.DataFrame(data)

def save_as_json(data, file_path):
    """
    데이터를 JSON 파일로 저장.
    """
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_as_csv(data, file_path):
    """
    데이터를 CSV 파일로 저장.
    """
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding='utf-8-sig')