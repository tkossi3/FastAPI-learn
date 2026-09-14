const API_BASE = "http://localhost:8000/taches/"


// GET - Toutes les taches

async function donneTaches(){
    try {
        const response = await fetch(`${API_BASE}`)
        if (!response.ok) {
            throw new Error(`Erreur HTTP - Status : ${response.status}`)
        }
        const data = await response.json
        return data
    } catch (error) {
        console.error(error)
    }
}

// GET - Une tache à partir de son id
// POST - Créer une nouvel tache
// PUT - Mettre à jour une tache
// DELETE - Supprimer une tache