import aiosqlite
import asyncio
from config import DB


async def db_connection():
    async with aiosqlite.connect(DB) as db:
        print("Success connection")
        async with db.execute('drop table testTABLE;'):
            print('Droped')
        async with db.execute('''create table testTABLE(
                                  id integer primary key autoincrement,
                                  name text(20) not null
                                  );''') as cursor:
            await db.commit()



async def main():
    tast = asyncio.create_task(db_connection())
    await tast


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())