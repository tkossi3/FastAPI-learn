from pydantic import BaseModel, Field
from enum import Enum
from datetime import date

class Etat(str, Enum):
    AFAIRE = "A faire"
    ENCOURS = "En cours"
    TERMINEE = "Terminée"

class TacheMiseAJour(BaseModel):
    titre : str = Field(min_lenth=1)
    description : str = Field(min_lenth=1)
    etat : Etat
    dateEch : date
    dateMaj : date = date.today()
