import re

def clean_text(text):
    """
    Clean and normalize text.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Cleaned text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text

def normalize_text(text):
    """
    Normalize text for comparison and matching.
    
    Args:
        text (str): Input text
        
    Returns:
        str: Normalized text (lowercase, no extra spaces)
    """
    text = clean_text(text)
    text = text.lower()
    return text

def remove_special_characters(text, keep_spaces=True):
    """
    Remove special characters from text.
    
    Args:
        text (str): Input text
        keep_spaces (bool): Whether to keep spaces
        
    Returns:
        str: Text without special characters
    """
    if keep_spaces:
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)
    else:
        return re.sub(r'[^a-zA-Z0-9]', '', text)
