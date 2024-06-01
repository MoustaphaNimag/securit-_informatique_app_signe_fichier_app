from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives import serialization, hashes
import Fonct_generate_key as gk
import os.path


def verifier_signature(file):
    chemin_du_fichier = file
    if not chemin_du_fichier:
        messagebox.showwarning("Aucun fichier", "Aucun fichier n'a été sélectionné.")
        return

    chemin_du_signature = chemin_du_fichier + ".sig"

    if not os.path.exists(chemin_du_signature):
        messagebox.showwarning("Erreur", "ce fichier n'est pas signé")
        return

    # Charger la clé publique
    with open(gk.CHEMIN_DU_CLE_PUBLIQUE, "rb") as f:
        cle_publique = serialization.load_pem_public_key(
            f.read()
        )

    # Lire le fichier à vérifier
    with open(chemin_du_fichier, "rb") as f:
        donnee = f.read()

    # Lire la signature
    with open(chemin_du_signature, "rb") as f:
        signature = f.read()

    try:
        # bloc pour vérifier la signature
        cle_publique.verify(
            signature,
            donnee,
            hashes.SHA256()
        )
        messagebox.showinfo("Information", "La signature est valide.")
    except Exception as e:
        messagebox.showerror("Erreur", "La signature est invalide.")
