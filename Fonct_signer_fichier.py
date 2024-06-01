from tkinter import filedialog, messagebox
import Fonct_generate_key as gk
from cryptography.hazmat.primitives import serialization, hashes
import os.path

def signer_un_fichier(file):
    # Demander à l'utilisateur de sélectionner un fichier à signer
    chemin_du_fichier = file

    if chemin_du_fichier:
        # Vérifier si l'extension du fichier est valide
            extension_invalide = {".exe", ".msi", ".sh", ".apk", ".deb", ".rpm", ".jar", ".dmg"}
            fichier_extension = os.path.splitext(chemin_du_fichier)[1]
            
            if fichier_extension in extension_invalide:
                messagebox.showerror("Extension invalide", "Les fichiers avec les extensions suivantes ne sont pas valides : .exe, .msi, .sh, .apk, .deb, .rpm, .jar, .dmg")
                return
            else:
                messagebox.showinfo("Fichier sélectionné", f"Chemin du fichier : {chemin_du_fichier}")
    else:
        return

    # j'ai utilisé la fonction generer_les_cles definie dans la page Fonct_generate_key.py
    gk.verifier_si_les_cles_existe()

    # Charger la clé privée
    with open(gk.CHEMIN_DU_CLE_PRIVEE, "rb") as f:
        cle_privee = serialization.load_pem_private_key(
            f.read(),
            password=None
        )

    # Lire le fichier à signer
    with open(chemin_du_fichier, "rb") as f:
        donnee = f.read()

    # Signature en utilisant SHA-256
    signature = cle_privee.sign(
        donnee,
        hashes.SHA256()
    )

    # Sauvegarder la signature dans un fichier .sig
    chemin_du_signature = chemin_du_fichier + ".sig"
    with open(chemin_du_signature, "wb") as f:
        f.write(signature)

    # Informer l'utilisateur que le fichier a été signé
    messagebox.showinfo("Information", f"Le fichier a été signé : {chemin_du_signature}")

