import re

FACT_KEYWORDS = {
    "name": [
        r"\bmy name is ([A-Z][a-zA-Z]+(?:\s[A-Z][a-zA-Z]+)*)",
        r"\bi am ([A-Z][a-zA-Z]+(?:\s[A-Z][a-zA-Z]+)*)",
        r"\bi'm ([A-Z][a-zA-Z]+(?:\s[A-Z][a-zA-Z]+)*)",
        r"\bcall me ([A-Z][a-zA-Z]+)",
        r"\bknown as ([A-Z][a-zA-Z]+)",
        r"\bpeople call me ([A-Z][a-zA-Z]+)"
    ],
    "age": [
        r"\bi am (\d{1,2})\s*(?:years old|yrs old|yo|year old)?\b",
        r"\bi'm (\d{1,2})\s*(?:years old|yrs old|yo|year old)?\b",
        r"\bmy age is (\d{1,2})\b",
        r"\bturning (\d{1,2})\b",
        r"\b(\d{1,2})\s*years old\b"
    ],
    "location": [
        r"\bi live in ([A-Z][a-zA-Z\s]+)",
        r"\bfrom ([A-Z][a-zA-Z\s]+)",
        r"\bin ([A-Z][a-zA-Z\s]+),\s*(?:India|USA|UK|Canada|Australia)",
        r"\bresiding in ([A-Z][a-zA-Z\s]+)",
        r"\bbased in ([A-Z][a-zA-Z\s]+)",
        r"\bborn in ([A-Z][a-zA-Z\s]+)"
    ],
    "education": [
        r"\bi study ([A-Za-z\s]+)",
        r"\bi am studying ([A-Za-z\s]+)",
        r"\bi'm studying ([A-Za-z\s]+)",
        r"\b(BCA|MCA|MBA|B\.Tech|M\.Tech|BSc|MSc|BA|MA|BTech|MTech|BE|ME|PhD)\b",
        r"\benrolled in ([A-Za-z\s]+)",
        r"\bpursuing ([A-Za-z\s]+)",
        r"\bmajoring in ([A-Za-z\s]+)"
    ],
    "work": [
        r"\bi work (?:as|at)\s+([A-Za-z\s]+)",
        r"\bmy job is ([A-Za-z\s]+)",
        r"\bi am a ([A-Za-z\s]+?)(?:\.|,|\n|$)",
        r"\bi'm a ([A-Za-z\s]+?)(?:\.|,|\n|$)",
        r"\bworking as ([A-Za-z\s]+)",
        r"\bemployed at ([A-Za-z\s]+)",
        r"\bmy profession is ([A-Za-z\s]+)"
    ],
    "email": [
        r"\b([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})\b"
    ],
    "phone": [
        r"\b(?:\+91[-\s]?)?(\d{10})\b",
        r"\b(\d{3}[-\s]?\d{3}[-\s]?\d{4})\b"
    ],
    "admission_number": [
        r"\b(\d{2}[A-Z]{2,6}\d{6,10})\b",
        r"\badmission (?:number|no|id) is (\w+)\b",
        r"\broll (?:number|no) is (\w+)\b"
    ],
    "university": [
        r"\bat ([A-Z][a-zA-Z\s]+ University)",
        r"\bstudying at ([A-Z][a-zA-Z\s]+)",
        r"\bfrom ([A-Z][a-zA-Z\s]+ (?:University|College|Institute))"
    ],
    "skills": [
        r"\bi know ([A-Za-z\s,]+(?:programming|coding|development))",
        r"\bskilled in ([A-Za-z\s,]+)",
        r"\bgood at ([A-Za-z\s,]+)",
        r"\bexpert in ([A-Za-z\s,]+)"
    ]
}

def extract_facts(messages):
    """
    Extract factual information about the user from messages.
    Returns a dictionary of facts with evidence.
    """
    facts = {}
    
    for idx, message in enumerate(messages, start=1):
        msg = message.strip()
        if not msg:
            continue
            
        for fact_type, patterns in FACT_KEYWORDS.items():
            for pattern in patterns:
                match = re.search(pattern, msg, re.IGNORECASE)
                if match:
                    # Extract the captured group if available
                    if match.groups():
                        value = match.group(1).strip()
                    else:
                        value = match.group(0).strip()
                    
                    # Clean up the value
                    value = re.sub(r'\s+', ' ', value)
                    
                    # Only store if meaningful (length > 2)
                    if len(value) > 2:
                        if fact_type not in facts:
                            facts[fact_type] = {
                                "value": value,
                                "message_index": idx,
                                "original_message": message.strip(),
                                "confidence": 0.85
                            }
                        else:
                            # If duplicate, increase confidence
                            if facts[fact_type]["value"].lower() == value.lower():
                                facts[fact_type]["confidence"] = min(0.95, facts[fact_type]["confidence"] + 0.05)
                        break  # Only first match per fact type
    
    return facts