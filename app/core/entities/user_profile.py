from dataclasses import dataclass

@dataclass
class UserEntity:
    name:str
    surname:str
    email:str
    phone_number:int
    password:str
    