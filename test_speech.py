# test_speech.py
from speech_utils import process_speech

test_phrases = [
    "That's really funny. I can't believe you said that.",
    "So, what do you want to do today?",
    "I think the weather is nice outside.",
    "That joke was hilarious! I'm still laughing about it.",
    "Okay, let me explain how this works.",
]

print("Testing natural speech patterns:\n")
for phrase in test_phrases:
    print(f"Original: {phrase}")
    print(f"Chaotic: {process_speech(phrase, 'chaotic')}")
    print(f"Nonchalant: {process_speech(phrase, 'nonchalant')}")
    print(f"Therapist: {process_speech(phrase, 'therapist')}")
    print("---")