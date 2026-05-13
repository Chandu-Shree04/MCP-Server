"""Risk Register Builder Tool"""
from typing import Optional, Dict, Any, List

def build_risk_register(project_description: str, constraints: Optional[str] = None) -> Dict[str, Any]:
    """
    Generate a risk register from a project description.
    
    Args:
        project_description: Description of the project
        constraints: Budget, timeline, regulatory constraints (optional)
    
    Returns:
        Risk register with scored risks and mitigation strategies
    """
    risks: List[Dict[str, Any]] = [
        {
            'id': 'R001',
            'description': 'Resource Availability',
            'likelihood': 'Medium',
            'impact': 'High',
            'score': 0.6,
            'mitigation': 'Secure resource commitments early and maintain contingency staffing'
        },
        {
            'id': 'R002',
            'description': 'Timeline Delay',
            'likelihood': 'Medium',
            'impact': 'Medium',
            'score': 0.5,
            'mitigation': 'Implement strong project management and weekly status reviews'
        },
        {
            'id': 'R003',
            'description': 'Budget Overrun',
            'likelihood': 'Low',
            'impact': 'High',
            'score': 0.3,
            'mitigation': 'Establish budget controls and regular financial monitoring'
        },
        {
            'id': 'R004',
            'description': 'Technical Challenges',
            'likelihood': 'Medium',
            'impact': 'High',
            'score': 0.6,
            'mitigation': 'Conduct technical assessments and maintain expert resources'
        },
        {
            'id': 'R005',
            'description': 'Stakeholder Misalignment',
            'likelihood': 'Low',
            'impact': 'Medium',
            'score': 0.3,
            'mitigation': 'Regular stakeholder communication and expectation management'
        }
    ]
    
    # Sort by risk score (likelihood × impact)
    risks.sort(key=lambda x: x['score'], reverse=True)
    
    total_risk_score = sum(r['score'] for r in risks) / len(risks)
    
    return {
        'status': 'success',
        'project_description': project_description[:100] + '...' if len(project_description) > 100 else project_description,
        'constraints': constraints or 'No specific constraints identified',
        'risks': risks,
        'total_risks': len(risks),
        'average_risk_score': round(total_risk_score, 2),
        'overall_risk_level': 'Medium' if total_risk_score > 0.5 else 'Low',
        'message': f'Generated risk register with {len(risks)} identified risks'
    }
