import string

def remove_punctuation(text):
    """Remove punctuation from a string."""
    return text.translate(str.maketrans("", "", string.punctuation))

def clean_text(text):
    """Convert to lowercase and remove punctuation."""
    cleaned = remove_punctuation(text)
    return cleaned.lower()
