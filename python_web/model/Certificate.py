from pydantic import BaseModel


class Certificate(BaseModel):
    title: str
    body: str
    url_icon: str
    url_pdf: str
