import sqlite3
import uuid
import time
import json





#con.execute("CREATE TABLE appointments(appointment_id PRIMARY KEY,patient_id,datetime,appointment_symptoms,appointment_reasons,appointment_doctor,appointment_notes)")
#con.execute("CREATE TABLE patients(patient_id PRIMARY KEY,demo_name,demo_sex,demo_gender,demo_dob,demo_address,demo_race,demo_height,demo_weight,demo_language,vital_heartrate,vital_bloodpressure,vital_temperature,vital_bloodoxygen,vitals_other,contact_phone,contact_email,conditions_chronic,history_appointments,patient_notes)")cur.execute("""




def get_all_patients():
    con = sqlite3.connect("design.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM patients")
    result = cur.fetchall()
    return result

def get_all_appointments():
    con = sqlite3.connect("design.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM appointments")
    result = cur.fetchall()
    return result

def get_patient_by_id(id):
    con = sqlite3.connect("design.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM patients WHERE patient_id LIKE ?", ('%' + id +'%',))
    row = cur.fetchone()
    con.close()
    nested_dict = {json.loads(val)["key"]: json.loads(val) for val in row}
    return nested_dict

def get_appointment_by_id(id):
    con = sqlite3.connect("design.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM appointments WHERE appointment_id LIKE ?", ('%' + id + '%',))
    row = cur.fetchone()
    con.close()
    nested_dict = {json.loads(val)["key"]: json.loads(val) for val in row}
    return nested_dict


def insert_patient(patient_id,name,username,password, sex, gender, dob, address, race, height, weight, language,
                   heartrate=None, blood_pressure=None, temp=None, blood_oxygen=None, other=None,
                   phone=None, email=None, conditions=None, history=None, patient_notes=None, unix=None):
    con = sqlite3.connect("design.db")
    cur = con.cursor()
    if unix is None:
        unix = time.time()
    else:
        unix = unix
    def wrap(value,key):
        return json.dumps({
            "uuid": str(uuid.uuid4()),
            "timestamp": unix,
            "key": key,
            "value": value
        })
    cur.execute("""
        INSERT INTO patients VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """, (
        wrap(patient_id,"patient_id"),
        wrap(name,"demo_name"),
        wrap(sex,"demo_sex"),
        wrap(gender,"demo_gender"),
        wrap(dob,"demo_dob"),
        wrap(address,"demo_address"),
        wrap(race,"demo_race"),
        wrap(height,"demo_height"),
        wrap(weight,"demo_weight"),
        wrap(language,"demo_language"),
        wrap(heartrate,"vital_heartrate"),
        wrap(blood_pressure,"vital_bloodpressure"),
        wrap(temp,"vital_temperature"),
        wrap(blood_oxygen,"vital_bloodoxygen"),
        wrap(other,"vital_other"),
        wrap(phone,"contact_phone"),
        wrap(email,"contact_email"),
        wrap(conditions,"conditions_chronic"),
        wrap(history,"history_appointments"),
        wrap(patient_notes,"patient_notes"),
        wrap(username,"username"),
        wrap(password,"password")
    ))

    con.commit()
    con.close()

def insert_appointment(appointment_id,patient_id,datetime,symptoms=None,reason=None,doctor=None,notes=None):
    con = sqlite3.connect("design.db")
    cur = con.cursor()
    if datetime is None:
        datetime = time.time()
    else:
        datetime = datetime
    def wrap(value,key):
        return json.dumps({
            "uuid": str(uuid.uuid4()),
            "timestamp": datetime,
            "key":key,
            "value": value
        })
    cur.execute("""
        INSERT INTO appointments VALUES (
            ?, ?, ?, ?, ?, ?, ?
        )
    """, (
        wrap(appointment_id,"appointment_id"),
        wrap(patient_id,"patient_id"),
        wrap(datetime,"datetime"),
        wrap(symptoms,"appointment_symptoms"),
        wrap(reason,"appointment_reasons"),
        wrap(doctor,"appointment_doctor"),
        wrap(notes,"appointment_notes")
    ))
    con.commit()
    con.close()
print(get_appointment_by_id("203940d9-5f81-4b5e-90c8-3e62a4d87570"))
