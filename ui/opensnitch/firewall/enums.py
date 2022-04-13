from opensnitch.utils import Enums
from opensnitch.config import Config

class Verdicts(Enums):
    EMPTY = ""
    ACCEPT = Config.ACTION_ACCEPT
    DROP = Config.ACTION_DROP
    REJECT = Config.ACTION_REJECT
    RETURN = Config.ACTION_RETURN
    STOP = Config.ACTION_STOP

class Policy(Enums):
    ACCEPT = "accept"
    DROP = "drop"

class Table(Enums):
    FILTER = "filter"
    MANGLE = "mangle"
    NAT = "nat"

class Hooks(Enums):
    INPUT  ="input"
    OUTPUT  ="output"
    FORWARD = "forward"
    PREROUTING = "prerouting"
    POSTROUTING = "postrouting"

class Family(Enums):
    INET = "inet"
    IPv4 = "ip"
    IPv6 = "ip6"

class ChainType(Enums):
    FILTER = "filter"
    MANGLE = "mangle"
    ROUTE = "route"
    SNAT = "snat"
    DNAT = "dnat"

class Operator(Enums):
    EQUAL = "=="
    NOT_EQUAL = "!="
    GT_THAN = ">="
    GT = ">"
    LT_THAN = "<="
    LT = "<"

class Statements(Enums):
    """Enum of known (allowed) statements:
        [tcp,udp,ip] ...
    """

    TCP = "tcp"
    UDP = "udp"
    UDPLITE = "udplite"
    SCTP = "sctp"
    DCCP = "dccp"
    ICMP = "icmp"
    SPORT = "sport"
    DPORT = "dport"

    IP = "ip"
    IIFNAME = "iifname"
    OIFNAME = "oifname"
