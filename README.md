# Adobe-India-Hackathon25-1b
Submission for Adobe India Hackathon 2025 challenge 1a

[![Docker Image](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/) [![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Schema Version](https://img.shields.io/badge/schema-draft--07-orange)](sample_dataset/schema/output_schema.json)

### Overview
Advanced PDF analysis solution that processes multiple document collections and extracts relevant content based on specific personas and use cases. Multi-Collection PDF Analysis

## Project Structure
```
Challenge_1b/
├── Foundations_of_Aviation/
│   ├── PDFs/
│   │   ├── AD1.pdf
│   │   ├── AD2.pdf
│   │   └── AD3.pdf
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Technological_Adaptations/
│   ├── PDFs/
│   │   ├── AD3.pdf
│   │   └── AD4.pdf
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── WWI_Military_Applications/
│   ├── PDFs/
│   │   └── AD4.pdf
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── extract_and_rank.py     # Core extraction & ranking logic
├── runner.py               # Orchestrates each collection’s processing
├── requirements.txt
├── Dockerfile
└── README.md               # This file


````

```mermaid
graph TD
    A[Container: pdf-multi-analyzer] --> B[runner.py]
    B --> C1[Read Collection_1 Input]
    B --> C2[Read Collection_2 Input]
    B --> C3[Read Collection_3 Input]
    C1 --> D1[Extract & Rank Collection_1]
    C2 --> D2[Extract & Rank Collection_2]
    C3 --> D3[Extract & Rank Collection_3]
    D1 --> Z[Write Collection_1 Output]
    D2 --> Z[Write Collection_2 Output]
    D3 --> Z[Write Collection_3 Output]
    Z --> U[All Collections Processed]

```


---

## Collections

### Collection 1: Travel Planning
- **Challenge ID**: round_1b_002  
- **Persona**: Travel Planner  
- **Task**: Plan a 4-day trip for 10 college friends to South of France  
- **Documents**: 7 travel guides  

### Collection 2: Adobe Acrobat Learning
- **Challenge ID**: round_1b_003  
- **Persona**: HR Professional  
- **Task**: Create and manage fillable forms for onboarding and compliance  
- **Documents**: 15 Acrobat guides  

### Collection 3: Recipe Collection
- **Challenge ID**: round_1b_001  
- **Persona**: Food Contractor  
- **Task**: Prepare vegetarian buffet-style dinner menu for corporate gathering  
- **Documents**: 9 cooking guides  

---

## Input/Output Format

### Input JSON Structure
```json
{
  "challenge_info": {
    "challenge_id": "round_1b_XXX",
    "test_case_name": "specific_test_case"
  },
  "documents": [
    {
      "filename": "doc.pdf",
      "title": "Title"
    }
  ],
  "persona": {
    "role": "User Persona"
  },
  "job_to_be_done": {
    "task": "Use case description"
  }
}
```

### Output JSON Structure
 ```json
{
  "metadata": {
    "input_documents": ["list"],
    "persona": "User Persona",
    "job_to_be_done": "Task description"
  },
  "extracted_sections": [
    {
      "document": "source.pdf",
      "section_title": "Title",
      "importance_rank": 1,
      "page_number": 1
    }
  ],
  "subsection_analysis": [
    {
      "document": "source.pdf",
      "refined_text": "Content",
      "page_number": 1
    }
  ]
}
```


## Key Features

* Persona-based content analysis
* Importance ranking of extracted sections
* Multi-collection document processing
* Structured JSON output with metadata

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
