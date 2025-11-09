from flask import Flask, request
from dataclasses import dataclass
import uuid
app = Flask(__name__)


@dataclass
class Session:
    patient_id: int
    is_doctor: int
    auth_uuid_expiration: float
    auth_uuid: str

## --- Authentication --- ##

@app.route('/authentication/login')
def login():
    if request.is_json:
        username = request.json.get('username')
        password = request.json.get('password')
    else:
        return "Bad Request", 400

    if username is None or password is None:
        return "Bad Request", 400


## --- AI Endpoints --- ##

@app.route('/ai/patient_data_summary')
def patient_data():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        doctor_summary_enabled = request.json.get('doctor_summary_enabled')
    else:
        return "Bad Request", 400

    if auth_uuid is None or doctor_summary_enabled is None:
        return "Bad Request", 400


@app.route('/ai/appointment_summary')
def appointment_summary():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        doctor_summary_enabled = request.json.get('doctor_summary_enabled')
        appointment_id = request.json.get('appointment_id')
    else:
        return "Bad Request", 400

    if auth_uuid is None or doctor_summary_enabled is None or appointment_id is None:
        return "Bad Request", 400


@app.route('/ai/extract_data_property')
def extract_data():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        desired_property = request.json.get('desired_property')
    else:
        return "Bad Request", 400

    if auth_uuid is None or desired_property is None:
        return "Bad Request", 400


@app.route('/ai/start_intake_chat_session')
def start_intake_chat_session():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        appointment_id = request.json.get('appointment_id')
    else:
        return "Bad Request", 400

    if auth_uuid is None or appointment_id is None:
        return "Bad Request", 400


@app.route('/ai/send_message')
def send_message():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        intake_chat_id = request.json.get('intake_chat_id')
        message = request.json.get('message')
    else:
        return "Bad Request", 400

    if auth_uuid is None or intake_chat_id is None or message is None:
        return "Bad Request", 400


## --- Appointments Endpoints --- ##

@app.route('/appointments/create')
def appointments_create():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        patient_id = request.json.get('patient_id')
        appointment_type = request.json.get('type')  # 'type' is a built-in, so renamed variable
        patient_needs = request.json.get('patient_needs')
    else:
        return "Bad Request", 400

    if auth_uuid is None or patient_id is None or appointment_type is None or patient_needs is None:
        return "Bad Request", 400


@app.route('/appointments/get_data')
def appointments_get_data():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        appointment_id = request.json.get('appointment_id')
    else:
        return "Bad Request", 400

    if auth_uuid is None or appointment_id is None:
        return "Bad Request", 400


@app.route('/appointments/get_property')
def appointments_get_property():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        appointment_id = request.json.get('appointment_id')
        property_name = request.json.get('property_name')
    else:
        return "Bad Request", 400

    if auth_uuid is None or appointment_id is None or property_name is None:
        return "Bad Request", 400


@app.route('/appointments/modify_datapoint')
def appointments_modify_datapoint():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        appointment_id = request.json.get('appointment_id')
        property_name = request.json.get('property_name')
        datapoint_id = request.json.get('datapoint_id')
        new_value = request.json.get('new_value')
    else:
        return "Bad Request", 400

    if auth_uuid is None or appointment_id is None or property_name is None or datapoint_id is None or new_value is None:
        return "Bad Request", 400


@app.route('/appointments/add_datapoint')
def appointments_add_datapoint():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        appointment_id = request.json.get('appointment_id')
        property_name = request.json.get('property_name')
        datetime = request.json.get('datetime')
        new_value = request.json.get('new_value')
    else:
        return "Bad Request", 400

    if auth_uuid is None or appointment_id is None or property_name is None or datetime is None or new_value is None:
        return "Bad Request", 400


## --- Patients Endpoints --- ##

@app.route('/patients/get_data')
def patients_get_data():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        patient_id = request.json.get('patient_id')
    else:
        return "Bad Request", 400

    if auth_uuid is None or patient_id is None:
        return "Bad Request", 400


@app.route('/patients/get_property')
def patients_get_property():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        patient_id = request.json.get('patient_id')
        property_name = request.json.get('property_name')
    else:
        return "Bad Request", 400

    if auth_uuid is None or patient_id is None or property_name is None:
        return "Bad Request", 400


@app.route('/patients/modify_datapoint')
def patients_modify_datapoint():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        patient_id = request.json.get('patient_id')
        property_name = request.json.get('property_name')
        datapoint_id = request.json.get('datapoint_id')
        new_value = request.json.get('new_value')
    else:
        return "Bad Request", 400

    if auth_uuid is None or patient_id is None or property_name is None or datapoint_id is None or new_value is None:
        return "Bad Request", 400


@app.route('/patients/add_datapoint')
def patients_add_datapoint():
    if request.is_json:
        auth_uuid = request.json.get('auth_uuid')
        patient_id = request.json.get('patient_id')
        property_name = request.json.get('property_name')
        datetime = request.json.get('datetime')
        new_value = request.json.get('new_value')
    else:
        return "Bad Request", 400

    if auth_uuid is None or patient_id is None or property_name is None or datetime is None or new_value is None:
        return "Bad Request", 400

if __name__ == '__main__':
    app.run(debug=True)