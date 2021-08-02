import asyncio
from typing import List, Optional, Union

import databases
import ormar
import sqlalchemy

database = databases.Database("postgres://DEV_USER:DEV_PASSWORD@localhost:5432/postgres")
metadata = sqlalchemy.MetaData()


async def main():
    await database.connect()
    print("Connected!")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
