import string
from dataclasses import dataclass
from enum import Enum


class Resource(Enum):
    COAL = 1
    OIL = 2
    GARBAGE = 3
    URANIUM = 4

class PlayerColor(Enum):
    RED = 1
    YELLOW = 2
    BLUE = 3
    GREEN = 4
    PURPLE = 5
    BLACK = 6

class PhaseStatus(Enum):
    PhaseContinues = 1
    PhaseEnds = 2
    GameEnds = 3

class GamePhase(Enum):
    DeterminePlayerOrder = 0 # UML diagram doesn't have it, temporarily kept for consistency with game rules
    AuctionPowerPlants = 1
    BuyResources = 2
    BuyHouses = 3
    Bureaucracy = 4
    GameEnd = 5

@dataclass
class PowerPlantNumber:
    number: int

@dataclass
class PowerPlant:
    number: PowerPlantNumber
    acceptedResources: list[Resource]
    resourceAmount: int
    numberOfCities: int

@dataclass
class RequestError:
    description: str

@dataclass
class SerializedGameState:
    state: str