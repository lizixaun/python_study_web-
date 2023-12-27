import aiofiles
import asyncio
async with aiofiles.open("name",mode="w",encoding="utf-8")as f:
    await f.writer()