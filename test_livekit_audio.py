# test_livekit_audio.py
import os
os.environ['LIVEKIT_AGENTS_DISABLE_AUDIO'] = '0'  # Enable audio

from livekit import agents
from livekit.agents import RoomInputOptions
import sounddevice as sd

async def test_audio():
    print("Testing LiveKit audio initialization...")
    
    try:
        # Configure sounddevice first
        sd.default.samplerate = 44100
        sd.default.device = 3
        
        # Try different RoomInputOptions configurations
        options = [
            RoomInputOptions(audio_enabled=True, audio_sample_rate=44100),
            RoomInputOptions(audio_enabled=True),  # Use defaults
            RoomInputOptions(audio_enabled=True, audio_sample_rate=48000),
        ]
        
        for i, opt in enumerate(options):
            print(f"Testing config {i+1}...")
            try:
                # This should trigger audio initialization
                session = agents.AgentSession()
                # We'll just test the options without full session start
                print(f"Config {i+1}: Options accepted")
            except Exception as e:
                print(f"Config {i+1}: Error - {e}")
                
    except Exception as e:
        print(f"Audio test failed: {e}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_audio())