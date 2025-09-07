# speech_utils.py
import random
import re
from typing import List, Tuple
from prompts import natural_laughter, add_speech_imperfections

def process_speech(text: str, mode: str = "chaotic") -> str:
    """
    Process text to make it sound more natural with fillers and laughter
    """
    if not text or text.strip() == "":
        return text
    
    # Step 1: Add laughter where appropriate
    text = add_natural_laughter(text, mode)
    
    # Step 2: Add speech imperfections
    text = add_speech_imperfections(text, mode)
    
    return text

def add_natural_laughter(text: str, mode: str) -> str:
    """
    Add natural laughter to appropriate places in text
    """
    # Patterns that might indicate laughter opportunities
    laughter_triggers = [
        r"funny", r"lol", r"lmao", r"hilarious", r"haha", 
        r"joke", r"comedy", r"laugh", r"chuckle", r"giggle"
    ]
    
    # Don't overdo it - only add laughter to some eligible sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)
    result = []
    
    for sentence in sentences:
        # Check if this sentence might warrant laughter
        should_laugh = any(re.search(trigger, sentence.lower()) for trigger in laughter_triggers)
        
        # Also randomly add laughter to some sentences (5% chance)
        random_laugh = random.random() < 0.05 and len(sentence.split()) > 3
        
        if should_laugh or random_laugh:
            # Decide laughter position and intensity
            laughter_intensity = "medium"
            if should_laugh and any(word in sentence.lower() for word in ["hilarious", "lmao", "dying"]):
                laughter_intensity = "high"
            
            # Add laughter either at the beginning, middle, or end
            position = random.choice(["start", "middle", "end"])
            
            if position == "start":
                laughter = natural_laughter(laughter_intensity, mode) + ", "
                sentence = laughter + sentence
            elif position == "middle" and len(sentence.split()) > 4:
                words = sentence.split()
                insert_pos = random.randint(2, len(words) - 2)
                words.insert(insert_pos, natural_laughter(laughter_intensity, mode))
                sentence = " ".join(words)
            else:  # end
                sentence = sentence + " " + natural_laughter(laughter_intensity, mode)
        
        result.append(sentence)
    
    return " ".join(result)