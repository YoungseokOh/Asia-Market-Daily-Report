import logging
import os

def setup_logger(log_file_path):
    """
    로깅 설정 함수.
    """
    logging.basicConfig(
        filename=log_file_path,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

def read_file(file_path, encoding='utf-8'):
    """
    파일 읽기 함수.
    """
    with open(file_path, 'r', encoding=encoding) as f:
        return f.read()

def write_file(file_path, content, encoding='utf-8'):
    """
    파일 쓰기 함수.
    """
    with open(file_path, 'w', encoding=encoding) as f:
        f.write(content)
