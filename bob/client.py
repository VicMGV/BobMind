import os
from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams


class BobClient:
    """Client for IBM watsonx.ai API"""
    
    def __init__(self):
        self.api_key = os.getenv("WATSONX_API_KEY")
        self.project_id = os.getenv("WATSONX_PROJECT_ID")
        self.url = os.getenv("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
        
        if not self.api_key or not self.project_id:
            raise ValueError("WATSONX_API_KEY and WATSONX_PROJECT_ID must be set in environment variables")
        
        self.credentials = {
            "url": self.url,
            "apikey": self.api_key
        }
        
        self.model_id = "ibm/granite-13b-chat-v2"
        
    def generate(self, prompt: str, max_tokens: int = 1000, temperature: float = 0.7) -> str:
        """
        Generate text using IBM watsonx.ai
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            
        Returns:
            Generated text
        """
        parameters = {
            GenParams.MAX_NEW_TOKENS: max_tokens,
            GenParams.TEMPERATURE: temperature,
            GenParams.TOP_P: 0.9,
            GenParams.TOP_K: 50
        }
        
        model = Model(
            model_id=self.model_id,
            params=parameters,
            credentials=self.credentials,
            project_id=self.project_id
        )
        
        response = model.generate_text(prompt=prompt)
        return response


# Global client instance
_client = None


def get_client() -> BobClient:
    """Get or create the global BobClient instance"""
    global _client
    if _client is None:
        _client = BobClient()
    return _client

# Made with Bob
