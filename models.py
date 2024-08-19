from pydantic import BaseModel, Field
from typing import Literal, Optional

class ModelInput(BaseModel):
    age: int = Field(..., ge=0, description="Age of the client")
    job: str = Field(..., description="Job title of the client")
    marital: Literal['married', 'single', 'divorced'] = Field(..., description="Marital status of the client")
    education: Literal['primary', 'secondary', 'tertiary', 'unknown'] = Field(..., description="Level of education of the client")
    default: Literal['yes', 'no'] = Field(..., description="Has credit in default?")
    balance: int = Field(..., description="Account balance")
    housing: Literal['yes', 'no'] = Field(..., description="Has housing loan?")
    loan: Literal['yes', 'no'] = Field(..., description="Has personal loan?")
    contact: Literal['cellular', 'telephone', 'unknown'] = Field(..., description="Contact communication type")
    day: int = Field(..., ge=1, le=31, description="Last contact day of the month")
    month: Literal['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'] = Field(..., description="Last contact month of year")
    duration: int = Field(..., ge=0, description="Last contact duration in seconds")
    campaign: int = Field(..., ge=0, description="Number of contacts performed during this campaign")
    pdays: int = Field(..., description="Number of days since the client was last contacted from a previous campaign (-1 means client was not previously contacted)")
    previous: int = Field(..., ge=0, description="Number of contacts performed before this campaign")
    poutcome: Literal['unknown', 'failure', 'success', 'other'] = Field(..., description="Outcome of the previous marketing campaign")
