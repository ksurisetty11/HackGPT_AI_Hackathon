import requests

def get_linkedin_profile(access_token):
    # Fetches the basic profile information of the authenticated user from LinkedIn
    # LinkedIn API endpoint to fetch user profile information
    url = "https://api.linkedin.com/v2/me"
    # Set the authorization header with the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_user_skills(access_token):
    # Fetches list of skills associated with authenticated user's LinkedIn profile
    url = "https://api.linkedin.com/v2/skills"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    # Return skills list from LinkedIn
    return response.json()