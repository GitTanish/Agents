from phi.tools.tool import Tool
from pycoingecko import CoinGeckoAPI

# Map popular crypto symbols to CoinGecko IDs
SYMBOL_TO_ID = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana",
    "DOGE": "dogecoin",
    "XRP": "ripple",
    "ADA": "cardano",
    "BNB": "binancecoin",
}

class CoinGeckoTool(Tool):
    type: str = "tool"
    name: str = "crypto_tool"
    description: str = "Get current crypto price and market data using CoinGecko."

    def run(self, coin_id: str = "bitcoin"):
        cg = CoinGeckoAPI()
        coin_id = SYMBOL_TO_ID.get(coin_id.upper(), coin_id.lower())  # map symbol to ID

        try:
            data = cg.get_coin_by_id(id=coin_id)
            market_data = data.get("market_data", {})

            return {
                "name": data.get("name"),
                "symbol": data.get("symbol").upper(),
                "current_price_usd": market_data.get("current_price", {}).get("usd", "N/A"),
                "market_cap_usd": market_data.get("market_cap", {}).get("usd", "N/A"),
                "volume_usd": market_data.get("total_volume", {}).get("usd", "N/A"),
                "price_change_24h_pct": market_data.get("price_change_percentage_24h", "N/A"),
            }
        except Exception as e:
            return {"error": f"Failed to get data for '{coin_id}': {str(e)}"}
