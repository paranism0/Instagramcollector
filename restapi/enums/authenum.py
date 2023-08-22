from enum import Enum

class resulttype:
    OK = "SUCCESS"
    FAIL = "FAILED"

class resultmsg(Enum):
    SUCCESS = "User successfully created"
    DUPLICATE = "User with this email or username already exists"
    ERROR = "There is an error with your request"