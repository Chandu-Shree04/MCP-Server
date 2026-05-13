"""Stakeholder Mapping Tool"""
from typing import Dict, Any, List

def map_stakeholders(stakeholders: List[Dict[str, str]], project_description: str) -> Dict[str, Any]:
    """
    Build an influence-interest matrix and per-stakeholder engagement strategy.
    
    Args:
        stakeholders: List of dicts with 'name', 'role', 'department' keys
        project_description: Description of the project
    
    Returns:
        Stakeholder map with influence-interest matrix and engagement strategies
    """
    # Categorize stakeholders into influence-interest matrix
    high_influence_high_interest = []
    high_influence_low_interest = []
    low_influence_high_interest = []
    low_influence_low_interest = []
    
    for stakeholder in stakeholders:
        role = stakeholder.get('role', '').lower()
        
        # Simple heuristic for influence and interest
        if 'director' in role or 'ceo' in role or 'vp' in role:
            influence = 'High'
        else:
            influence = 'Low'
        
        if 'project' in project_description.lower() and ('manager' in role or 'lead' in role):
            interest = 'High'
        else:
            interest = 'Low'
        
        stakeholder_data = {
            **stakeholder,
            'influence': influence,
            'interest': interest,
            'engagement_strategy': get_engagement_strategy(influence, interest)
        }
        
        if influence == 'High' and interest == 'High':
            high_influence_high_interest.append(stakeholder_data)
        elif influence == 'High' and interest == 'Low':
            high_influence_low_interest.append(stakeholder_data)
        elif influence == 'Low' and interest == 'High':
            low_influence_high_interest.append(stakeholder_data)
        else:
            low_influence_low_interest.append(stakeholder_data)
    
    return {
        'status': 'success',
        'total_stakeholders': len(stakeholders),
        'matrix': {
            'manage_closely': high_influence_high_interest,
            'keep_satisfied': high_influence_low_interest,
            'keep_informed': low_influence_high_interest,
            'monitor': low_influence_low_interest
        },
        'engagement_plan': {
            'manage_closely': 'Engage regularly, involve in decision-making',
            'keep_satisfied': 'Provide key information, meet periodically',
            'keep_informed': 'Share regular updates, provide detailed information',
            'monitor': 'Minimal engagement, provide basic information'
        },
        'message': f'Mapped {len(stakeholders)} stakeholders across influence-interest matrix'
    }

def get_engagement_strategy(influence: str, interest: str) -> str:
    """Determine engagement strategy based on influence and interest levels."""
    if influence == 'High' and interest == 'High':
        return 'Manage Closely - Engage actively in all decisions'
    elif influence == 'High' and interest == 'Low':
        return 'Keep Satisfied - Regular updates on key milestones'
    elif influence == 'Low' and interest == 'High':
        return 'Keep Informed - Share regular detailed updates'
    else:
        return 'Monitor - Provide basic information as needed'
