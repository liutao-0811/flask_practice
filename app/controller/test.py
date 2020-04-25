#coding:utf-8

#接口文件
import string,random,json
from flask import jsonify,request,Response
from flask import render_template
from app import app
from werkzeug.utils import secure_filename
import os


#文件上传目录  取绝对路径
app.config['UPLOAD_FOLDER'] = r'F:\flask_practice\app\static\uploads'
#支持的文件格式
app.config['ALLOWED_EXETENSIONS'] = {'png','jpg','jpeg','gif'} #集合类型
#文件大小
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 #16MB
#文件内容

#获取某个文件的绝对路径：app.root_path,



#判断文件是否是我们的格式
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1]in app.config['ALLOWED_EXETENSIONS']



@app.route('/')
def index():
    return render_template("index.html")


#上传文件
@app.route('/upload',methods=['POST'])
def upload():
    upload_file = request.files['image']
    if upload_file and allowed_file(upload_file.filename):
        # 将文件保存到 static/uploads 目录，文件名同上传时使用的文件名
        filename = secure_filename(upload_file.filename)
        upload_file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        return 'info is '+request.form.get('info','')+'. success'
    #获取文件内容file_content = request.files['image'].stream.read()
    else:
        return 'failed'

@app.route('/list')
def hello_lo():
    return request.args.__str__()# 列出所有的url参数


@app.route('/list1')
def hello_lo1():
    #return request.args.get('info')   #列出某个指定参数
    r= request.args.get('info')
    if r == None:
        return jsonify(msg="info为空")
    else:
        #return r
        print(type(r))
        return jsonify(msg=r)


#查看post数据内容
@app.route('/register',methods=['POST'])
def register():
    print(request.headers)
    #print(request.stream.read())
    print(request.form['username'])#获取参数的值
    print(request.form.get('username'))#获取参数的值
    print(request.form.getlist('username'))#获取参数的值（参数多多值）
    print(request.form.get('nicknime',default='little apple'))
    return 'welcome'


@app.route('/hello',methods=['get'])
def hello():
    return jsonify(status=1,msg="hello world!")

#请求json时
#处理json格式的请求数据
@app.route('/add',methods=['POST'])
def add():
    print(request.headers)
    print(type(request.json))
    print(request.json)
    result = request.json['a']+request.json['b']
    return str(result)

#响应JSON时，除了要把响应体改成JSON格式，
# 响应头的Content-Type也要设置为application/json。

@app.route('/add1',methods=['POST'])
def add1():
    result = {'sum':request.json['a']+request.json['b']}
    ####方法1：：：
    #return Response(json.dumps(result), mimetype='application/json')
    # #可增加定制性  响应头,如下 ：
    # resp = Response(json.dumps(result),  mimetype='application/json')
    # resp.headers.add('Server', 'python flask')
    # return resp

    ####方法2：：：  方法2比较简单
    return jsonify(result)

@app.route('/n1/')
def hello_world():
    return 'Hello World!'
    # 等价于
    # Response('Hello World!', status=200, mimetype='text/html')




@app.route('/test/<username>')
def profile(username):
    return jsonify(who=username)

@app.route('/get_create_data',methods=['GET', 'POST'])
def get_creat_dada():
    sepcial="~!@#$%^&*()_+{}|:\"<>?\'"

    a = string.ascii_letters
    # 大写string.ascii_uppercase
    # 小写string.ascii_lowercase
    d = string.digits
    v = random.randint(0x4e00, 0x9fbf)
    randomlength =request.args.get('length')
    if randomlength == None:
        randomlength = 20
    else:
        randomlength = int(randomlength)
    random_str = 0
    num = int(request.args.get('num'))
    if num == 0:
        """
        键盘上所有特殊字符
        """
        random_str = sepcial

    elif num == 1:
        """
        随机字符串包含数字+字母+特殊符号
        """
        str_list = [random.choice(sepcial+a+d) for i in range(randomlength)]
        random_str = ''.join(str_list)

    elif num == 2:
        """
        随机字符串包含数字+字母+不包含特殊符号
        """
        str_list = [random.choice(a+d) for i in range(randomlength)]
        random_str = ''.join(str_list)

    elif num == 3:
        """
        随机字符串包含数字+字母+汉字
        """
        str_list = [random.choice(a+d) for i in range(randomlength-1)]
        random_str = ''.join(str_list)+chr(v)

    response ={
        'msg' : random_str
    }
    return jsonify(response)