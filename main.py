from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    pass

@app.route('/authentication/login')
def login():
    pass

@app.route('/ai/patient_data_summary')
def patient_data():
    pass

@app.route('/ai/extract_data_properly')
def extract_data():
    pass

@app.route('/ai/find_missing_required_properties')
def find_missing_properties():
    pass
