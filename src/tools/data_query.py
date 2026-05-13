"""Business Data Query Tool (NL to SQL)"""
from typing import Optional, Dict, Any

def query_business_data(question: str, schema_hint: Optional[str] = None) -> Dict[str, Any]:
    """
    Answer a business question in plain English by generating and executing SQL.
    
    Args:
        question: Plain English business question
        schema_hint: Relevant table names to focus on (optional)
    
    Returns:
        Query results with narrative interpretation
    """
    # Simple NL to SQL conversion logic
    sql_query = generate_sql_from_question(question, schema_hint)
    
    # Mock results
    results = {
        'rows': [
            {'metric': 'Sample Data 1', 'value': 100},
            {'metric': 'Sample Data 2', 'value': 250},
            {'metric': 'Sample Data 3', 'value': 175}
        ],
        'row_count': 3
    }
    
    narrative = generate_narrative(question, results)
    
    return {
        'status': 'success',
        'question': question,
        'generated_sql': sql_query,
        'schema_hint': schema_hint or 'All tables',
        'results': results,
        'row_count': results['row_count'],
        'narrative_interpretation': narrative,
        'message': f'Query executed successfully. Retrieved {results["row_count"]} rows.'
    }

def generate_sql_from_question(question: str, schema_hint: Optional[str] = None) -> str:
    """Convert natural language question to SQL query."""
    # Simple keyword matching for SQL generation
    question_lower = question.lower()
    
    if 'count' in question_lower:
        return "SELECT COUNT(*) as total FROM table_name"
    elif 'average' in question_lower or 'avg' in question_lower:
        return "SELECT AVG(column_name) as average FROM table_name"
    elif 'sum' in question_lower or 'total' in question_lower:
        return "SELECT SUM(column_name) as total FROM table_name"
    elif 'top' in question_lower or 'highest' in question_lower:
        return "SELECT * FROM table_name ORDER BY metric DESC LIMIT 10"
    else:
        return "SELECT * FROM table_name WHERE condition"

def generate_narrative(question: str, results: Dict[str, Any]) -> str:
    """Generate natural language narrative for query results."""
    row_count = results.get('row_count', 0)
    return f"""Based on the query for '{question}':

We found {row_count} relevant records. The data shows:
- Key metrics have been identified and analyzed
- Results are sorted by relevance and importance
- Sample data points are provided above

For detailed analysis, please review the full result set.
    """
