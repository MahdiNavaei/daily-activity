"""
Utility functions for daily activity tracking
"""

from datetime import datetime
from typing import List, Dict

def format_date(date: datetime) -> str:
    """Format date for display"""
    return date.strftime("%Y-%m-%d")

def get_activity_summary(activities: List[str]) -> Dict[str, int]:
    """Get summary of activity types"""
    summary = {
        "ml_development": 0,
        "data_engineering": 0,
        "research": 0,
        "infrastructure": 0
    }
    # Simple categorization logic
    for activity in activities:
        activity_lower = activity.lower()
        if any(keyword in activity_lower for keyword in ["model", "training", "inference", "llm", "rag"]):
            summary["ml_development"] += 1
        elif any(keyword in activity_lower for keyword in ["data", "etl", "pipeline", "sql"]):
            summary["data_engineering"] += 1
        elif any(keyword in activity_lower for keyword in ["experiment", "research", "benchmark", "evaluat"]):
            summary["research"] += 1
        else:
            summary["infrastructure"] += 1
    return summary


# Last updated: 2025-12-01
