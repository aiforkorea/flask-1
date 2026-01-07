import pytest
from app import app as flask_app

# Flask 앱이 제대로 작동하는지 확인하는 테스트 함수
def test_hello_world_status_code():
    with flask_app.test_client() as client:
        response = client.get('/')
        # 접속에 성공했는지 (상태코드 200) 확인
        assert response.status_code == 200

def test_hello_world_content():
    with flask_app.test_client() as client:
        response = client.get('/')
        # 웹사이트 내용에 'Hello Team'이라는 글자가 있는지 확인
        assert b'Hello Team' in response.data
