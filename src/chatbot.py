import openai
import config

# Set up the OpenAI API key from the config file
openai.api_key = config.OPENAI_API_KEY

def get_chat_response(user_input):
    """
    Sends user input to the GPT-3 model and returns the response.
    """
    # Prepare the prompt for GPT-3
    prompt = format_prompt(user_input)
    
    # Call OpenAI's API with the formatted prompt
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or use gpt-4 if available
        messages=[{"role": "user", "content": prompt}]
    )
    
    # Extract the response and return it
    return response.choices[0].message['content'].strip()

def format_prompt(user_input):
    """
    Format the prompt for GPT-3.
    """
    return f"User: {user_input}\nChatbot:"
