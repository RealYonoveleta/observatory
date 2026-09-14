import asyncio
import aiofiles
from polymarket import AsyncPublicClient
from datetime import datetime

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

DATASETS_DIR = Path(os.getenv("DATASETS_DIR"))

async def ingest_from_polymarket(target, output_path=None) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    output_path = (
        DATASETS_DIR / "raw" / "polymarket" / f"{target}_snapshot_{timestamp}.jsonl"
        if output_path is None else output_path
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    method_name = f"list_{target}"

    async with AsyncPublicClient() as client:
        try:
            method = getattr(client, method_name)

        except AttributeError:
            print(f"Error: Polymarket client doesn't contain method {method_name}")

        pages = method(closed=False)

        async for page in pages:
            for element in page.items:
                element_dict = element.model_dump_json()

                async with aiofiles.open(output_path, mode="a", encoding="utf-8") as f:
                    await f.write(element_dict + '\n')
               
    
markets = asyncio.run(ingest_from_polymarket("markets"))