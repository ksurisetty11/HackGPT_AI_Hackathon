from flask import Flask, render_template, request, jsonify
from chatbot import get_chat_response
from linkedin_api import get_linkedin_profile
from course_recommendation import recommend_courses
import config

app = Flask(__name__)

#Use html file for formatting 
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat(): 
    user_input = request.json.get('user_input')  # Fixed the input key here
    if user_input:
        # Get chatbot response
        chatbot_response = get_chat_response(user_input)
        return jsonify({"response": chatbot_response})
    return jsonify({"error": "error"}), 400

@app.route('/linkedin-profile', methods=['GET'])
def linkedin_profile():
    try:
        # Fetch LinkedIn profile using LinkedIn API
        profile_data = get_linkedin_profile(config.LINKEDIN_ACCESS_TOKEN)
        return jsonify(profile_data)
    except Exception as e:
        return jsonify({"error": f"Failed to fetch LinkedIn profile: {str(e)}"}), 500

@app.route('/recommend-courses', methods=['POST'])
def recommend_courses_route():
    try:
        # Get LinkedIn profile and user input to recommend courses
        profile_data = get_linkedin_profile(config.LINKEDIN_ACCESS_TOKEN)
        user_input = request.json.get('user_input')
        
        if not user_input:
            return jsonify({"error": "Missing user_input"}), 400
        
        courses = recommend_courses(profile_data, user_input)
        return jsonify({"courses": courses})
    except Exception as e:
        return jsonify({"error": f"Error recommending courses: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
