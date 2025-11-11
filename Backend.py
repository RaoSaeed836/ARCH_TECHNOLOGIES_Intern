import ollama

def get_response(user_prompt):
    try:
        client = ollama.Client()
        model = "rao:latest"   # apna model name
        result = client.generate(model=model, prompt=user_prompt)
        return result.response
    except Exception as e:
        return f"Error: {str(e)}"
