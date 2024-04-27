from pydantic import BaseModel


class Taiwan(BaseModel):
    cities: list[str]
