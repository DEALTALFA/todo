#!/usr/bin/env python
# coding: utf-8
import json
from flask import Flask,render_template
import custom

app=Flask(__name__)

# conn,cur=custom.createcon()
@app.route('/',methods=['GET'])
def first():
      return render_template('index.html')

if __name__=='__main__':
      app.run(debug=True,host="0.0.0.0",port=4000,)





# custom.fetch()
# custom.tdel("COMPANY")
# custom.tcreate()
#custom.deltable("COMPANY")
# custom.insertd()
conn.close()   


