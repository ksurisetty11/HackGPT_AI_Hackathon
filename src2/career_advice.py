import openai
import os
from dotenv import load_dotenv
from linkedin_api import Linkedin

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Authenticate LinkedIn API using credentials from environment variables
linkedin_email = os.getenv("LINKEDIN_EMAIL")
linkedin_password = os.getenv("LINKEDIN_PASSWORD")
linkedin = Linkedin(linkedin_email, linkedin_password)

def get_career_courses(user_input):
    """
    Simulates career course suggestions based on user input.
    Uses OpenAI's API to generate tailored advice.
    
    Args:
        user_input (str): User's background and career interests.
    
    Returns:
        str: Suggested career advice or courses.
    """
    try:
        # Query OpenAI for career advice
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a career advisor specializing in professional growth and skill development."},
                {"role": "user", "content": f"I am looking for career advice. Here is my background and interest: {user_input}"}
            ]
        )
        # Extract and return the response content
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error fetching career courses: {e}"

def fetch_linkedin_profile(public_profile_url):
    """
    Fetch LinkedIn user profile data using public profile URL.

    Args:
        public_profile_url (str): LinkedIn public profile URL of the user.

    Returns:
        dict: Extracted skills or other details from the profile.
    """
    try:
        profile = linkedin.get_profile(public_profile_url)
        skills = profile.get('skills', [])
        return {
            "name": profile.get('firstName') + " " + profile.get('lastName'),
            "skills": skills,
            "headline": profile.get('headline'),
            "industry": profile.get('industryName'),
        }
    except Exception as e:
        return {"error": f"Unable to fetch profile: {e}"}
