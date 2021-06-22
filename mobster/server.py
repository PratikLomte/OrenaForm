from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/temp.html')
def temp():
    return render_template('temp.html')

@app.route('/try.html')
def try1():
    return render_template('try.html')

@app.route('/try.html')
def try2():
    return render_template('try.html')

@app.route('/new.html')
def new():
    return render_template('new.html')

def write_to_file(data):
    with open('database1.txt', mode = 'a') as database:
        name = data['name']
        email = data['email']
        college = data['college']
        phone = data['phone']
        event = data['event']
        orgdetails = data['orgdetails']
        comments = data['comments']

        file = database.write(f'\n\n{name}, {email}, {college}, {phone}, {event}, {orgdetails}, {comments} \n')

def write_to_csv(data):
    with open('database2.csv', mode = 'a') as database2:
        name = data['name']
        email = data['email']
        college = data['college']
        phone = data['phone']
        event = data['event']
        orgdetails = data['orgdetails']
        comments = data['comments']

        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,college,phone,event,orgdetails,comments])

@app.route('/ty.html', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        write_to_csv(data)
        return render_template('ty.html')
    else:
        return "Error 404"

@app.route('/ty1.html')
def submit1():
        return render_template('ty.html')




