import configparser
from pathlib import Path

path = Path(__file__).parent
parser = configparser.ConfigParser()
parser.read(f"{path}/urls.conf")

BTC_TOPIC_NAME: str = parser.get("TOPICNAME", "BTC_TOPIC_NAME")
ETH_TOPIC_NAME: str = parser.get("TOPICNAME", "ETHER_TOPIC_NAME")
# OTHER_TOPIC_NAME: str = parser.get("TOPICNAME", "OTHER_TOPIC_NAME")

BTC_AVERAGE_TOPIC_NAME: str = parser.get("AVERAGETOPICNAME", "BTC_AVERAGE_TOPIC_NAME")
ETH_AVERAGE_TOPIC_NAME: str = parser.get("AVERAGETOPICNAME", "ETHER_AVERAGE_TOPIC_NAME")


BTC_TOPIC_NAME: str = parser.get("TOPICNAME", "BTC_TOPIC_NAME")
ETH_TOPIC_NAME: str = parser.get("TOPICNAME", "ETHER_TOPIC_NAME")

UPBIT_URL: str = parser.get("APIURL", "UPBIT")
BITHUMB_URL: str = parser.get("APIURL", "BITHUMB")
KORBIT_URL: str = parser.get("APIURL", "KORBIT")
COINONE_URL: str = parser.get("APIURL", "COINONE")

SOCKET_UPBIT_URL: str = parser.get("SOCKETURL", "UPBIT")
SOCKET_BITHUMB_URL: str = parser.get("SOCKETURL", "BITHUMB")
SOCKET_KORBIT_URL: str = parser.get("SOCKETURL", "KORBIT")
SOCKET_COINONE_URL: str = parser.get("SOCKETURL", "COINONE")

MAXLISTSIZE: int = 10

UPBIT_BTC_REAL_TOPIC_NAME: str = parser.get(
    "REALTIMETOPICNAME", "UPBIT_BTC_REAL_TOPIC_NAME"
)
BITHUMB_BTC_REAL_TOPIC_NAME: str = parser.get(
    "REALTIMETOPICNAME", "BITHUMB_BTC_REAL_TOPIC_NAME"
)
KORBIT_BTC_REAL_TOPIC_NAME: str = parser.get(
    "REALTIMETOPICNAME", "KORBIT_BTC_REAL_TOPIC_NAME"
)
COINONE_BTC_REAL_TOPIC_NAME: str = parser.get(
    "REALTIMETOPICNAME", "COINONE_BTC_REAL_TOPIC_NAME"
)


# KAFKA
BOOTSTRAP_SERVER = parser.get("KAFKA", "bootstrap_servers")
SECURITY_PROTOCOL = parser.get("KAFKA", "security_protocol")
MAX_BATCH_SIZE: int = parser.get("KAFKA", "max_batch_size")
MAX_REQUEST_SIZE: int = parser.get("KAFKA", "max_request_size")
ARCKS = parser.get("KAFKA", "acks")
