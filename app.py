#!/usr/bin/env python
'''Python anaconda environment'''
# coding: utf-8

import json
import custom
from flask import Flask,render_template,request
import requests

cur=custom.createcon
app=Flask(__name__)

@app.route('/',methods=['GET'])
def first():
      '''
      Rendering the home page 

      Returns
      -------
      None

      '''
      return render_template('index.html')

@app.route('/create',methods=['POST'])
def addList():
      value=request.json.get("msg")
      custom.insertd(value)
      return "OK"

@app.route("/getAll",methods=['GET'])
def getdata():
      data=custom.fetch()
      for dat in data:
         print(dat[0])
      return "Ok"

if __name__=='__main__':
      app.run(debug=True,host="0.0.0.0",port=4000)



#custom.fetch()
#custom.tdel("COMPANY")
#custom.tcreate()
#custom.deltable("COMPANY")
#custom.insertd()
#conn.close()
