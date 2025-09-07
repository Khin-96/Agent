# test_grok_api.py
import os
import asyncio
from dotenv import load_dotenv
from xai_sdk import AsyncClient

load_dotenv()

async def test_grok_api():
    api_key = os.getenv("XAI_API_KEY")
    if not api_key:
        print("XAI_API_KEY not set in .env file")
        return
        
    try:
        client = AsyncClient(api_key=api_key)
        
        # Test the chat.create method
        response = await client.chat.create(
            model="grok-beta",
            messages=[{"role": "user", "content": "Hello! How are you?"}],
            temperature=0.8,
            max_tokens=50
        )
        
        print("API call successful!")
        print("Response type:", type(response))
        print("Response attributes:", [a for a in dir(response) if not a.startswith('_')])
        
        # Try to extract content
        if hasattr(response, 'choices') and len(response.choices) > 0:
            print("Content:", response.choices[0].message.content)
        elif hasattr(response, 'text'):
            print("Content:", response.text)
        else:
            print("Raw response:", response)
            
    except Exception as e:
        print("Error:", e)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(test_grok_api())