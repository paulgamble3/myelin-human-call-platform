import streamlit as st
import hth_utils

from scripts_patients.scripts import SCRIPTS
from scripts_patients.patients import PATIENTS

st.title('Myelin Human Call Platform')

user_name = st.text_input("Please enter your name:", key="user_name")
user_phone_number = st.text_input("Please enter your phone number:", key="user_phone_number")

with st.form(key='my_form'):
    # Form contents
    submit_button = st.form_submit_button(label="I'm ready for another call")

    if submit_button:
        #st.write(f"Thank you {user_name}! We will call you at {user_phone_number} shortly.")

        CALLER_INFO = hth_utils.ready_for_call(user_phone_number)
        
        if CALLER_INFO['role'] == "patient":
            st.subheader("You will be playing the patient.")
            st.subheader("A nurse will call you shortly.")
            st.write("If you don't receive a call within 2 minutes, reach out in google chat")
            pt_id = CALLER_INFO['patient']
            st.subheader("You will be playing the following patient:")
            st.write(PATIENTS[pt_id])

            # need to provide the correct google form link

        if CALLER_INFO['role'] == "nurse":
            st.subheader("You are the nurse. Please call the patient.")
            st.write("You will be calling", CALLER_INFO['phone_number_to_call'])
            st.write("If the number is invalid or they don't pick up, reach out in google chat")
            patient_id = CALLER_INFO['patient']
            script_id = CALLER_INFO['script']

            st.subheader("You are calling the following patient:")
            st.write(PATIENTS[patient_id])

            st.subheader("Here are the call objectives:")
            st.write(SCRIPTS[script_id])

            # need to provide the correct google form link


        # give message to the nurse
        # the script 
        # the patient


