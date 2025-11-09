from ollama import chat
from ollama import ChatResponse

MODEL = "nemotron-nano:9b-v2-q8_0"

def patient_data_summary(patient_data_string, for_doctor=False):
    messages = [
        {
            'role': 'system',
            'content': f"You are AI that summarizes patient data. You will be given a set of patient data, summarize it into a form fit for {"a doctor/physician" if for_doctor else "a patient."}. Keep your responses concise, and only include information that is present in the provided data. Do not add any more information.",
        },
        {
            'role': 'user',
            'content':patient_data_string,
        }
    ]

    response = chat(model=MODEL, messages=messages)

    return response.message

def appointment_data_summary(appointment_data_string, for_doctor=False):
    messages = [
        {
            'role': 'system',
            'content': f"You are AI that summarizes appointment data. You will be given a set of data from a primary care appointment, summarize it into a form fit for {"a doctor/physician" if for_doctor else "a patient."}. Keep your responses concise, and only include information that is present in the provided data. Do not add any more information.",
        },
        {
            'role': 'user',
            'content': appointment_data_string,
        }
    ]

    response = chat(model=MODEL, messages=messages)

    return response.message

def extract_parameter(patient_report, property, property_description):
    messages = [
        {
            'role': 'system',
            'content': f"You are AI that looks for a certain bit of information. Once that information is found, you ONLY respond with the information that is desired. You can only retrieve this information from the text provided. If it is not present, simply state \"DATA NOT PRESENT\". If it is present, only respond with the information directly.",
        },
        {
            'role': 'user',
            'content': patient_report + f"\n\nYou are looking for {property}. {property_description}",
        }
    ]

    response = chat(model=MODEL, messages=messages)

    return response.message