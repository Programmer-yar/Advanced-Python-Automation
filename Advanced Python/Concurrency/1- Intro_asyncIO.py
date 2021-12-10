"""
Syntax:
async def - introduces a coroutine or asynchronous generator
await     - passes function control back to event loop
""" 

import asyncio

async def count():
	print('one')
	await asyncio.sleep(1)
	print('Two')

async def main():
	""" event loop or coordinator:
	calls each count function and when it reaches "await" It returns the control
	back to event loop"""
	await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
	asyncio.run(main())