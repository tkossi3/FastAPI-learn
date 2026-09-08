from pydantic import BaseModel, Field
from enum import Enum

class Etat(str, Enum):
    AFAIRE = "A faire"
    ENCOURS = "En cours"
    TERMINEE = "Terminée"

class Tache(BaseModel):
    titre : str = Field(min_lenth=1)
    description : str = Field(min_lenth=1)
    etat : Etat

