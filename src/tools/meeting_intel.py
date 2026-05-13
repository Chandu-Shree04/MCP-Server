"""Meeting Intelligence Extraction Tool"""
import re
from typing import Optional, Dict, Any, List

def extract_meeting_intelligence(transcript: str, meeting_context: Optional[str] = None) -> Dict[str, Any]:
    """
    Process a meeting transcript or notes to extract structured intelligence.
    
    Args:
        transcript: Raw meeting transcript or notes
        meeting_context: Additional context about the meeting (optional)
    
    Returns:
        Structured meeting intelligence with action items, decisions, and summary
    """
    lines = transcript.split('\n')
    
    action_items = []
    decisions = []
    open_questions = []
    
    # Extract action items
    for line in lines:
        if 'action' in line.lower() or 'todo' in line.lower() or 'task' in line.lower():
            action_items.append({
                'item': line.strip(),
                'owner': 'TBD',
                'deadline': 'TBD',
                'status': 'Open'
            })
        
        # Extract decisions
        if 'decided' in line.lower() or 'agreed' in line.lower() or 'approved' in line.lower():
            decisions.append({
                'decision': line.strip(),
                'timestamp': 'During meeting',
                'status': 'Implemented'
            })
        
        # Extract open questions
        if '?' in line:
            open_questions.append(line.strip())
    
    # Create summary
    summary = f"""Meeting Summary:
- Context: {meeting_context or 'General discussion'}
- Total participants: Unknown
- Duration: Unknown
- Key outcomes: {len(decisions)} decisions, {len(action_items)} action items
- Outstanding items: {len(open_questions)} open questions
    """
    
    return {
        'status': 'success',
        'summary': summary,
        'action_items': action_items[:10],
        'total_action_items': len(action_items),
        'decisions': decisions[:10],
        'total_decisions': len(decisions),
        'open_questions': open_questions[:5],
        'total_questions': len(open_questions),
        'meeting_context': meeting_context or 'Not provided',
        'message': f'Extracted {len(action_items)} action items, {len(decisions)} decisions, and {len(open_questions)} open questions'
    }
