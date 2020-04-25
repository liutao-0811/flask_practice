from flask import Flask,request,current_app

#初始化
app = Flask(__name__)

#应用程序上下文(application context)和请求上下文(request context)
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is:{}</p>',format(user_agent)

if __name__ == '__main__':
    app.run()
    #app.run(debug=True)  #调试
