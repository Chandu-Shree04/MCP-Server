# BA Copilot MCP Server

Business Analysis Copilot powered by Model Context Protocol (MCP). This server provides comprehensive tools for business analysis, requirements management, risk assessment, and data insights.

## Features

### 1. **Requirements Analyzer**
- Parse and validate business requirements documents
- Categorize requirements by type
- Calculate completeness scores
- Identify ambiguities and missing acceptance criteria

### 2. **Gap Analyzer**
- Compare current-state and future-state systems
- Produce structured gap matrices with prioritization
- Generate migration step recommendations
- Support domain-specific analysis (finance, HR, etc.)

### 3. **Risk Register Builder**
- Generate comprehensive risk registers
- Score risks by likelihood × impact
- Provide mitigation strategies for each risk
- Support constraint-based risk assessment

### 4. **Stakeholder Mapper**
- Build influence-interest matrices
- Categorize stakeholders into engagement groups
- Generate per-stakeholder engagement strategies
- Support cross-functional analysis

### 5. **Meeting Intelligence**
- Extract action items from meeting transcripts
- Identify key decisions and open questions
- Generate structured meeting summaries
- Track action item owners and deadlines

### 6. **Business Data Query**
- Convert natural language questions to SQL
- Execute queries against connected database
- Return results with narrative interpretation
- Support schema hints for focused queries

## Installation

```bash
# Clone the repository
git clone https://github.com/Chandu-Shree04/MCP-Server.git
cd MCP-Server

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Running the Server

```bash
python src/index.py
```

The server will start on stdio transport and be ready to handle MCP requests.

### Example Tool Calls

#### Requirements Analysis
```python
analyze_requirements(
    content="As a user, I shall login with credentials. Acceptance criteria: Valid credentials accepted.",
    project_context="Authentication module for web application"
)
```

#### Gap Analysis
```python
perform_gap_analysis(
    current_state="Manual HR processes, spreadsheet-based",
    future_state="Integrated HRIS system with automation",
    domain="HR"
)
```

#### Risk Register
```python
build_risk_register(
    project_description="Cloud migration project for enterprise",
    constraints="Budget: $500k, Timeline: 6 months, Regulatory compliance required"
)
```

#### Stakeholder Mapping
```python
map_stakeholders(
    stakeholders=[
        {"name": "John Doe", "role": "Director", "department": "IT"},
        {"name": "Jane Smith", "role": "Project Manager", "department": "Operations"}
    ],
    project_description="Cloud infrastructure modernization"
)
```

#### Meeting Intelligence
```python
extract_meeting_intelligence(
    transcript="John: We need to finalize requirements by Friday. Action: Mary to compile list.",
    meeting_context="Project kickoff meeting"
)
```

#### Data Query
```python
query_business_data(
    question="What is the total revenue by region for Q1?",
    schema_hint="sales, revenue tables"
)
```

## Project Structure

```
MCP-Server/
├── src/
│   ├── index.py                 # Main server entry point
│   └── tools/
│       ├── __init__.py
│       ├── requirements.py      # Requirements analysis tool
│       ├── gap_analysis.py      # Gap analysis tool
│       ├── risk_register.py     # Risk register builder
│       ├── stakeholder_map.py   # Stakeholder mapper
│       ├── meeting_intel.py     # Meeting intelligence extraction
│       └── data_query.py        # Business data query tool
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Dependencies

- `mcp`: Model Context Protocol SDK
- Python 3.8+

## Configuration

Edit `src/index.py` to configure:
- Server name and version
- Tool parameters and descriptions
- Transport mechanism (currently stdio)

## API Documentation

Each tool accepts specific parameters and returns structured JSON responses. See tool docstrings in `src/tools/` for detailed parameter specifications.

## Logging

The server uses Python's standard logging module. Configure log levels in `src/index.py`.

## Contributing

Feel free to submit issues and enhancement requests!

## License

MIT License

## Author

Chandu-Shree04
