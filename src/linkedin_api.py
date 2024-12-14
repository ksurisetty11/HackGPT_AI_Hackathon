import requests

def get_linkedin_profile(access_token):
    # LinkedIn API 
    url = "https://api.linkedin.com/v2/me"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def get_user_skills(access_token):
    # List of skills
    url = "https://api.linkedin.com/v2/skills"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    # Return skills list from LinkedIn
    return response.json()