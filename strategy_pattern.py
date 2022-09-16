from dataclasses import dataclass
import statistics
from typing import Protocol

from exchange import Exchange


class TradingStrategy(Protocol):
    def should_buy(self, prices: list[int]) -> bool:
        raise NotImplementedError()

    def should_sell(self, prices: list[int]) -> bool:
        raise NotImplementedError()


class AverageTradingStrategy(TradingStrategy):
    def should_buy(self, prices: list[int]) -> bool:
        list_window = prices[-3:]
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, prices: list[int]) -> bool:
        list_window = prices[-3:]
        return prices[-1] > statistics.mean(list_window)


class MinMaxStrategy(TradingStrategy):
    def should_buy(self, prices: list[int]) -> bool:
        return prices[-1] < 32_000_00

    def should_sell(self, prices: list[int]) -> bool:
        return prices[-1] > 33_000_00


@dataclass
class TradingBot:
    exchange: Exchange
    trading_strategy: TradingStrategy

    def run(self, symbol: str) -> None:
        prices = self.exchange.get_market_data(symbol)
        should_buy = self.trading_strategy.should_buy(prices)
        should_sell = self.trading_strategy.should_sell(prices)

        if should_buy:
            self.exchange.buy(symbol, 10)
        elif should_sell:
            self.exchange.sell(symbol, 10)
        else:
            print(f"No action needed for {symbol}.")


def main() -> None:

    exchange = Exchange()
    exchange.connect()

    trading_strategy = MinMaxStrategy()

    bot = TradingBot(exchange=exchange, trading_strategy=trading_strategy)
    bot.run("BTC/USD")


if __name__ == "__main__":
    main()
