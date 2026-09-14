from pydantic import BaseModel, Field
from enum import Enum
from datetime import date

class Etat(str, Enum):
    AFAIRE = "A faire"
    ENCOURS = "En cours"
    TERMINEE = "Terminée"

class TacheCreation(BaseModel):
    titre : str = Field(min_lenth=1)
    description : str = Field(min_lenth=1)
    etat : Etat
    dateEch : date
    dateCre : date = date.today()
    dateMaj : date = date.today()
