from tkinter import filedialog, messagebox
import Fonct_generate_key as gk
from cryptography.hazmat.primitives import serialization, hashes
import os.path


def signer_une_application(file):
    chemin_de_apply = file

    if chemin_de_apply:
        extension_valide = {".exe", ".msi", ".sh", ".apk", ".deb", ".rpm", ".jar", ".dmg"}

        apply_extension = os.path.splitext(chemin_de_apply)[1]

        if apply_extension in extension_valide:
            messagebox.showinfo("Fichier sélectionné", f"Chemin du fichier : {chemin_de_apply}")
        else:
            messagebox.showwarning("Extension invalide",
                                   f"Le fichier sélectionné n'est pas une application valide (pas une extension d'application).")
            return
    else:
        return

    gk.generer_les_cles()

    with open(gk.CHEMIN_DU_CLE_PRIVEE, "rb") as f:
        cle_privee = serialization.load_pem_private_key(
            f.read(),
            password=None
        )

    with open(chemin_de_apply, "rb") as f:
        donnee = f.read()

    signature = cle_privee.sign(
        donnee,
        hashes.SHA256()
    )

    chemin_du_signature = chemin_de_apply + ".sig"
    with open(chemin_du_signature, "wb") as f:
        f.write(signature)

    messagebox.showinfo("Information", f"L'application a été signée : {chemin_du_signature}")


