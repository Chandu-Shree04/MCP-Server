"""Requirements Analysis Tool"""
from typing import Optional, Dict, Any
import re

def analyze_requirements(content: str, project_context: Optional[str] = None) -> Dict[str, Any]:
    """
    Parse and validate a business requirements document.
    
    Args:
        content: Raw BRD text or user story block
        project_context: Brief project background (optional)
    
    Returns:
        Analyzed requirements with categorization and completeness score
    """
    lines = content.split('\n')
    requirements = []
    ambiguities = []
    
    # Identify functional requirements
    functional_reqs = [line for line in lines if 'shall' in line.lower() or 'must' in line.lower()]
    
    # Identify ambiguous statements
    ambiguous_keywords = ['may', 'could', 'might', 'should', 'nice to have']
    for line in lines:
        if any(keyword in line.lower() for keyword in ambiguous_keywords):
            ambiguities.append(line.strip())
    
    # Calculate completeness score
    has_acceptance_criteria = 'acceptance' in content.lower() or 'criteria' in content.lower()
    has_user_stories = 'as a' in content.lower() or 'as an' in content.lower()
    has_constraints = 'constraint' in content.lower() or 'limitation' in content.lower()
    
    completeness_score = sum([
        has_acceptance_criteria,
        has_user_stories,
        has_constraints,
        len(functional_reqs) > 0
    ]) / 4 * 100
    
    requirements = {
        'functional': functional_reqs[:10],
        'count': len(functional_reqs),
        'context': project_context or 'No context provided'
    }
    
    missing_items = []
    if not has_acceptance_criteria:
        missing_items.append('Acceptance Criteria')
    if not has_constraints:
        missing_items.append('Constraints')
    if not has_user_stories:
        missing_items.append('User Stories Format')
    
    return {
        'status': 'success',
        'requirements': requirements,
        'completeness_score': round(completeness_score, 2),
        'ambiguity_flags': ambiguities[:5],
        'missing_items': missing_items,
        'total_requirements': len(functional_reqs),
        'message': f'Analyzed {len(functional_reqs)} requirements with {round(completeness_score, 2)}% completeness'
    }
