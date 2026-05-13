from mcp.server import Server
from mcp.server.stdio import StdioServerTransport
from typing import Optional, List, Dict, Any
import asyncio
import logging

from tools.requirements import analyze_requirements
from tools.gap_analysis import perform_gap_analysis
from tools.risk_register import build_risk_register
from tools.stakeholder_map import map_stakeholders
from tools.meeting_intel import extract_meeting_intelligence
from tools.data_query import query_business_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize MCP Server
server = Server("ba-copilot")


# Tool 1 — Requirements Analyzer
@server.tool()
def analyze_requirements(
    content: str,
    project_context: Optional[str] = None
) -> Dict[str, Any]:
    """
    Parse and validate a business requirements document. Returns categorized requirements, 
    completeness score, ambiguity flags, and missing acceptance criteria.
    
    Args:
        content: Raw BRD text or user story block
        project_context: Brief project background (optional)
    
    Returns:
        Analyzed requirements with categorization and completeness score
    """
    return analyze_requirements(content, project_context)


# Tool 2 — Gap Analyser
@server.tool()
def perform_gap_analysis(
    current_state: str,
    future_state: str,
    domain: Optional[str] = None
) -> Dict[str, Any]:
    """
    Compare current-state and desired future-state to produce a structured gap matrix 
    with prioritization and suggested migration steps.
    
    Args:
        current_state: Description of the as-is situation
        future_state: Description of the desired to-be state
        domain: Business domain e.g. 'finance', 'HR' (optional)
    
    Returns:
        Gap analysis matrix with prioritization and migration steps
    """
    return perform_gap_analysis(current_state, future_state, domain)


# Tool 3 — Risk Register Builder
@server.tool()
def build_risk_register(
    project_description: str,
    constraints: Optional[str] = None
) -> Dict[str, Any]:
    """
    Generate a risk register from a project description. Each risk is scored by 
    likelihood × impact and paired with a mitigation strategy.
    
    Args:
        project_description: Description of the project
        constraints: Budget, timeline, regulatory constraints (optional)
    
    Returns:
        Risk register with scored risks and mitigation strategies
    """
    return build_risk_register(project_description, constraints)


# Tool 4 — Stakeholder Mapper
@server.tool()
def map_stakeholders(
    stakeholders: List[Dict[str, str]],
    project_description: str
) -> Dict[str, Any]:
    """
    Build an influence-interest matrix and per-stakeholder engagement strategy 
    from a list of people and roles.
    
    Args:
        stakeholders: List of dicts with 'name', 'role', 'department' keys
        project_description: Description of the project
    
    Returns:
        Stakeholder map with influence-interest matrix and engagement strategies
    """
    return map_stakeholders(stakeholders, project_description)


# Tool 5 — Meeting Intelligence
@server.tool()
def extract_meeting_intelligence(
    transcript: str,
    meeting_context: Optional[str] = None
) -> Dict[str, Any]:
    """
    Process a meeting transcript or notes. Returns structured action items 
    (with owners and deadlines), key decisions, open questions, and a summary.
    
    Args:
        transcript: Raw meeting transcript or notes
        meeting_context: Additional context about the meeting (optional)
    
    Returns:
        Structured meeting intelligence with action items, decisions, and summary
    """
    return extract_meeting_intelligence(transcript, meeting_context)


# Tool 6 — Data Insights (NL → SQL)
@server.tool()
def query_business_data(
    question: str,
    schema_hint: Optional[str] = None
) -> Dict[str, Any]:
    """
    Answer a business question in plain English. Generates SQL, executes it 
    against the connected database, and returns the result with a narrative interpretation.
    
    Args:
        question: Plain English business question
        schema_hint: Relevant table names to focus on (optional)
    
    Returns:
        Query results with narrative interpretation
    """
    return query_business_data(question, schema_hint)


async def main():
    """Main entry point for the MCP server"""
    transport = StdioServerTransport()
    await server.connect(transport)
    logger.error("BA Copilot MCP server running")


if __name__ == "__main__":
    asyncio.run(main())
