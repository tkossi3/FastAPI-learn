from fastapi import FastAPI
from schemas.tache import Tache

app = FastAPI(title = "API de gestion des tâches",
              description = 
              """
            Cette application permet de :
            - Lister les tâches
            - Récupérer les détails d'une tâche
            - Ajouter une tâche
            - Mettre à jour une tâche
            - Supprimer une tâche
              """)

@app.get("/taches/",
         summary="Récupérer toutes les tâches",
         description="Toutes les tâches de la BDD se retrouve dans un JSON",
         response_description="Liste de toutes les tâches au format JSON")
def getAllTaches():
    return {"message": "Fonction qui va recuperer toutes les taches."}

@app.get("/taches/{tache_id}")
def getTache(tache_id : int):
    return {"tache_id": tache_id, "message": "Détails de la tâche."}

@app.post("/taches/")
def createTache(tache: Tache):
    return {"message": "Tache recue", "tache": tache}

@app.put("/taches/{tache_id}")
def updateTache(tache_id: int, tache: Tache):
    return {"message": f"Je vais modifier la tache {tache_id}", "nouvelleValeur": tache}

@app.delete("/taches/{tache_id}")
def deleteTache(tache_id: int):
    return {"message": f"Je vais supprimer la tache {tache_id}"}