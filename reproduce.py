import asyncio
from typing import List, Optional, Union

import databases
import ormar
import sqlalchemy

database = databases.Database("postgres://DEV_USER:DEV_PASSWORD@localhost:5432/postgres")
metadata = sqlalchemy.MetaData()


class Author(ormar.Model):
    class Meta:
        tablename = "authors"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    first_name: str = ormar.String(max_length=80)
    last_name: str = ormar.String(max_length=80)


class Category(ormar.Model):
    class Meta:
        tablename = "categories"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=40)


class Post(ormar.Model):
    class Meta:
        tablename = "posts"
        database = database
        metadata = metadata

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=200)
    categories: Optional[List[Category]] = ormar.ManyToMany(Category)
    author: Optional[Author] = ormar.ForeignKey(Author)


async def main():
    await database.connect()
    print("Connected!")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
