# Adobe-India-Hackathon25-1b
[![Docker Image](https://img.shields.io/badge/docker-ready-blue)](https://www.docker.com/) [![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE) [![Schema Version](https://img.shields.io/badge/schema-draft--07-orange)](sample_dataset/schema/output_schema.json)
### Submission for Adobe India Hackathon 2025 challenge 1a

## Overview
Advanced PDF analysis solution that processes multiple document collections and extracts relevant content based on specific personas and use cases. Multi-Collection PDF Analysis

## Project Structure
```

Challenge\_1b/
├── Collection\_1/                    # Travel Planning
│   ├── PDFs/                        # South of France guides
│   ├── challenge1b\_input.json      # Input configuration
│   └── challenge1b\_output.json     # Analysis results
├── Collection\_2/                    # Adobe Acrobat Learning
│   ├── PDFs/                        # Acrobat tutorials
│   ├── challenge1b\_input.json      # Input configuration
│   └── challenge1b\_output.json     # Analysis results
├── Collection\_3/                    # Recipe Collection
│   ├── PDFs/                        # Cooking guides
│   ├── challenge1b\_input.json      # Input configuration
│   └── challenge1b\_output.json     # Analysis results
└── README.md                        # This file

````

```mermaid
flowchart TD
  subgraph Container
    A[Docker Container<br/>(pdf-multi-analyzer)] 
    A --> B[runner.py]
  end

  B --> C1[Read Collection_1 Input<br/>(challenge1b_input.json)]
  B --> C2[Read Collection_2 Input<br/>(challenge1b_input.json)]
  B --> C3[Read Collection_3 Input<br/>(challenge1b_input.json)]

  subgraph Coll1 [Collection_1<br/>(Travel Planning)]
    C1 --> P1[Load PDFs from PDFs/]
    P1 --> E1[extract_and_rank.py]
    E1 --> H1[extract_headings()] 
    H1 --> R1[rank_sections()] 
    R1 --> S1[extract_subsections()] 
    S1 --> O1[Write challenge1b_output.json]
  end

  subgraph Coll2 [Collection_2<br/>(Adobe Acrobat Learning)]
    C2 --> P2[Load PDFs from PDFs/]
    P2 --> E2[extract_and_rank.py]
    E2 --> H2[extract_headings()] 
    H2 --> R2[rank_sections()] 
    R2 --> S2[extract_subsections()] 
    S2 --> O2[Write challenge1b_output.json]
  end

  subgraph Coll3 [Collection_3<br/>(Recipe Collection)]
    C3 --> P3[Load PDFs from PDFs/]
    P3 --> E3[extract_and_rank.py]
    E3 --> H3[extract_headings()] 
    H3 --> R3[rank_sections()] 
    R3 --> S3[extract_subsections()] 
    S3 --> O3[Write challenge1b_output.json]
  end

  O1 --> Z[Completion]
  O2 --> Z
  O3 --> Z

  Z --> U[Output JSON files ready in each collection folder]
```

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


## Key Features

* Persona-based content analysis
* Importance ranking of extracted sections
* Multi-collection document processing
* Structured JSON output with metadata

## Extensibility

* Integrate OCR (Tesseract + pdf2image) for scanned documents
* Use regex or machine-learning techniques to detect numbered headings
* Parameterize font-size thresholds for multi-language support


## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
