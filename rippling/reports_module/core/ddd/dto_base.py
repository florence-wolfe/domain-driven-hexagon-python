from pydantic import BaseModel


class BaseDTO(BaseModel):
    class Config:
        use_enum_values = True
