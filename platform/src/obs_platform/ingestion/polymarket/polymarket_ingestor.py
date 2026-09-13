import asyncio
from polymarket import AsyncPublicClient

import os
from pathlib import Path
from dotenv import load_dotenv
import json

load_dotenv()

DATASETS_DIR = Path(os.getenv("DATASETS_DIR"))

async def main() -> list:
    markets_list = []

    async with AsyncPublicClient() as client:

        pages = client.list_markets(closed=False)
        
        async for page in pages:
            for market in page.items:
                markets_list.append(market.model_dump())
        
    return markets_list 

       
markets = asyncio.run(main())

output_path = DATASETS_DIR / "raw" / "polymarket" / "markets.json"

output_path.parent.mkdir(parents=True, exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(markets, f, indent=4, default=str)