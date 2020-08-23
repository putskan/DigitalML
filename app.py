import argparse
import os
import random
import json
import helper_functions
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)
    
SMTP_SERVER = "smtp.gmail.com"
SENDER_EMAIL = "mule9006@gmail.com"
RECIEVER_EMAIL = "mule9003@gmail.com"
EMAIL_PORT = 587
WORKING_DIR = os.path.dirname(os.path.realpath(__file__))
SENDER_PASSWORD_PATH = os.path.join(WORKING_DIR, "email_pass")
DIGENERATOR_IMAGES_FOLDER = os.path.join(WORKING_DIR, 'static/img/digenerator-buzzphotos/')


@app.route('/')
@app.route('/index.html')
def index():
    """
    serve webpage
    """
    return render_template('index.html')


@app.route('/team.html')
def team():
    """
    serve webpage
    """
    return render_template('team.html')


@app.route('/products.html')
def products():
    """
    serve webpage
    """
    return render_template('products.html')


@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    """
    serve webpage
    """
    return render_template('contact.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    """
    send Contact Us form results to RECIEVER_EMAIL
    """
    # build mail content
    client_email = request.form.get('email')
    client_interest = request.form.get('interest')
    client_subject = request.form.get('subject')
    client_message = request.form.get('message')
    email_content = helper_functions.build_email_content(client_subject, client_email, client_interest, client_message)
    # send mail
    helper_functions.send_email(EMAIL_PORT, SMTP_SERVER, SENDER_EMAIL, RECIEVER_EMAIL, sender_password, email_content)
    return ""


@app.route('/digenerator.html')
def digenerator():
    """
    serve digenerator
    """
    return render_template('digenerator.html')


@app.route('/digenerate_backend_query')
def digenerate_backend_query():
    """
    pick random pic, title and description and send back to frontend
    """
    name = helper_functions.digenerate_product_name()
    description = helper_functions.digenerate_product_description()
    images_files = [f for f in os.listdir(DIGENERATOR_IMAGES_FOLDER) if os.path.isfile(os.path.join(DIGENERATOR_IMAGES_FOLDER, f))]
    image_filename = random.choice(images_files)
    image_path_for_js = r'.\static' + os.path.join(DIGENERATOR_IMAGES_FOLDER, image_filename).split('static')[1]
    digenerate_result = { 
        'image_path': image_path_for_js,
        'name': name,
        'description': description
    }
    return json.dumps(digenerate_result)


def get_email_password():
    """
    get sender_password, preferably from user, if not, from local file.
    if both do not exist - ask user for password
    """
    sender_password = ""
    if os.path.isfile(SENDER_PASSWORD_PATH):
        with open(SENDER_PASSWORD_PATH, 'r') as f:
            sender_password = f.read()
            
    # don't apply logic if inside a PythonAnywhere hosting server
    if len(list(filter(lambda k: 'PYTHONANYWHERE' in k.upper(), list(os.environ)))) == 0:
        ap = argparse.ArgumentParser()
        if len(ap.parse_known_args()[1]) > 0 or sender_password == "":
            ap.add_argument("-p", "--password", required=True, help="email password")
            args = vars(ap.parse_args())
            sender_password = args['password']

    if sender_password == "":
        raise Exception("sender_password is empty.")

    return sender_password


# called out of main conditional for PythonAnywhere usage
sender_password = get_email_password()
if __name__ == '__main__':
    """
    handle digitalML website requests
    """
    app.run(host='0.0.0.0', port=2048, debug=True)

