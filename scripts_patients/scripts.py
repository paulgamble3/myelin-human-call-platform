

CHF_OBJECTIVES = """
This call is a routine CHF Assessment\n
Verify the patient’s identity - First name, Last name, DOB\n
Ask the patient if they have any new or worsening shortness of breath with activity, laying down, or at rest?\n
Ask the patient if they have any ongoing or worsening chest pain\n
Ask the patient if they have any new or worsening dry cough\n
Ask the patient if they have increased swelling in their feet, ankle, stomach or legs\n
Ask the patient weigh themselves daily\n
If they weigh themselves regularly, ask the patient if they have gained more than 2 pounds in the past day or 5 pounds in the past week.\n
If they do not weigh themselves regularly, reiterate the importance of doing so\n
Ask the patient if they are using more pillows at night to sleep\n
Inform the patient that we just performed a simple CHF assessment and encourage them to do it at home every day\n
Review the patient’s current medications (new + old, excluding discontinued) with the patient, including dosage\n
Review patient's diet, educate the patient on following low sodium diet and fluid restriciton if necessary\n
When is the next appointment, make sure theyre planning on going
"""

CKD_OBJECTIVES = """
This call is a post-discharge CKD check-in\n
Set context for the call - patient was recently discharged and you're calling to check in\n
Check blood pressure (and blood sugar if diabetic)\n
Answer questions about lab results\n
Review medications\n
Review diet and provide recommendations\n
Check on other chronic conditions (if any)\n
Close call
"""


HRT_OBJECTIVES = """
This is follow-up call for a post-menopausal patient who has been prescriped estradiol HRT\n
Check whether patient received new medications: estradiol cream\n
Check whether patient has started taking new medications\n
If they have, check if patient is experiencing any side effects\n
If they have not, coach them on how to use the Estradiol prescription\n
Encourage patient to stay with the treatment until it takes effect\n
Ask about current symptoms and offer advice on how to manage them\n
Offer self-advocacy tips\n
Close Call\n
"""

COLONOSCOPY_OBJECTIVES = """
This a pre-op call for a patient scheduled for a colonoscopy\n
Set context for the call - the patient has a colonoscopy scheduled for tomorrow\n
Review arrival time and location - Bridgemoore Memorial Hospital, first floor 7am\n
Review stoppage instructions for medications - anti coagulants\n
Discuss low fiber and clear liquid diet\n
Review bowel prep instructions - begin GoLytely this evening at 8pm\n
Remind about NPO after midnight\n
Close call\n
"""

RPM_OBJECTIVES = """
This is a call to help a patient with their new remote patient monitoring devices\n
Check on patient's use of their monitoring device - a wifi scale, a blood pressure cuff, and a pulse oximeter\n
Understand why patient may be struggling to use the device(s)\n
Help patient overcome barriers\n
Provide (basic) tech support if needed\n
Have patient use device(s) during the call\n
Close Call\n
"""

HRA_OBJECTIVES = """
You will be conducting a Health Risk Assessment (HRA) with the patient on behalf of their insurance company. Ask the following questions in order and be sure to give the patient the answer choices for each question. There should not be much back-and-forth conversation for this call type outside of the questions and answers.\n
1. Overall Health and Vaccinations:\n
 - First you would like to get started by asking the patient how they rate their overall health: would they say it's (a) excellent (b) Very good (c) good (d) fair (e) poor. You may have a dialogue with the patient if needed to help them answer you. There are no other options available, you must determine which choice to select.\n
  - Next, ask the patient if they have already received a flu shot this year or if they are planning to receive one. (a) Yes (b) No.\n
  - Ask the patient if they remember when they last received a pneumonia vaccine. Ask questions until you determine which of the following to mark: (a) In the last year, (b) in the last 2-4 years (c) in the last 5 years (d) in the last 10 years (e) never. Mark never if the patient can't remember even after you probe. There are no other options available, you must determine which choice to select.\n
  - Educate the patient on why it's important to get their vaccinations on time.\n
2. Gender-specific preventive screenings:\n
  - Tell the patient that the next set of questions is about preventive health screenings.\n
  - If the patient is female, Ask the patient if they have ever received a mammogram. The patient is female. Then ask simple follow-up questions until you determine which of the following to mark: (a) In the last year, (b) in the last 2-4 years (c) in the last 5 years (d) in the last 10 years (e) never (f) not applicable. Mark never if the patient can't remember even after you probe. There are no other options available, you must determine which choice to select.\n
  - If the patient is female, Ask the patient if they have ever received a pap smear. The patient is female. Then ask simple follow-up questions until you determine which of the following to mark: (a) In the last year, (b) in the last 2-4 years (c) in the last 5 years (d) in the last 10 years (e) never (f) not applicable. Mark never if the patient can't remember even after you probe. There are no other options available, you must determine which choice to select.\n
  - If the patient is male, Ask the patient if they have ever received a colonoscopy to screen for colorectal cancer. The patient is female. Then ask simple follow-up questions until you determine which of the following to mark: (a) In the last year, (b) in the last 2-4 years (c) in the last 5 years (d) in the last 10 years (e) never (f) not applicable. Mark never if the patient can't remember even after you probe. There are no other options available, you must determine which choice to select.\n
  - Educate the patient on why getting their preventive screenings is important. If they haven't gotten them, ask them why not and then provide targeted advice based on what they say.\n
3. Physical activity and medications:\n
  - Ask the patient if they regularly physical activity or take part in a physical physical activity program. The options are (a) yes, daily (b) yes, more than 3 times a week but not daily, (c) yes, fewer than 3 times a week, or (d) no. If they patient is doing a great job, tell them so.\n
  - Educate the patient on why it's important to exercise. Ask the patient how often they take medications. The options are (a) daily (b) weekly, (c) as needed (d) never\n
4. Acute events:\n
  - Ask the patient if they've fallen in the past 6 months. The options are (a) yes (b) no. If they said yes, empathetically acknowlege what they said and ask how the recovery was.\n
  - Ask the patient if they've been to the emergency room in the past 6 months. The options are (a) yes (b) no. If they said yes, empathetically acknowlege what they said and ask if they feel better now.\n
  - Ask the patient how many times they've have had unplanned overnight stays as a patient in a hospital. If they said yes, empathetically acknowlege what they said and ask how long they had to stay in the hospital for.\n
  - Give a 1-2 sentence comment on the patient's responses\n
5. Nutrition:\n
  - Warmly tell the patient that the next few questions are about their physical wellbeing and nutrition. Ask the patient if their doctor has recently told them they need to lose weight. The options are (a) yes (b) no\n
  - Ask the patient if they are on a special diet recommended by the doctor. The options are (a) yes (b) no\n
  - Warmly comment on the patient's responses with one to two sentences. Ask the patient how many sugar sweetened beverages that aren't labeled as 'diet' do they typically consume in a day. Examples are regular coke, sprite, and gatorade. The options are (a) 0 (b) 1 (c) 2-3 (d) 4 or more. If the patient doesn't drink any, tell them that's great for their health and educate them on why.\n
  - Ask the patient if in the past two weeks they've experienced a change in the amount they normally eat, including either poor appetite or overeating. The options are (a) yes (b) no\n
6. Tobacco, drugs and alcohol:\n
  - Warmly tell the patient that the next few questions are about tobacco and alcohol use. Ask the patient when was the last time they smoked or used any tobacco products. The options are (a) Today (b) Last week, (c) last month, (d) in the last 3 months, (e) last year, (f) a year to 5 years ago, (g) longer than 5 years ago, or (h) never. Choose the option that best fits the patient's response. There are no other options available, you must determine which choice to select.Educate them on why smoking is bad. If the patient does not smoke, tell them they're doing a great job taking care of their health.\n
  - If the patient indicated they've used tobacco products in the last day or week, ask them if they are interested in quitting. Mark (a) yes or (b) no. Otherwise, mark (c) not applicable.\n
  - Ask the patient if they drink alcohol. The options are (a) yes (b) no. If the patient does not drink alcohol, praise them.\n
  - If the patient indicated they use tobacco or alcohol, ask them if they ever think they should cut down on drug or alcohol use. The options are (a) yes (b) no. Warmly educate them on they should reduce their use of tobacco and alcohol.\n
7. Depression:\n
  - Warmly tell the patient that the next few questions you're going to ask them are about their mood and emotional wellbeing. Ask the patient if they have felt stressed or anxious in the last 2 weeks. The options are (a) yes (b) no.\n
  - Ask the patient if they have had little interest or pleasure in doing things they normally like to do in the last 2 weeks. The options are (a) yes (b) no\n
  - Ask the patient if they have felt down, depressed, or 'blue' more than usual in the last 2 weeks. The options are (a) yes (b) no\n
  - Warmly say one to two sentences about the patient's responses to help them feel heard and supported.\n
8. Sleep:\n
  - Tell the patient that the next question is about their sleep. Ask them if they have expereinced a signficiant change in the amount they normally sleep (either trouble getting to sleep or sleeping too much) in the past 2 weeks. The options are (a) yes (b) no\n
9. Beliefs:\n
  - Tell the patient for the next set of questions, you'll make a statement and you'd like them to tell you if they strongly disagree, disagree, agree, or strongly agree. Sound good?\n
  - The statement is 'I am ultimately the one responsible for taking care of my health and wellness.' Do they (a) strongly disagree, (b) disagree, (c) agree, or (d) strongly agree? Do not state the letters to the patient.\n
  - The statement is 'It is important for me to take an active role in my health care'. Do they (a) strongly disagree, (b) disagree, (c) agree, or (d) strongly agree? Do not state the letters to the patient.\n
  - The statement is 'I am confident I can prevent or reduce problems associated with my health'. Do they (a) strongly disagree, (b) disagree, (c) agree, or (d) strongly agree? Do not state the letters to the patient.\n
  - Warmly comment 1 to 2 sentences about the patient's responses to help them feel heard and supported.\n
10. Support from others:\n
  - Thank the patient for bearing with you. Tell the patient these are the last two questions. Ask the patient how often do they need to have someone help when they read instructions, pamphlets or other written materials from their doctor or pharmacy. The options are (a) always, (b) usually, (c) sometimes, (d) never. Do not state the letters to the patient.\n
  - Ask the patient who they live with. Ask simple follow up questions until you know which box to check. (a) alone (b) with spouse (c) with other family member(s) (d) with non-relative(s) (e) in a nursing home or assisted living facility. Do not state the letters to the patient.\n
"""


SCRIPTS = {
    "CHF_SCRIPT": CHF_OBJECTIVES,
    "CKD_SCRIPT": CKD_OBJECTIVES,
    "HRT_SCRIPT": HRT_OBJECTIVES,
    "COLONOSCOPY_SCRIPT": COLONOSCOPY_OBJECTIVES,
    "RPM_SCRIPT": RPM_OBJECTIVES,
    "HRA_SCRIPT": HRA_OBJECTIVES
}