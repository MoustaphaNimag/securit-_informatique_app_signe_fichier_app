import os.path
from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import serialization



# Generer les cles public et prive

CHEMIN_DU_CLE_PRIVEE = "clé_privee.pem"
CHEMIN_DU_CLE_PUBLIQUE = "clé_publique.pem"

def generer_les_cles():
    cle_privee = dsa.generate_private_key(key_size=2048)

    with open(CHEMIN_DU_CLE_PRIVEE, "wb") as f:
        f.write(cle_privee.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))

    cle_publique = cle_privee.public_key()

    with open(CHEMIN_DU_CLE_PUBLIQUE,"wb") as f:
        f.write(cle_publique.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def verifier_si_les_cles_existe():
    if not os.path.exists(CHEMIN_DU_CLE_PRIVEE) or not os.path.exists(CHEMIN_DU_CLE_PUBLIQUE):
        generer_les_cles()

