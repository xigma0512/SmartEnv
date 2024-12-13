from typing import TypedDict, Literal, Dict

class DataType(TypedDict):
    mode: Literal["indoor", "outdoor"]
    timestamp: int
    temp: float
    moist: float

class Table(TypedDict):
    temp: list
    moist: list
    
class AverageRecord(TypedDict):
    hour: int
    temp: float
    moist: float

type History = Dict[str, list[AverageRecord]]