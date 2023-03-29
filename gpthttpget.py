# -*- coding: UTF-8 -*-
# !/usr/bin/python
 
from flask import Flask, request, jsonify
from revChatGPT.V3  import Chatbot
chatbot = Chatbot(api_key="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")
# chatbot = Chatbot(api_key="<api_key>")

 
app = Flask(__name__)
 
 
@app.route('/ask', methods=["GET"])
def calculate():
    if request.method == 'GET':
        params = request.args

    msg = params.get("msg", "")

    result = ""
    for data in chatbot.ask(msg):
        result = result + data

    res = {"result": result}
    return jsonify(content_type='application/json;charset=utf-8',
                   reason='success',
                   charset='utf-8',
                   status='200',
                   content={"result": res})
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',
            threaded=True,
            debug=False,
            port=8868)