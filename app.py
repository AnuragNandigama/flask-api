from flask import Flask

app = Flask(__name__)


student_json = {
    "name": "Anurag", 
    "email": "anurag.nandigama@montrealcollege.ca", 
    "language": ["English", "Telugu"],
    "country" : "Canada",
    "City": "Montreal"
}

student_dict = {
    'name': 'Anurag', 
    'address': 'Montreal'
    }

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World CST!"

@app.route('/contact', methods=['GET'])
def get_contact():
    return "montrealcollege.ca"

@app.route('/employees/<string:name>')
def user_called(name):
    return "This call has been made by " + name


@app.route('/student/')
def get_student():
    return student_dict

if __name__ == '__main__':
    app.run()