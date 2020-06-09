from pydantic import BaseModel

class RequestPayload(BaseModel):
    feature1: float
    feature2: float