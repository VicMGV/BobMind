import re


def clean_text(text: str) -> str:
    """
    Clean and normalize document text.
    
    Args:
        text: Raw text content
        
    Returns:
        Cleaned text
    """
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters but keep punctuation
    text = re.sub(r'[^\w\s.,!?;:()\-\'"]+', '', text)
    
    # Normalize line breaks
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    
    # Remove multiple consecutive newlines
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text


def extract_keywords(text: str, max_keywords: int = 10) -> list:
    """
    Extract keywords from text (simple implementation).
    
    Args:
        text: Document text
        max_keywords: Maximum number of keywords to extract
        
    Returns:
        List of keywords
    """
    # Simple keyword extraction based on word frequency
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    
    # Common stop words to exclude
    stop_words = {'that', 'this', 'with', 'from', 'have', 'been', 'were', 
                  'their', 'there', 'would', 'could', 'should', 'about'}
    
    # Filter stop words
    words = [w for w in words if w not in stop_words]
    
    # Count frequency
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency and return top keywords
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, freq in sorted_words[:max_keywords]]

# Made with Bob
