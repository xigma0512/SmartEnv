from typing import TypedDict, Literal, Dict

class DataType(TypedDict):
    timestamp: int
    temp: float
    moist: float
    PM25: int
    PM10: int

class Table(TypedDict):
    temp: list
    moist: list
    PM25: list
    PM10: list
    
class AverageRecord(TypedDict):
    hour: int
    temp: float
    moist: float
    PM25: float
    PM25: float

type History = Dict[str, list[AverageRecord]]