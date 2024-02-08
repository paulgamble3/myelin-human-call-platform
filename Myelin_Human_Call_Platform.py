import streamlit as st
import hth_utils

st.title('Myelin Human Call Platform')

user_name = st.text_input("Please enter your name:", key="user_name")
user_phone_number = st.text_input("Please enter your phone number:", key="user_phone_number")

with st.form(key='my_form'):
    # Form contents
    submit_button = st.form_submit_button(label="I'm ready for another call")

    if submit_button:
        st.write(f"Thank you {user_name}! We will call you at {user_phone_number} shortly.")


        CALLER_INFO = hth_utils.ready_for_call(user_phone_number)
        
        if CALLER_INFO['role'] == "patient":
            st.write("You are the patient. We will call you shortly.")
            st.write(CALLER_INFO)

        if CALLER_INFO['role'] == "nurse":
            st.write("You are the nurse. Please call the patient.")
            st.write("You will be calling", CALLER_INFO['phone_number_to_call'])
            st.write(CALLER_INFO)

        # give message to the nurse
        # the script 
        # the patient


