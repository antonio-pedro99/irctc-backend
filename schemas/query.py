from datetime import datetime
from optparse import Option
from typing import Optional
from pydantic import BaseModel

# Shared properties
class SearchQueryBase(BaseModel):
    dt_departure:Optional[str] = datetime.now()
    dt_arrival:Optional[str]
    dt_duration:Optional[int]


