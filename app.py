from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # 개발자 1이 추가한 코드:
    user_name = "Developer 1"
    return f'<h1>Hello Team! Ready for CI/CD!</h1><p>Welcome, {user_name}! modified by feature/login</p>'

# Render.com에서 실행할 때 필요한 코드 (필수는 아님)
if __name__ == '__main__':
    app.run(debug=True)

