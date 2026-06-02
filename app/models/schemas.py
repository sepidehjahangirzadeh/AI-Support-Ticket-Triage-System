"""
Support Triaging Engine
 
Author: Sepideh Jahangirzadeh
"""

from enum import Enum
from typing import List
from pydantic import BaseModel, Field

class Department(str, Enum):

    """
    Supported support ticket departments.
    """
    TECHNICAL = "فنی و باگ"
    BILLING = "مالی و فاکتور"
    SALES = "فروش و ارتقا"
    COMPLAINT = "شکایات"

class TicketAnalysis(BaseModel):

    """
    Structured support ticket analysis schema.
    """
    
    department: Department = Field(..., description="The most appropriate department for this ticket")
    summary_en: str = Field(..., description="Concise English summary in max 2 sentences")
    urgency_level: int = Field(..., ge=1, le=5, description="1 is low, 5 is critical")
    detected_bugs: List[str] = Field(default_factory=list, description="List of system components that are bugged")
