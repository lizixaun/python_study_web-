import aiohttp
import asyncio
urls={

}
async def download(url):
    name=1
    async with aiohttp.ClientSession as session:
        async with session.get(url) as resp:
            with open(name,mode="wb")as f :
                f.write(await resp.content.read())
async def main():
    task=[]
    for url in urls:
        b=asyncio.create_task(download(url))
        task.append(b)
    await asyncio.wait(task)
if __name__ == '__main__':
    # asyncio.run(main())
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())