import random
import string
from uuid import uuid4


def generate_nickname() -> str:
    """
    Generate a random nickname in the format: adjective_animal_number.
    Example: gentle_fox_813

    Returns:
        str: Randomly generated nickname.
    """
    adjectives = ["gentle", "brave", "quick", "happy", "bold"]
    animals = ["fox", "koala", "eagle", "lion", "tiger"]
    number = random.randint(100, 999)
    return f"{random.choice(adjectives)}_{random.choice(animals)}_{number}"


async def generate_unique_nickname(session) -> str:
    """
    Generate a unique nickname that does not exist in the database.

    Args:
        session (AsyncSession): Database session for querying existing nicknames.

    Returns:
        str: Unique nickname.
    """
    for _ in range(10):  # Retry up to 10 times
        nickname = generate_nickname()
        existing_user = await session.execute(
            select(User).filter_by(nickname=nickname)
        )
        if not existing_user.scalar():  # No conflict in the database
            return nickname
    # Fallback to UUID if all retries fail
    return f"user_{uuid4().hex[:8]}"
