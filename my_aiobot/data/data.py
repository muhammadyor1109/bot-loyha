import aiosqlite
import asyncio

async def create_sessions_table():
    async with aiosqlite.connect("data/session_storage.db") as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                user_id INTEGER PRIMARY KEY,
                lang TEXT
            )
        """)
        await db.commit()

# Dastur ishga tushganda chaqirish uchun
if __name__ == "__main__":
    asyncio.run(create_sessions_table())
