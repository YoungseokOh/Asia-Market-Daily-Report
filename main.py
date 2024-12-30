from data_processing import fetch_japan_headlines, save_as_json, save_as_csv
from utils import setup_logger, read_file, logging
import os

# 경로 설정
HTML_FILE = "data/html_samples/yahoo_finance_sample.html"
OUTPUT_JSON = "data/output/japan_headlines.json"
OUTPUT_CSV = "data/output/japan_headlines.csv"
LOG_FILE = "data/logs/app.log"

if __name__ == "__main__":
    # 로깅 설정
    setup_logger(LOG_FILE)

    try:
        # HTML 파일 읽기
        html_content = read_file(HTML_FILE)
        logging.info("HTML 파일 읽기 성공.")

        # 뉴스 헤드라인 크롤링
        headlines = fetch_japan_headlines(html_content)
        logging.info(f"{len(headlines)}개의 뉴스 헤드라인을 가져왔습니다.")

        # 결과 저장
        save_as_json(headlines, OUTPUT_JSON)
        save_as_csv(headlines, OUTPUT_CSV)
        logging.info("결과를 JSON 및 CSV 파일로 저장했습니다.")

        print("작업이 완료되었습니다. 결과를 확인하세요.")

    except Exception as e:
        logging.error(f"오류 발생: {e}")
        print("오류가 발생했습니다. 로그 파일을 확인하세요.")
