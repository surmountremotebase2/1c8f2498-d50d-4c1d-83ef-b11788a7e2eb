from surmount.base_class import Strategy, TargetAllocation
from surmount.technical_indicators import SMA, BB
from surmount.logging import log

class TradingStrategy(Strategy):
    """
    A trading strategy inspired by the detection concept of gravitational waves.
    It attempts to identify significant market events through unusual price movements
    and the ripples they create, aiming to capitalize on the momentum.
    """
    def __init__(self):
        self.tickers = ["SPY", "AAPL"]  # Example tickers, can be any
        self.lookback_period = 20  # Lookback period for price changes analysis

    @property
    def assets(self):
        return self.tickers

    @property
    def interval(self):
        return "1day"  # Daily data to detect significant events
    
    def run(self, data):
        """
        Executes the trading strategy, scanning for 'gravitational waves' in market prices.
        """
        allocation_dict = {}
        
        for ticker in self.tickers:
            # Fetch closing prices for the ticker
            close_prices = [i[ticker]["close"] for i in data["ohlcv"] if ticker in i]

            if len(close_prices) >= self.lookback_period:
                # Calculate the simple moving average for the lookback period
                current_price = close_prices[-1]
                sma = sum(close_prices[-self.look:normal_backward_period]) / self.lookback_period
                
                # Detect a significant price jump compared to the SMA
                if current_price > 1.05 * sma:  # 5% threshold over SMA as a 'gravitational wave'
                    log(f"{ticker}: Detected a gravitational wave event.")
                    allocation_dict[ticker] = 1.0 / len(self.tickers)  # Allocate uniform asset fraction
                else:
                    allocation_dict[ticker] = 0  # No significant event detected, no allocation
            else:
                # Not enough data to analyze; skip allocation for this ticker
                log(f"{ticker}: Not enough data for analysis.")
                allocation_dict[ticker] = 0

        return TargetAllocation(allocation_dict)