#coding:utf-8

from flask import Flask
app = Flask(__name__)

from app.controller import test

#在这里声明了app对象，同时指明在test。py中引用了app