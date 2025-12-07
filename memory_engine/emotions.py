import re
from collections import Counter

EMOTION_KEYWORDS = {
    "happy": [
        r"\bhappy\b", r"\bexcited\b", r"\bglad\b", 
        r"\bjoy(?:ful)?\b", r"\bcheerful\b", r"\bdelighted\b",
        r"\bthrilled\b", r"\bpleased\b", r"\becstatic\b",
        r"\boverjoyed\b", r"\bcontent\b", r"\belated\b"
    ],
    "sad": [
        r"\bsad\b", r"\bupset\b", r"\bdown\b", 
        r"\bdepress(?:ed|ing)\b", r"\bunhappy\b",
        r"\bmiserable\b", r"\bheartbroken\b", r"\bmelancholy\b",
        r"\bdespondent\b", r"\bdejected\b", r"\bsorrowful\b"
    ],
    "angry": [
        r"\bangry\b", r"\bmad\b", r"\bfurious\b", 
        r"\bannoyed\b", r"\birrit(?:ated|ating)\b",
        r"\benraged\b", r"\binfuriated\b", r"\blivid\b",
        r"\boutraged\b", r"\bfrustrated\b", r"\baggravated\b"
    ],
    "stressed": [
        r"\bstress(?:ed|ing|ful)?\b", r"\boverwhelm(?:ed|ing)?\b",
        r"\btired\b", r"\bexhausted\b", r"\bburned? out\b",
        r"\bpressured\b", r"\btense\b", r"\bstrained\b",
        r"\bfrazzled\b", r"\bworked up\b"
    ],
    "anxious": [
        r"\banxious\b", r"\bworried\b", r"\bnervous\b", r"\bworry\b",
        r"\bapprehensive\b", r"\buneasy\b", r"\bconcerned\b",
        r"\bpanicked\b", r"\bon edge\b", r"\bjittery\b"
    ],
    "excited": [
        r"\bexcited\b", r"\bthrilled\b", r"\beager\b", r"\bpumped\b",
        r"\benthusiastic\b", r"\bstoked\b", r"\bpsyched\b",
        r"\bamped\b", r"\bfired up\b"
    ],
    "confused": [
        r"\bconfused\b", r"\bpuzzled\b", r"\bbewildered\b",
        r"\bperplexed\b", r"\bbaffled\b", r"\blost\b",
        r"\bunsure\b", r"\buncertain\b"
    ],
    "confident": [
        r"\bconfident\b", r"\bsure\b", r"\bcertain\b",
        r"\bassured\b", r"\bself-assured\b", r"\bproud\b"
    ],
    "motivated": [
        r"\bmotivated\b", r"\bdriven\b", r"\bdetermined\b",
        r"\binspired\b", r"\benergized\b", r"\bfocused\b"
    ],
    "bored": [
        r"\bbored\b", r"\buninterested\b", r"\bindifferent\b",
        r"\bapathetic\b", r"\bunmotivated\b", r"\bdisengaged\b"
    ]
}

NEGATION_WORDS = r"\b(?:not|never|no|n't|neither|nor)\b"

def extract_emotions(messages):
    """
    Extract emotional patterns from messages.
    Returns dominant emotion, secondary emotion, and timeline.
    """
    emotion_counter = Counter()
    emotion_timeline = []
    
    for idx, message in enumerate(messages, start=1):
        msg = message.strip().lower()
        if not msg:
            continue
            
        for emotion, patterns in EMOTION_KEYWORDS.items():
            for pattern in patterns:
                match = re.search(pattern, msg, re.IGNORECASE)
                if match:
                    # Check for negation before the emotion word
                    before_text = msg[max(0, match.start()-30):match.start()]
                    is_negated = re.search(NEGATION_WORDS, before_text, re.IGNORECASE)
                    
                    if not is_negated:
                        emotion_counter[emotion] += 1
                        emotion_timeline.append({
                            "message_index": idx,
                            "emotion": emotion,
                            "original_message": message.strip()
                        })
                    break  # Only count first emotion match per message
    
    # Determine dominant and secondary emotions
    most_common = emotion_counter.most_common(2)
    
    emotional_patterns = {
        "dominant": None,
        "secondary": None,
        "all_emotions": dict(emotion_counter),
        "timeline": emotion_timeline
    }
    
    if len(most_common) >= 1:
        emotional_patterns["dominant"] = {
            "emotion": most_common[0][0],
            "count": most_common[0][1]
        }
    
    if len(most_common) >= 2:
        emotional_patterns["secondary"] = {
            "emotion": most_common[1][0],
            "count": most_common[1][1]
        }
    
    return emotional_patterns