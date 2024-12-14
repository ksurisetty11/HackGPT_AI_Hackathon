import openai
import os
from dotenv import load_dotenv, dotenv_values
from career_advice import get_career_courses, fetch_linkedin_profile

# Load environment variables from .env file
load_dotenv()

# Initialize the OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def chatbot():
    """
    Main chatbot function to handle user interactions.
    """
    print("AI Chatbot: Hi! I'm your career advisor chatbot. How can I assist you today?")
    print("Type 'career' for career advice, 'linkedin' to fetch LinkedIn profile data, or 'exit' to end the chat.")

    while True:
        # Take user input
        user_input = input("You: ")
        
        # Exit command
        if user_input.lower() == "exit":
            print("AI Chatbot: Goodbye! Wishing you a successful career journey!")
            break
        
        # Career advice command
        elif user_input.lower() == "career":
            print("AI Chatbot: Please tell me about your background and career interests.")
            user_background = input("You: ")  # Ask for career background
            career_advice = get_career_courses(user_background)
            print(f"AI Chatbot: {career_advice}")
        
        # LinkedIn profile integration
        elif user_input.lower() == "linkedin":
            public_profile_url = input("AI Chatbot: Please provide the LinkedIn public profile URL: ")
            profile_data = fetch_linkedin_profile(public_profile_url)
            if "error" in profile_data:
                print(f"AI Chatbot: {profile_data['error']}")
            else:
                print("AI Chatbot: Here's what I found about the user:")
                print(f"Name: {profile_data['name']}")
                print(f"Headline: {profile_data['headline']}")
                print(f"Industry: {profile_data['industry']}")
                print(f"Skills: {', '.join(profile_data['skills']) if profile_data['skills'] else 'No skills listed'}")
        
        # General chatbot conversation
        else:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",  # You can replace with 'gpt-4' if available
                    messages=[
                        {"role": "system", "content": "You are a helpful and friendly chatbot."},
                        {"role": "user", "content": user_input}
                    ]
                )
                ai_response = response["choices"][0]["message"]["content"]
                print(f"AI Chatbot: {ai_response}")
            except Exception as e:
                print(f"AI Chatbot: Oops! Something went wrong. {e}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
