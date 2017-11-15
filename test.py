#!flask/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置数据库驱动
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/nowstgram'  # 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 设置这一项是每次请求结束后都会自动提交数据库中的变动
db = SQLAlchemy(app)  # 实例化


# 定义表名
class Member(db.Model):
    __tablename__ = 'member'  # 定义表名
    Id = db.Column(db.Integer, primary_key=True)  # 定义列对象
    name = db.Column(db.String(64))
    nickname = db.Column(db.String(64))
    rest_time = db.Column(db.Integer)
    integral = db.Column(db.Integer)


# 执行插入操作
user = Member(name='Yanke', nickname='Tom', rest_time=12, integral=100)
db.session.add_all([user])  # 准备把对象写入数据库之前，先要将其添加到会话中
db.session.commit()  # 提交会话到数据库
