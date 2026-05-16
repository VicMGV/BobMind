from bob.client import get_client
from profiles import PROFILES


def analyze_document(profile_name: str, document_text: str, question: str) -> dict:
    """
    Analyze a document using a specific profile.
    
    Args:
        profile_name: Name of the profile to use
        document_text: Document content
        question: Question to answer
        
    Returns:
        Dictionary with analysis results
    """
    if profile_name not in PROFILES:
        raise ValueError(f"Unknown profile: {profile_name}. Available profiles: {list(PROFILES.keys())}")
    
    profile = PROFILES[profile_name]
    client = get_client()
    
    # Build the prompt
    system_prompt = profile.get_system_prompt()
    analysis_prompt = profile.get_analysis_prompt(document_text, question)
    
    full_prompt = f"{system_prompt}\n\n{analysis_prompt}"
    
    # Generate response
    analysis = client.generate(full_prompt, max_tokens=1500, temperature=0.7)
    
    return {
        "analysis": analysis,
        "profile": profile_name,
        "question": question
    }


def summarize_document(profile_name: str, document_text: str) -> dict:
    """
    Summarize a document using a specific profile.
    
    Args:
        profile_name: Name of the profile to use
        document_text: Document content
        
    Returns:
        Dictionary with summary results
    """
    if profile_name not in PROFILES:
        raise ValueError(f"Unknown profile: {profile_name}. Available profiles: {list(PROFILES.keys())}")
    
    profile = PROFILES[profile_name]
    client = get_client()
    
    # Build the prompt
    system_prompt = profile.get_system_prompt()
    summary_prompt = profile.get_summary_prompt(document_text)
    
    full_prompt = f"{system_prompt}\n\n{summary_prompt}"
    
    # Generate response
    summary = client.generate(full_prompt, max_tokens=1000, temperature=0.5)
    
    return {
        "summary": summary,
        "profile": profile_name
    }


def generate_hypothesis(profile_name: str, documents: list) -> dict:
    """
    Generate hypotheses from multiple documents using a specific profile.
    
    Args:
        profile_name: Name of the profile to use
        documents: List of document texts
        
    Returns:
        Dictionary with hypothesis results
    """
    if profile_name not in PROFILES:
        raise ValueError(f"Unknown profile: {profile_name}. Available profiles: {list(PROFILES.keys())}")
    
    profile = PROFILES[profile_name]
    client = get_client()
    
    # Build the prompt
    system_prompt = profile.get_system_prompt()
    hypothesis_prompt = profile.get_hypothesis_prompt(documents)
    
    full_prompt = f"{system_prompt}\n\n{hypothesis_prompt}"
    
    # Generate response
    hypothesis = client.generate(full_prompt, max_tokens=2000, temperature=0.8)
    
    return {
        "hypothesis": hypothesis,
        "profile": profile_name,
        "documents_count": len(documents)
    }

# Made with Bob
