"""Bien sûr ! Voici les **trois consignes** détaillées et optimisées pour la création des fonctions de gestion de session, en reprenant les objectifs que nous avons définis.

---

## 🔒 Consignes de l'Exercice : Gestion de Session Utilisateur (`is_login`)

L'exercice consiste à développer trois fonctions distinctes en Python pour gérer l'état de connexion d'un utilisateur, en utilisant la clé de session (ou cookie) nommée **`'is_login'`**.

### 1. Consigne : Vérification de l'Existence de la Session

Créez une fonction nommée **`check_session_existence(session_name)`** dont le rôle est de confirmer la présence physique du mécanisme de session.

* **Entrée :** Une chaîne de caractères représentant le nom de la session (ex. : `'is_login'`).
* **Action :** Parcourez le contexte de la requête simulée (par exemple, un dictionnaire représentant les cookies entrants) pour déterminer si la clé de session est présente.
* **Sortie :** Un **booléen** :
    * `True` si la session/clé `'is_login'` est trouvée.
    * `False` si elle est absente.

---

### 2. Consigne : Validation et Extraction des Données Utilisateur

Créez une fonction nommée **`get_validated_session_data(session_name, session_content)`** qui est responsable de l'extraction sécurisée des informations de l'utilisateur.

* **Entrées :**
    1.  Le nom de la session (`'is_login'`).
    2.  Le contenu brut de cette session (simulé comme une chaîne de caractères ou un objet décodable).
* **Format de Contenu Attendu :** Le contenu doit être vérifié pour s'assurer qu'il correspond à la structure sécurisée suivante après décodage :
    $$\text{contenu} = \{'is\_login': [\text{ID\_utilisateur}, \text{'rôle\_utilisateur'}]\}$$
* **Actions :**
    1.  Tenter de décoder le `session_content` (ex. : gérer les erreurs de décodage si le contenu est corrompu).
    2.  Vérifier rigoureusement que le format obtenu correspond à la structure attendue (dictionnaire, clé `'is_login'`, valeur étant une liste de deux éléments).
* **Sortie :**
    * Si la validation est un succès : Une liste contenant exactement deux éléments : **`[ID_utilisateur, 'rôle_utilisateur']`**.
    * Si la validation échoue (format incorrect, données manquantes ou corrompues) : **`None`**.

---

### 3. Consigne : Destruction de la Session (Déconnexion)

Créez une fonction nommée **`destroy_session(session_name)`** qui simule la déconnexion de l'utilisateur.

* **Entrée :** Une chaîne de caractères représentant le nom de la session à supprimer (`'is_login'`).
* **Action :** Mettre en œuvre le mécanisme standard de déconnexion basé sur les cookies :
    * L'action doit générer l'instruction qui ordonne au navigateur de supprimer le cookie `session_name`.
    * Ceci est réalisé en définissant la durée de vie (`Max-Age` ou `Expires`) du cookie à **zéro (0)** ou à une date déjà passée.
* **Sortie :** Un **booléen** indiquant le succès de l'opération :
    * `True` si l'instruction de destruction (l'en-tête de réponse `Set-Cookie` avec l'expiration à 0) est générée.
    * `False` en cas de problème (si l'opération ne peut pas être effectuée)."""