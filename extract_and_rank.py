import fitz        
import re
from typing import List, Dict

def extract_headings(pdf_path: str) -> List[Dict]:
    ...

def rank_sections(entries: List[Dict], keywords: List[str], top_k: int=5) -> List[Dict]:
    ...

def extract_subsections(pdf_path: str, sections: List[Dict]) -> List[Dict]:
    ...
