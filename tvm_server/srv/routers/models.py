from pydantic import BaseModel


class GetMethodRequest(BaseModel):
    code: str
    data: str
    method: str
    config: str
