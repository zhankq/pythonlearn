import asyncio
import aiohttp
import time

async def download_one(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as resp:
			print('Read {} from {}'.format(resp.content_length,url))

async def download_all(sites):
	tasks = [asyncio.create_task(download_one(site)) for site in sites]
	await asyncio.gather(*tasks)

def main():
	sites = [
	'https://baoku.360.cn/'    
	]
	start_time = time.perf_counter()
	asyncio.run(download_all(sites))
	end_time = time.perf_counter()
	print('Download {} sites in {} seconds'.format(len(sites),end_time-start_time))

main()