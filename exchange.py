PRICE_DATA = {
    "BTC/USD": [
        35_842_00,
        34_069_00,
        33_871_00,
        32_917_00,
    ],
    "ETH/USD": [
        2_381_00,
        2_221_00,
        2_511_00,
        2_211_00,
    ],
}


class ExchangeConnectionError(Exception):
    """custom error that is raised when an exchange is not connected."""


class Exchange:
    def __init__(self) -> None:
        self.connected = False

    def connect(self) -> None:
        print("Connecting to Crypto exchange...")
        self.connected = True

    def check_connection(self) -> None:
        if not self.connected:
            raise ExchangeConnectionError()

    def get_market_data(self, symbol: str) -> list[int]:
        self.check_connection()
        return PRICE_DATA[symbol]

    def buy(self, symbol: str, amount: int) -> None:
        self.check_connection()
        print(f"Buying amount {amount} in market {symbol}.")

    def sell(self, symbol: str, amount: int) -> None:
        self.check_connection()
        print(f"Selling amount {amount} in market {symbol}.")
