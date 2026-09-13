import asyncio

from obs_platform.ingestion.kalshi.adapter import KalshiIngestor
from obs_platform.ingestion.polymarket.adapter import PolymarketIngestor


def test_polymarket_list_markets():
    ingestor = PolymarketIngestor()
    markets = asyncio.run(ingestor.list_markets())
    assert markets[0].id == "pm-1"


def test_kalshi_list_markets():
    ingestor = KalshiIngestor()
    markets = asyncio.run(ingestor.list_markets())
    assert markets[0].id == "kal-1"
