import re

PREFERENCE_KEYWORDS = {
    "likes": [
        r"\bi (?:like|love|enjoy|adore|appreciate|am into|dig)\b",
        r"\bmy (?:favourite|favorite)\b",
        r"\bi'm (?:into|fond of)\b",
        r"\bi prefer\b",
        r"\bmy hobby\b",
        r"\bi really like\b",
        r"\bi'm passionate about\b",
        r"\bi'm interested in\b",
        r"\bi can't get enough of\b",
        r"\bi'm a fan of\b",
        r"\bi'm crazy about\b"
    ],
    "dislikes": [
        r"\bi (?:hate|dislike|don't like|do not like|can't stand|despise)\b",
        r"\bnot a fan of\b",
        r"\bi'm not into\b",
        r"\bi avoid\b",
        r"\bi'm not interested in\b",
        r"\bi don't enjoy\b",
        r"\bi'm not keen on\b"
    ],
    "goals": [
        r"\bi want to\b",
        r"\bmy goal (?:is|was)\b",
        r"\bi wish to\b",
        r"\bi dream of\b",
        r"\bmy dream is\b",
        r"\bplanning to\b",
        r"\baiming to\b",
        r"\bi aspire to\b",
        r"\bi hope to\b",
        r"\bi'm working towards\b",
        r"\bi intend to\b",
        r"\bmy ambition is\b",
        r"\bi'm determined to\b",
        r"\bi'm going to\b"
    ]
}

def extract_preferences(messages):
    """
    Extract user preferences from messages using keyword matching.
    Returns a dictionary with likes, dislikes, and goals.
    """
    preferences = {
        "likes": [],
        "dislikes": [],
        "goals": []
    }
    
    for idx, message in enumerate(messages, start=1):
        msg = message.strip().lower()
        if not msg:
            continue
            
        for category, patterns in PREFERENCE_KEYWORDS.items():
            for pattern in patterns:
                match = re.search(pattern, msg, re.IGNORECASE)
                if match:
                    # Extract the rest of the sentence after the keyword
                    start_pos = match.end()
                    rest = msg[start_pos:].strip()
                    
                    # Clean up: take until punctuation or end
                    rest = re.split(r'[.,;!?\n]', rest)[0].strip()
                    
                    # Remove common connecting words at start
                    rest = re.sub(r'^(?:that|to|the|a|an)\s+', '', rest)
                    
                    if rest and len(rest) > 3:  # Only meaningful extractions
                        preferences[category].append({
                            "value": rest,
                            "message_index": idx,
                            "original_message": message.strip()
                        })
                    break  # Only match first pattern per message
    
    # Remove duplicates while preserving order
    for category in preferences:
        seen = set()
        unique = []
        for item in preferences[category]:
            if item["value"] not in seen:
                seen.add(item["value"])
                unique.append(item)
        preferences[category] = unique
    
    return preferences