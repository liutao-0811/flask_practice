# -*- coding: utf-8 -*-

#启动文件
from app import app

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080,debug=True)


