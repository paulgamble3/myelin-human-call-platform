import json

fn = "./patient_info/patient_data.json"

with open(fn, "r") as f:
    data = json.load(f)
    patients = data["patients"]

first_name = "Jill"
last_name = "Davis"

patient_info = False
# get the matching patient
for patient in patients:
    p_info = patient["ehr_data"]["patient"]
    if p_info["first_name"] == first_name and p_info["last_name"] == last_name:
        patient_info = patient["ehr_data"]
        break

if not patient_info:
    print("Patient not found")
    exit()

# build up patient string
patient_string = ""
patient_string += f"Name: {patient_info['patient']['first_name']} {patient_info['patient']['last_name']}\\n\n"
patient_string += f"DOB: {patient_info['patient']['dob']}\\n\n"
patient_string += f"Gender: {patient_info['patient']['gender']} \\n\n"

conditions = patient_info["conditions"]
patient_string += "================================"
patient_string += "\n\\n\\n**Active Conditions:**\\n\n"
for condition in conditions:
    patient_string += f"{condition['display']}\\n\n"
    

medications = patient_info["medications"]
patient_string += "================================"
patient_string += "\n\\n\\n**Active Medications:**\\n\n"
for medication in medications:
    if not medication["active"]:
        continue
    patient_string += f"{medication['display']}\\n\n"

if "numerical_observations" not in patient_info:
    print(patient_string)
    exit()
labs = patient_info["numerical_observations"]
patient_string += "================================"
patient_string += "\n\\n\\n**Recent Labs:**\\n\n"
for lab in labs[:10]:
    patient_string += f"{lab['name']}: {lab['value']} {lab['unit']}\\n\n"


print(patient_string)

# for k, v in patient_info.items():
#     print(k, v)
#     print("\\n\n\\n\n")