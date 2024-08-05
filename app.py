from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def priti_chatbot(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case-insensitivity
    
    responses = {
        "hello": "Hello there! I am Priti",
        "hi": "Hello there! I am Priti",
        "who are you?": "I'm a rule-based chatbot developed by Priti.",
        "how are you?": "I'm fine. What about you? I'm here to assist you!",
        "what is artificial intelligence?": "Artificial intelligence (AI) refers to the simulation of human intelligence processes by machines.",
        "name some fruits": "Yeah sure! Mango, Apple, Guava, Grapes are some fruits which I can suggest",
        "name some vegetables": "Yeah sure! Potato, Tomato, Carrot, Cabbage are some vegetables which I can suggest",
        "bye": "Goodbye! Have a great day!",
        "goodbye": "Goodbye! Have a great day!",
        "how can i find a doctor in my area?": "You can use our 'Find Doctor' feature on the homepage to search for doctors in your area.",
        "what services does the clinic offer?": "Our clinic offers a variety of services including general consultations, specialist visits, lab tests, and more.",
        "how can i book an appointment online?": "You can book an appointment online through our website's 'Appointment' section.",
        "what are the clinic's operating hours?": "Our clinic operates from 8 AM to 8 PM, Monday to Friday.",
        "is the clinic open on weekends and holidays?": "Yes, the clinic is open on weekends but closed on major holidays.",
        "how do i contact the clinic for emergency services?": "For emergencies, please call our emergency hotline at +012 345 6789.",
        "can i see a specialist without a referral?": "Yes, you can see a specialist without a referral by booking an appointment directly.",
        "what types of insurance do you accept?": "We accept various types of insurance. Please contact our billing department for more details.",
        "how do i cancel or reschedule an appointment?": "You can cancel or reschedule an appointment through our website or by calling our front desk.",
        "are walk-in appointments available?": "Yes, we do accept walk-in appointments but it's best to book in advance.",
        "what should i bring to my appointment?": "Please bring a valid ID, insurance card, and any medical records relevant to your visit.",
        "how do i get my medical records transferred to this clinic?": "You can request a transfer of medical records from your previous healthcare provider.",
        "do you offer telehealth or virtual consultations?": "Yes, we offer telehealth and virtual consultations. You can book these through our website.",
        "how can i access my test results online?": "You can access your test results through our patient portal.",
        "what is the process for getting a prescription refill?": "You can request a prescription refill through our patient portal or by calling our clinic.",
        "are there any patient forms i need to fill out before my visit?": "Yes, there are patient forms you can fill out online before your visit to save time.",
        "how do i prepare for a specific test or procedure?": "Preparation instructions will be provided by your doctor or you can find them on our website under the 'Services' section.",
        "what is your policy on patient confidentiality?": "We adhere to strict patient confidentiality policies to protect your personal information.",
        "how do i pay my bill online?": "You can pay your bill online through our billing section on the website.",
        "what payment methods do you accept?": "We accept credit/debit cards, online payments, and insurance payments.",
        "do you offer payment plans for services?": "Yes, we offer flexible payment plans for certain services.",
        "what should i do if i need medical advice after hours?": "If you need medical advice after hours, please call our 24/7 hotline.",
        "how do i register as a new patient?": "You can register as a new patient by filling out the registration form on our website.",
        "can i choose my own doctor?": "Yes, you can choose your own doctor based on availability.",
        "how do i provide feedback about my visit?": "You can provide feedback through our website or by filling out a feedback form at the clinic.",
        "do you have a patient portal? how do i access it?": "Yes, we have a patient portal. You can access it through the 'Patient Portal' link on our website.",
        "what vaccinations do you offer?": "We offer a range of vaccinations including flu shots, COVID-19 vaccines, and more.",
        "how often should i get a health check-up?": "It's recommended to have a health check-up at least once a year or as advised by your doctor.",
        "what are the common symptoms of [specific illness]?": "You can find information on common symptoms of various illnesses in the 'Health Information' section of our website.",
        "how do i know if i need to see a doctor?": "If you're experiencing unusual symptoms or health issues, it's best to consult with a doctor.",
        "what preventive care services do you offer?": "We offer preventive care services such as screenings, vaccinations, and wellness check-ups.",
        "do you provide mental health services?": "Yes, we provide mental health services including counseling and therapy.",
        "can i get a second opinion from another doctor in the clinic?": "Yes, you can request a second opinion from another doctor within our clinic.",
        "are your doctors board certified?": "Yes, all our doctors are board certified in their respective specialties.",
        "what should i do if i have a reaction to medication?": "If you have a reaction to medication, please contact our clinic immediately or seek emergency care.",
        "how do i prepare my child for their first visit to the clinic?": "You can prepare your child by explaining the visit and bringing their favorite toy for comfort.",
        "do you offer any health and wellness programs?": "Yes, we offer various health and wellness programs. Please visit our website for more details.",
        "can i request a specific doctor for my appointment?": "Yes, you can request a specific doctor when booking your appointment.",
        "what is the wait time for an appointment with a specialist?": "Wait times for specialists can vary. Please check with our front desk for current availability.",
        "do you have any resources for managing chronic conditions?": "Yes, we provide resources and support for managing chronic conditions. You can find more information on our website.",
        "how can i get a referral for a specialist?": "You can get a referral for a specialist by consulting with your primary care doctor.",
        "what should i do if i have an issue with my insurance claim?": "If you have an issue with your insurance claim, please contact our billing department for assistance.",
        "how do i update my personal information in your records?": "You can update your personal information through our patient portal or by contacting our front desk.",
        "what languages are spoken at the clinic?": "Our clinic staff speaks multiple languages. Please contact us for specific language availability.",
        "are there any dietary guidelines i should follow before a test?": "Dietary guidelines for tests will be provided by your doctor or you can find them on our website.",
        "do you offer support for patients with disabilities?": "Yes, we offer support and accommodations for patients with disabilities.",
        "how can i get a copy of my medical records?": "You can request a copy of your medical records through our patient portal or by contacting our clinic.",
        "what is your policy on visitors during my appointment?": "Our policy on visitors may vary. Please contact our clinic for the most current information.",
        "can i receive treatment if i am traveling from another city or country?": "Yes, we provide treatment for patients traveling from other cities or countries.",
        "how do i get information about clinical trials or research studies?": "You can get information about clinical trials and research studies through our website or by contacting our research department.",
        "tell me about this website": "This website is designed to provide information about our healthcare services, allow you to find doctors, book appointments, access medical records, and get answers to your health-related questions."
    }

    return responses.get(user_input, "I'm sorry, I didn't quite get that. I am a pre-defined chatbot of Priti. Please ask me pre-defined questions.")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.json.get("message")
    response = priti_chatbot(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
