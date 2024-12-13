from typing import TypedDict, Literal

class DataType(TypedDict):
    mode: Literal["indoor", "outdoor"]
    timestamp: int
    temp: float
    moist: float

class TableType(TypedDict):
    temp: list
    moist: list
    averageTemp: float
    averageMoist: float