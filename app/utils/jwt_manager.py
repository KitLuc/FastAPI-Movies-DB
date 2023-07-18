from jwt import encode, decode

__KEY = "Narnia"

def create_token(data: dict) -> str:
    token: str = encode(payload=data, key=f"{__KEY}", algorithm="HS256")
    return token


def validate_token(token: str) -> dict:
    data: dict = decode(token, key=f"{__KEY}", algorithms=["HS256"])
    return data
