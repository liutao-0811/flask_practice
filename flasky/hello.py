from flask import Flask,request,render_template

#初始化
app = Flask(__name__)

#静态路由和
@app.route('/')
def index():  #视图函数
    #return '<h1>hello world 你好</h1>',400
    return render_template('index.html')#引入模板 默认读取flask下的目录templates中的对应文件
"""
<p>从字典中获取一个值： {{ mydict['key'] }}.</p>
<p>从列表中获取一个值： {{ mylist[3] }}.</p>
<p>通过一个变量索引，从列表中获取一个值： {{ mylist[myintvar] }}.</p>
<p>从对象的方法中获取一个值： {{ myobj.somemethod() }}.</p>
"""


#动态路由
@app.route('/user/<name>')
def user(name):
    #return '<h1>hello,{}!</h1>'.format(name)
    return render_template('user.html',name=name)


if __name__ == '__main__':
    app.run()
    #app.run(debug=True)  #调试
