from flask import Flask, request, jsonify
from chatbot import get_chat_response
from linkedin_api import get_linkedin_profile
from course_recommendation import recommend_courses
import config

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat(): 
    user_input = request.json.get('user_input')  # Fixed the input key here
    if user_input:
        # Get chatbot response
        chatbot_response = get_chat_response(user_input)
        return jsonify({"response": chatbot_response})
    return jsonify({"error": "Invalid input"}), 400

@app.route('/linkedin-profile', methods=['GET'])
def linkedin_profile():
    # Fetch LinkedIn profile using LinkedIn API
    profile_data = get_linkedin_profile(config.LINKEDIN_ACCESS_TOKEN)
    return jsonify(profile_data)

@app.route('/recommend-courses', methods=['POST'])
def recommend_courses_route():
    # Get LinkedIn profile and user input to recommend courses
    profile_data = get_linkedin_profile(config.LINKEDIN_ACCESS_TOKEN)
    user_input = request.json.get('user_input')
    
    courses = recommend_courses(profile_data, user_input)
    return jsonify({"courses": courses})

if __name__ == '__main__':
    app.run(debug=True)
