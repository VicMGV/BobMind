from profiles.base_profile import BaseProfile


class DoctorProfile(BaseProfile):
    """Medical professional profile for analyzing medical documents"""
    
    def __init__(self):
        super().__init__(
            name="Doctor",
            description="Medical professional specialized in analyzing medical documents, research papers, and patient data"
        )
    
    def get_system_prompt(self) -> str:
        return """You are an experienced medical doctor with expertise in analyzing medical documents, 
research papers, clinical trials, and patient data. You provide accurate, evidence-based medical insights 
while maintaining professional medical standards."""
    
    def get_analysis_prompt(self, document: str, question: str) -> str:
        return f"""As a medical professional, analyze the following document and answer the question.

Document:
{document}

Question: {question}

Provide a detailed medical analysis with:
1. Key medical findings
2. Clinical significance
3. Evidence-based recommendations
4. Any relevant medical considerations"""
    
    def get_summary_prompt(self, document: str) -> str:
        return f"""As a medical professional, provide a comprehensive summary of this medical document.

Document:
{document}

Include:
1. Main medical findings
2. Clinical implications
3. Key recommendations
4. Important medical terminology explained"""
    
    def get_hypothesis_prompt(self, documents: list) -> str:
        docs_text = "\n\n---\n\n".join([f"Document {i+1}:\n{doc}" for i, doc in enumerate(documents)])
        return f"""As a medical professional, analyze these medical documents and generate research hypotheses.

{docs_text}

Based on these documents, provide:
1. Key patterns or trends identified
2. Potential research hypotheses
3. Clinical implications
4. Suggested areas for further investigation"""

# Made with Bob
