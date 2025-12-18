import os from openai import OpenAI from dotenv import load_dotenv from schema import DocumentAnalysis

load_dotenv()

class AIEngine: def init(self): self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) self.model = "gpt-4o-mini"

async def analyze_document(self, content: str) -> DocumentAnalysis:
    """
    Uses OpenAI Structured Outputs to parse unstructured text into 
    the Pydantic-validated DocumentAnalysis schema.
    """
    response = self.client.beta.chat.completions.parse(
        model=self.model,
        messages=[
            {"role": "system", "content": "You are a professional data analyst. Extract structured insights from the provided document."},
            {"role": "user", "content": content}
        ],
        response_format=DocumentAnalysis,
    )
    return response.choices[0].message.parsed