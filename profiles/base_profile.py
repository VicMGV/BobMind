from abc import ABC, abstractmethod


class BaseProfile(ABC):
    """Base class for all professional profiles"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    @abstractmethod
    def get_system_prompt(self) -> str:
        """Return the system prompt for this profile"""
        pass
    
    @abstractmethod
    def get_analysis_prompt(self, document: str, question: str) -> str:
        """Return the analysis prompt for this profile"""
        pass
    
    @abstractmethod
    def get_summary_prompt(self, document: str) -> str:
        """Return the summary prompt for this profile"""
        pass
    
    @abstractmethod
    def get_hypothesis_prompt(self, documents: list) -> str:
        """Return the hypothesis generation prompt for this profile"""
        pass

# Made with Bob
