from fastapi import FastAPI, Request
from simple_llm import *


app = FastAPI()


@app.get("/healthz")
async def health():
    return {
        "application": "Simple LLM API", 
        "message": "Running Successfully!"
    }
    
    
@app.post("/chat")
async def generate_chat(request: Request):
    
    query = await request.json()
    model = query["model"]
    
    try: 
        temperature = float(query["temperature"])
    
    except:
        return {
            "Error": "Invalid temperature input, pass a number between 0 and 2."
        }
        
    if model not in models:
        return {
            "Error": "You did not pass a correct model code!"
        }
        
    response_generated = generate_response(model=model, query=query["question"], temperature=temperature)
    
    return {
        "Status": "Success",
        "Response": response_generated
    }





if __name__ == "__main__":
    import uvicorn
    print("Starting LLM API")
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    
