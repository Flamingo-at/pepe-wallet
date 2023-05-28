import asyncio

from loguru import logger
from random import choice
from aiohttp import ClientSession
from string import ascii_lowercase


async def worker():
    while True:
        try:
            async with ClientSession() as client:

                data = ''.join(choice(ascii_lowercase) for _ in range(12))

                logger.info('Registration')

                response = await client.post('https://pewall.org/mobileAppAPI/signup.php',
                    data={
                        'email':f'{data}@gmail.com',
                        'username':data,
                        'password':data,
                        'referral_code':ref,
                        'first_name':'',
                        'last_name':'',
                        'phone_number':'',
                        'language':'en'
                    })
                if (await response.json())['status'] != 'success':
                    raise

        except:
            logger.error('Error')

        else:
            logger.success('Successfully')

        finally:
            await asyncio.sleep(delay)


async def main():
    tasks = [asyncio.create_task(worker()) for _ in range(1)]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    print("Bot Pepe wallet @flamingoat\n")

    ref = input('Ref code: ')
    delay = int(input('Delay(sec): '))

    asyncio.run(main())
