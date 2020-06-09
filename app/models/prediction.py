from pydantic import BaseModel

class PredictionResult(BaseModel):
    label: int
    probability: list