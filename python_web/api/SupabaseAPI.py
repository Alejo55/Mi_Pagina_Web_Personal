import os
import dotenv
from supabase import create_client, Client


class SupabaseAPI:
    # Busca var de entorno de mi environment y las mete en mi entorno, y si tengo un fichero .dotenv tmbn la app las situara como var de entorno
    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        self.supabase: Client = None

    def create_client(self):
        if self.supabase is None:
            self.supabase = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    def cert(self) -> list:
        if self.supabase is None:
            self.create_client()

        response = self.supabase.table("certificates").select("*").execute()

        certificates_data = []

        # Si los datos que obtengo son mayores que 0, entonces existen y puedo trabajar con ellos
        if len(response.data) > 0:
            for cert_item in response.data:
                certificates_data.append(cert_item)

        return certificates_data
