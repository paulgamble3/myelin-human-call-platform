from firebase.firebase_utils import write_task_item, retrieve_data, delete_item_by_ref
import random
from time import sleep

FIREBASE_DB = "myelin_hth_2_9_WAITING_PATIENTS"

PAIRING_DB = "myelin_hth_2_9_PAIRINGS"



SCRIPT_PATIENT_DICT = {
    "CHF_SCRIPT": [
        "CHF_PATIENT"
    ],
    "CKD_SCRIPT": [
        "CKD_PATIENT"
    ],
    "HRT_SCRIPT": [
        "HRT_PATIENT"
    ],
    "COLONOSCOPY_SCRIPT": [
        "COLONSCOPY_PATIENT"
    ],
    "RPM_SCRIPT": [
        "RPM_PATIENT"
    ],
    "HRA_SCRIPT": [
        "HRA_PATIENT"
    ],
}

def ready_for_call(name, phone_number):

    sleep(random.randint(1, 5))

    waiting_patients = retrieve_data(FIREBASE_DB)

    if not waiting_patients:
        # this caller will be the patient
        # sample the case and patient
        # return the patient info
        # write this patient to the db - including patient and case info

        # sample a script and a patient
        script = random.choice(list(SCRIPT_PATIENT_DICT.keys()))
        patient = random.choice(SCRIPT_PATIENT_DICT[script])

        CALLER_INFO = {
            "role": "patient",
            "user_phone_number": phone_number,
            "user_name": name,
            "phone_number_to_call": None,
            "script": script,
            "patient": patient,
        }


        write_task_item(CALLER_INFO, FIREBASE_DB)
        return CALLER_INFO
    
    if len(waiting_patients) > 0:
        # this caller will be the nurse
        # they need to call the patient
        # and then delete the patient from the db

        # get the patient
        patient = waiting_patients[0]

        # delete the patient from the db
        #print("deleting patient", patient)
        patient_fb_id = patient['id']
        patient_result = patient['result']
        delete_item_by_ref(patient_fb_id, FIREBASE_DB)

        # I should write the pairings out to a seperate DB

        CALLER_INFO = {
            "role": "nurse",
            "user_phone_number": phone_number,
            "user_name": name,
            "phone_number_to_call": patient_result['user_phone_number'],
            "script": patient_result['script'],
            "patient": patient_result['patient'],
        }

        write_task_item({
            "NURSE_CALLER": CALLER_INFO,
            "PATIENT_CALLED": patient_result
        }, PAIRING_DB)

        if CALLER_INFO["user_phone_number"] == patient_result["user_phone_number"]:
            return {
                "role": "SELF-CALL"
            }
        # return the patient info to the nurse
        return CALLER_INFO
