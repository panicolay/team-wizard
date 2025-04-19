from dataclasses import dataclass
from datetime import date, datetime
from typing import List, Optional
from enum import Enum

class ActionStatus(Enum):
    TODO = "to do"
    IN_PROGRESS = "in progress"
    DONE = "done"
    CANCELLED = "cancelled"

@dataclass
class Action:
    description: str
    owner: Optional[str] = None
    due_date: Optional[date] = None
    status: ActionStatus = ActionStatus.TODO
    topic_id: Optional[str] = None
    id: Optional[str] = None
    created_at: Optional[datetime] = None

@dataclass
class Topic:
    title: str
    summary: Optional[str] = None
    tags: List[str] = None
    meeting_id: Optional[str] = None
    actions: List[Action] = None
    id: Optional[str] = None
    created_at: Optional[datetime] = None

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.actions is None:
            self.actions = []

@dataclass
class Meeting:
    date: date
    raw_notes: str
    type: str = "dk"
    summary: Optional[str] = None
    topics: List[Topic] = None
    id: Optional[str] = None
    created_at: Optional[datetime] = None

    def __post_init__(self):
        if self.topics is None:
            self.topics = [] 