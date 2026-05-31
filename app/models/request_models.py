from pydantic import BaseModel


class FitnessRequest(BaseModel):
    city: str
    activity: str