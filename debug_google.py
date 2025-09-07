# debug_google.py
from livekit.plugins import google

# Check what the TTS class looks like
print("Google TTS class:", google.TTS)
print("TTS __init__ signature:", google.TTS.__init__.__doc__)

# Try to see available attributes
import inspect
sig = inspect.signature(google.TTS.__init__)
print("TTS __init__ parameters:", list(sig.parameters.keys()))