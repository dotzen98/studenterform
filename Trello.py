import trello
import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
   if request.method == 'POST':

      title = request.form['name']
      contact = request.form['email']
      customer = request.form['customer']
      tool = request.form['tool']
      time = request.form['time']
      comment = request.form['comment']
      priority = request.form['priority']
      place = request.form['place']
      dueDate = request.form['dueDate']


      url = "https://api.trello.com/1/cards"

      headers = {
      "Accept": "application/json"
      }

      query = {
      'name':  title,
      'desc':  "Kontakt: " + contact +
               "\nKunde: " + customer +
               "\nIT-værktøj: " + tool +
               "\nformodede timer: " + time +
               "\n\n" + comment,
      'idLabels': [priority],
      'idList': place,
      'due': dueDate,
      'key': '1a103f112c5701f3209d9ff096bbdcab',
      'token': 'f5975e8f00403d42c05378edec1b909fe2f3f64d65c9926b7ede0e850793be1f'
      }

      response = requests.request(
         "POST",
         url,
         headers=headers,
         params=query
         )


      #print(
      json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))
         #)

      return render_template('hali.html')
   else:
      return render_template('hali.html')

if __name__ == '__main__':
   app.run()





