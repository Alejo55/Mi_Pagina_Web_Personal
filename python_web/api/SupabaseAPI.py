import os
import dotenv
from supabase import create_client, Client
from python_web.model.Certificate import Certificate


class SupabaseAPI:
    # Busca var de entorno de mi environment y las mete en mi entorno, y si tengo un fichero .dotenv tmbn la app las situara como var de entorno
    dotenv.load_dotenv()

    SUPABASE_URL = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

    def __init__(self) -> None:
        if self.SUPABASE_URL != None and self.SUPABASE_KEY != None:
            self.supabase: Client = create_client(self.SUPABASE_URL, self.SUPABASE_KEY)

    def cert(self) -> list[Certificate]:
        response = (
            self.supabase.table("certificates")
            .select("*")
            .order(column="init_date", desc=True)
            .execute()
        )

        certificates_data = []

        # Si los datos que obtengo son mayores que 0, entonces existen y puedo trabajar con ellos
        if len(response.data) > 0:
            for cert_item in response.data:
                certificates_data.append(
                    Certificate(
                        title=cert_item["title"],
                        body=cert_item["body"],
                        url_icon=cert_item["url_icon"],
                        url_pdf=cert_item["url_pdf"],
                    )
                )

        return certificates_data
