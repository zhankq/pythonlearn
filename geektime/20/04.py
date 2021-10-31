import asyncio

s  = []
async def worker_1(a):
	print('worker_1 start')
	await asyncio.sleep(3)
	print('worker_1 done')
	s.append(a)

async def  worker_2(a):
	print('worker_2 start')
	await asyncio.sleep(2)
	print('worker_2 done')
	s.append(a)

async def main():
	print("before await")
	await worker_1()
	print('awaited worker_1')
	await worker_2()
	print('awaited worker_2')

#asyncio.run(main())
async def main2():
	task1 = asyncio.create_task(worker_1(1))
	task2 = asyncio.create_task(worker_2(2))
	print('before await')
	await task1
	print('awaited worker_1')
	await task2
	print('awaited worker_2')

asyncio.run(main2())

print(s)
