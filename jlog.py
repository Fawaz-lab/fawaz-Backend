from typing import Any, Dict, Tuple
import json
import http.cookies
from jugopy import jugoRoute, jugoRender, jugoRedirect, jugoGetCookie, jugoParsePost, jugoCrypt, jugoRun, jugoDispatch, runSql

COOKIE_NAME = 'is_login'
COOKIE_MAX_AGE = 3600

def generate_set_cookie_header(name: str, content: Any, max_age: int = COOKIE_MAX_AGE) -> Tuple[str, str]:
    val = json.dumps(content) if isinstance(content, (dict, list)) else str(content)
    
    cookies = http.cookies.SimpleCookie()
    cookies[name] = val
    
    cookies[name]['max-age'] = max_age
    cookies[name]['path'] = '/'
    cookies[name]['httponly'] = True 
    
    header_value = cookies.output(header='')[1:].strip()
    return ('Set-Cookie', header_value)

def handle_register(environ: Dict, startResponse: Any, form_data: Dict) -> Any:
    username = form_data.get('username', '').strip()
    email = form_data.get('email', '').strip()
    password = form_data.get('password', '')
    confirm_password = form_data.get('confirm_password', '')

    if not username or not email or not password or not confirm_password:
        return jugoRender('register.html', {'title': 'ColloDev | Register', 'error': "Veuillez remplir tous les champs."}, startResponse)
    
    if password != confirm_password:
        return jugoRender('register.html', {'title': 'ColloDev | Register', 'error': "Les mots de passe ne correspondent pas."}, startResponse)
        
    pre_existing_user = runSql("SELECT id FROM user WHERE email=%s OR username=%s", (email, username))
    
    if not pre_existing_user:
        return jugoRender('register.html', {'title': 'ColloDev | Register', 'error': "Erreur: Ce compte n'a pas été pré-enregistré par l'administrateur."}, startResponse)
    
    user_id = pre_existing_user[0]['id']
    
    existing_connection = runSql("SELECT id FROM connexion WHERE user_id=%s", (user_id,))
    
    if existing_connection:
        return jugoRender('register.html', {'title': 'ColloDev | Register', 'error': "Ce compte a déjà été activé. Veuillez vous connecter."}, startResponse)
        
    hashed_password = jugoCrypt(password) 

    create_account = runSql("INSERT INTO connexion (user_id, mot_de_passe_hash) VALUES (%s, %s)", (user_id, hashed_password))
    
    if create_account is not None:
        return jugoRedirect('/login', startResponse)
    else:
        return jugoRender('register.html', {'title': 'ColloDev | Register', 'error': "Erreur lors de l'activation du compte. Veuillez réessayer."}, startResponse)

def handle_login(environ: Dict, startResponse: Any, form_data: Dict) -> Any:
    identifier = form_data.get('identifier', '')
    password = form_data.get('password', '')

    if not identifier or not password:
        return jugoRender('login.html', {'title': 'ColloDev | Login', 'error': "Veuillez remplir tous les champs."}, startResponse)
    
    user = runSql("SELECT id, role_id FROM user WHERE email=%s OR username=%s", (identifier, identifier))
    
    error_message = "Identifiant ou mot de passe invalide."
    
    if user:
        user_id = user[0]['id']
        role_id = user[0]['role_id']
        user_password = runSql("SELECT mot_de_passe_hash FROM connexion WHERE user_id=%s", (user_id))
        
        if not user_password:
            return jugoRender('login.html', {'title': 'ColloDev | Login', 'error': error_message}, startResponse)

        password_db = user_password[0]['mot_de_passe_hash']
        
        if jugoCrypt(password) == password_db: 
            
            cookie_data = {'is_login': [user_id, 'user', role_id]}
            set_cookie_header = generate_set_cookie_header(COOKIE_NAME, cookie_data)
            
            status = '302 Found' 
            headers = [
                ('Location', '/'),
                set_cookie_header
            ]
            
            startResponse(status, headers)
            return [b'']
            
        else:
            return jugoRender('login.html', {'title': 'ColloDev | Login', 'error': error_message}, startResponse)
    else:
        return jugoRender('login.html', {'title': 'ColloDev | Login', 'error': error_message}, startResponse)
