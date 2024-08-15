"""Build a Simple LLM Application"""

# Import the necessary libraries.
import os 
import groq
from dotenv import load_dotenv

# Load the environment variables from the .env file.
load_dotenv()

# Load the GROQ API KEY from the env file.
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")


client = groq.Groq(api_key=GROQ_API_KEY)


system_prompt = """You are a helpful virtual assistant \
    Your name is Silas. Your goal is to provide useful and relevant \
        responses to my requests. 
    """

models = [
    "llama-3.1-405b-reasoning",
    "llama-3.1-70b-versatile",
    "llama-3.1-8b-instant",
    "mixtral-8x7b-32768"
]


def generate_response(model, query, temperature=0):
    
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system",
            "content": system_prompt},
            
            {"role": "user",
            "content": query}
            ],
        temperature=temperature,
        response_format= {"type": "text"}
    )
    
    response = response.choices[0].message.content
    
    return response 




if __name__ == "__main__":
    model = models[2]
    user_query = input("Enter your message or query? ")
    response = generate_response(model=model, query=user_query, temperature=0.9)
    

    
    print("\n" + response) 

 
