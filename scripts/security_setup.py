# Ce fichier ne fait que documenter les étapes à faire dans MongoDB Atlas :
"""
1. Connecte-toi à https://cloud.mongodb.com/
2. Crée un cluster gratuit.
3. Va dans Database Access > Add New Database User
   - Username : projetRH
   - Password : à définir
   - Role : ReadWrite sur la base 'rh_management'
4. Ajoute ton IP à Network Access > IP Whitelist
5. Remplis la variable MONGO_ATLAS_URI dans .env
"""
