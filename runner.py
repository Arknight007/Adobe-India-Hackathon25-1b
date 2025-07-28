import json, os
from pathlib import Path
from extract_and_rank import extract_headings, rank_sections, extract_subsections

def process_collection(col_dir: Path):
    inp = json.loads((col_dir/"challenge1b_input.json").read_text())
    docs = inp["documents"]
    keywords = inp["persona"]["focus_keywords"]
    all_extracted, all_subs = [], []
    for d in docs:
        pdf = col_dir/"PDFs"/d["filename"]
        entries = extract_headings(str(pdf))
        top_secs = rank_sections(entries, keywords)
        subs = extract_subsections(str(pdf), top_secs)
