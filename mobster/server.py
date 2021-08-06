from flask import Flask, render_template, url_for, request
import csv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('form1.html')

# @app.route('/form1.html')
# def temp():
#     return render_template('form1.html')

# @app.route('/form2.html')
# def form2():
#     return render_template('form2.html')

# @app.route('/form3.html')
# def form3():
#     return render_template('form3.html')

@app.route('/<page_name>')
def auto_html_page(page_name):
    return render_template(page_name)


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
