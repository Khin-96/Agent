# check_xai_roles.py
from xai_sdk import AsyncClient
import asyncio

async def check_roles():
    try:
        # Let's see what the chat module expects
        from xai_sdk import chat
        print("Chat module contents:", [a for a in dir(chat) if not a.startswith('_')])
        
        # Check if there are any enum definitions
        try:
            from xai_sdk.chat import RoleType
            print("RoleType values:", [r for r in dir(RoleType) if not r.startswith('_')])
        except ImportError:
            print("No RoleType enum found")
            
    except Exception as e:
        print("Error:", e)

asyncio.run(check_roles())