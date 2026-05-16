import io
from typing import Union


def load_document(filename: str, file_bytes: bytes) -> str:
    """
    Load document content from bytes based on file extension.
    
    Args:
        filename: Name of the file
        file_bytes: File content as bytes
        
    Returns:
        Document text content
        
    Raises:
        ValueError: If file type is not supported
    """
    file_extension = filename.lower().split('.')[-1]
    
    if file_extension == 'txt':
        return file_bytes.decode('utf-8')
    
    elif file_extension == 'pdf':
        try:
            import PyPDF2
            pdf_file = io.BytesIO(file_bytes)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
            return text
        except ImportError:
            raise ValueError("PyPDF2 is required to process PDF files. Install it with: pip install PyPDF2")
    
    elif file_extension in ['doc', 'docx']:
        try:
            import docx
            doc_file = io.BytesIO(file_bytes)
            doc = docx.Document(doc_file)
            text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
            return text
        except ImportError:
            raise ValueError("python-docx is required to process Word files. Install it with: pip install python-docx")
    
    elif file_extension == 'md':
        return file_bytes.decode('utf-8')
    
    else:
        raise ValueError(f"Unsupported file type: {file_extension}. Supported types: txt, pdf, doc, docx, md")
