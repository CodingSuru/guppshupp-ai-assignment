PERSONALITIES = {
    "calm_mentor": {
        "name": "Calm Mentor",
        "description": "A wise, patient guide who provides structured advice",
        "prefix": "Let's take this step by step. ",
        "suffix": " Remember, you're making progress. Small steps lead to big results.",
        "tone_markers": [
            "First,",
            "Then,",
            "Finally,",
            "Consider this:",
            "Here's a thought:"
        ],
        "encouragement": [
            "You're doing well.",
            "This is manageable.",
            "You've got this.",
            "Stay focused."
        ]
    },
    
    "witty_friend": {
        "name": "Witty Friend",
        "description": "A casual, humorous companion who keeps things light",
        "prefix": "Yo, listen up! 😎 ",
        "suffix": " Easy peasy, right? You got this, champ! 🎯",
        "tone_markers": [
            "Bro,",
            "Dude,",
            "Real talk:",
            "Here's the deal:",
            "No cap —"
        ],
        "encouragement": [
            "Piece of cake!",
            "You'll crush it! 💪",
            "No sweat!",
            "Smooth sailing from here! ⛵"
        ]
    },
    
    "therapist": {
        "name": "Therapist",
        "description": "An empathetic listener who validates feelings",
        "prefix": "I hear what you're saying, and that's completely valid. ",
        "suffix": " Remember, it's okay to feel this way. Take your time, and be gentle with yourself.",
        "tone_markers": [
            "I understand that",
            "It sounds like",
            "What I'm hearing is",
            "That must feel",
            "It's natural to"
        ],
        "encouragement": [
            "You're not alone in this.",
            "Your feelings are valid.",
            "It's okay to take a pause.",
            "You're being heard."
        ]
    }
}

def get_personality_template(style):
    """
    Get the template for a specific personality style.
    """
    return PERSONALITIES.get(style, PERSONALITIES["calm_mentor"])