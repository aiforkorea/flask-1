from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # 개발자 1, 2가 기능을 추가할 공간입니다.
    return '<h1>Hello Team! Ready for CI/CD! try to login</h1>'

# Render.com에서 실행할 때 필요한 코드 (필수는 아님)
if __name__ == '__main__':
    app.run(debug=True)
