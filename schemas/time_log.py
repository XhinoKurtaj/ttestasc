
from datetime import date 

from pydantic import BaseModel
from typing import List, Optional


class TimeLogBase(BaseModel):
    full_date       :   date
    start_time      :   str
    end_time        :   str
    description     :   Optional[str] = None
    project         :   str
    tags            :   Optional[List[str]] = None


class CreateTimeLog(CommentBase):
    pass

class TimeLogDB(CommentBase):
    id      :   int



class TimeLogDBBase(TimeLogBase):
    id      :   int

    class Config:
        orm_mode    =   True