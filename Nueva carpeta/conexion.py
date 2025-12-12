import os 
from dotenv import load_dotenv
from supabase import create_client

class ConexionBD:
    def __init__(self):
        load_dotenv()

    def conexionSupabase(self):
        url = os.getenv('SUPABASE_URL')
        apikey = os.getenv('SUPABASE_APIKEY')
        supabase = create_client(url, apikey)
        return supabase
    
