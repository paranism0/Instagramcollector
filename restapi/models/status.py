from dataclasses import dataclass
from ..enums.authenum import resultmsg , resulttype

@dataclass
class msgstatus:
    status : resulttype
    msg : resultmsg