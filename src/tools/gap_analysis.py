"""Gap Analysis Tool"""
from typing import Optional, Dict, Any

def perform_gap_analysis(current_state: str, future_state: str, domain: Optional[str] = None) -> Dict[str, Any]:
    """
    Compare current-state and desired future-state to produce a structured gap matrix.
    
    Args:
        current_state: Description of the as-is situation
        future_state: Description of the desired to-be state
        domain: Business domain e.g. 'finance', 'HR' (optional)
    
    Returns:
        Gap analysis matrix with prioritization and migration steps
    """
    gaps = []
    
    # Extract key phrases from both states
    current_phrases = set(current_state.lower().split())
    future_phrases = set(future_state.lower().split())
    
    # Identify gaps (things in future not in current)
    gap_phrases = future_phrases - current_phrases
    
    migration_steps = [
        'Phase 1: Assessment - Evaluate current capabilities and readiness',
        'Phase 2: Planning - Develop detailed migration roadmap',
        'Phase 3: Pilot - Test changes in controlled environment',
        'Phase 4: Full Rollout - Deploy to production',
        'Phase 5: Optimization - Monitor and optimize performance'
    ]
    
    gap_matrix = {
        'high_priority': list(gap_phrases)[:5],
        'medium_priority': list(gap_phrases)[5:10],
        'low_priority': list(gap_phrases)[10:15]
    }
    
    return {
        'status': 'success',
        'domain': domain or 'General',
        'gap_matrix': gap_matrix,
        'total_gaps': len(gap_phrases),
        'migration_steps': migration_steps,
        'estimated_effort': 'Medium',
        'estimated_timeline': '3-6 months',
        'message': f'Identified {len(gap_phrases)} gaps between current and future states'
    }
