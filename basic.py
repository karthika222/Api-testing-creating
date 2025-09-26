'''
Install Flask: pip install flask

Create your API: Write a simple Flask app in a file app.py.

Run the Flask app: Run python app.py in your terminal.

Test with Postman: Use Postman to send a GET request to http://127.0.0.1:5000/api/message.''''
from flask import Flask
app= Flask(__name__)

@app.route('/api/message',methods=['GET'])
def getmssg():
    return {'message': 'Hello This is simple api'}

if __name__=='__main__':
    app.run(debug=True)
