from .preferences import extract_preferences
from .emotions import extract_emotions
from .facts import extract_facts
import datetime

def extract_memory(messages):
    """
    Main extraction function that combines all memory extraction modules.
    Returns a complete memory object with metadata.
    """
    print("  → Extracting preferences...")
    preferences = extract_preferences(messages)
    
    print("  → Extracting emotional patterns...")
    emotional_patterns = extract_emotions(messages)
    
    print("  → Extracting facts...")
    facts = extract_facts(messages)
    
    memory = {
        "metadata": {
            "total_messages": len(messages),
            "extraction_timestamp": datetime.datetime.now().isoformat(),
            "version": "1.0"
        },
        "preferences": preferences,
        "emotional_patterns": emotional_patterns,
        "facts": facts
    }
    
    print("  ✓ Memory extraction complete!")
    return memory