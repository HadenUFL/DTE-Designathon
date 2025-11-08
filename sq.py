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


def get_patient_by_id(id):
    con = sqlite3.connect("design.db")
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM patients WHERE patient_id = ?", (id,))
    row = cur.fetchone()
    con.close()
    return dict(row) if row else None

def insert_patient(patient_id,name, sex, gender, dob, address, race, height, weight, language,
                   heartrate=None, blood_pressure=None, temp=None, blood_oxygen=None, other=None,
                   phone=None, email=None, conditions=None, history=None, patient_notes=None, unix=None):
    con = sqlite3.connect("design.db")
    cur = con.cursor()
    if unix is None:
        unix = time.time()
    else:
        unix = unix
    def wrap(value):
        return json.dumps({
            "uuid": str(uuid.uuid4()),
            "timestamp": unix,
            "value": value
        })
    cur.execute("""
        INSERT INTO patients VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
    """, (
        wrap(patient_id),
        wrap(name),
        wrap(sex),
        wrap(gender),
        wrap(dob),
        wrap(address),
        wrap(race),
        wrap(height),
        wrap(weight),
        wrap(language),
        wrap(heartrate),
        wrap(blood_pressure),
        wrap(temp),
        wrap(blood_oxygen),
        wrap(other),
        wrap(phone),
        wrap(email),
        wrap(conditions),
        wrap(history),
        wrap(patient_notes)
    ))

    con.commit()
    con.close()


insert_patient(
    patient_id=str(uuid.uuid4()),
    name="Connor Benson",
    sex="M",
    gender="Male",
    dob="1990-04-22",
    address="123 Oak Street, Tampa, FL",
    race="White",
    height=165,
    weight=60,
    language="English",
    phone="555-1234",
    email="cbbenson@example.com",
    conditions="Balding, strong loss of hair"
)
