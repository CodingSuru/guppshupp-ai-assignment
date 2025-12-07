import random
from .templates import get_personality_template

def apply_personality(neutral_response, style):
    """
    Transform a neutral response into a specific personality style.
    
    Args:
        neutral_response (str): The base neutral response
        style (str): The personality style to apply
        
    Returns:
        str: The transformed response with personality
    """
    template = get_personality_template(style)
    
    # Split neutral response into sentences
    sentences = neutral_response.split('. ')
    sentences = [s.strip() for s in sentences if s.strip()]
    
    # Build the personality-infused response
    transformed_parts = []
    
    # Add prefix
    transformed_parts.append(template["prefix"])
    
    # Transform each sentence
    for i, sentence in enumerate(sentences):
        # Add tone marker for some sentences
        if i == 0 and template["tone_markers"]:
            marker = random.choice(template["tone_markers"])
            transformed_parts.append(f"{marker} {sentence}.")
        else:
            transformed_parts.append(f"{sentence}.")
    
    # Add encouragement randomly
    if template["encouragement"] and random.random() > 0.5:
        encouragement = random.choice(template["encouragement"])
        transformed_parts.append(encouragement)
    
    # Add suffix
    transformed_parts.append(template["suffix"])
    
    # Join all parts
    final_response = " ".join(transformed_parts)
    
    return final_response

def generate_all_personalities(neutral_response):
    """
    Generate responses for all available personality styles.
    
    Args:
        neutral_response (str): The base neutral response
        
    Returns:
        dict: Dictionary with all personality-styled responses
    """
    from .templates import PERSONALITIES
    
    responses = {
        "neutral": neutral_response
    }
    
    for style in PERSONALITIES.keys():
        responses[style] = apply_personality(neutral_response, style)
    
    return responses