import google.generativeai as genai

# Set your Gemini API key here
Api_key = "your-gemini-api-key"
genai.configure(api_key=Api_key)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def is_inappropriate(text):
    """
    Use Gemini to determine if the text is inappropriate.
    """
    prompt = f"Is the following text inappropriate? Respond with 'yes' or 'no' only:\n{text}"
    try:
        response = model.generate_content(prompt)
        return response.text.strip().lower() == 'yes'
    except Exception as e:
        print(f"Error checking content: {e}")
        return False  # Assume content is appropriate if there's an error

while True:
    prompt = input("Ask me anything: ")
    
    # Exit condition
    if prompt.lower() == "exit":
        print("Exiting the chat. Goodbye!")
        break
    
    # Check if the user's query is inappropriate
    if is_inappropriate(prompt):
        print("Your query contains inappropriate content and cannot be processed.")
        continue  # Skip generating a response
    
    # Generate and stream the response
    try:
        response = chat.send_message(prompt, stream=True)
        for chunk in response:
            if chunk.text:
                print(chunk.text)
    except Exception as e:
        print(f"An error occurred: {e}")
