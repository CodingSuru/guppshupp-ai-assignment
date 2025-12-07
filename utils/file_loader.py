import os

def load_messages(file_path):
    """
    Load messages from a text file.
    Each line in the file is treated as one message.
    
    Args:
        file_path (str): Path to the message file
        
    Returns:
        list: List of message strings
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Message file not found: {file_path}")
    
    with open(file_path, "r", encoding="utf-8") as file:
        messages = file.readlines()
    
    # Clean up messages: remove empty lines and strip whitespace
    messages = [msg.strip() for msg in messages if msg.strip()]
    
    return messages

def save_output(data, file_path):
    """
    Save output data to a file.
    
    Args:
        data (str): Data to save
        file_path (str): Destination file path
    """
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(data)
    
    print(f"✓ Output saved to {file_path}")