# check_livekit_api.py
from livekit.agents import llm
print("llm module contents:", [a for a in dir(llm) if not a.startswith('_')])

# Check what's available for responses
try:
    from livekit.agents.llm import ChatResponse
    print("ChatResponse found")
except ImportError:
    print("ChatResponse not found")

# Check what's available for tools
try:
    from livekit.agents.llm import Tool
    print("Tool found")
except ImportError:
    print("Tool not found")

# Check the LLM base class
print("LLM class methods:", [m for m in dir(llm.LLM) if not m.startswith('_')])