import os 
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key=os.environ.get("GEMINI_API_KEY")

    client= genai.Client(api_key=api_key)

    response= client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents="why sky is blue?"
    )

    print(response.text)
    if response is None or response.usage_metadata is None:
        print("response doesnt have")
        return
    print(f"Prompt token:{response.usage_metadata.prompt_token_count}")
    print(f"Response token:{response.usage_metadata.candidates_token_count}")

main()