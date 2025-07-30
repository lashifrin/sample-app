"""User Manager Module

Manages users in the system. Provides methods to create, read, update, and delete users.
"""

from typing import Optional
from dataclasses import dataclass, field
import abc

@dataclass
class User:
    """User class

    Represents a user in the system.
    """

    id: int
    name: str
    email: str
    password: Optional[str] = None

class AbstractUserManager:
    """Abstract User Manager

    Defines the contract for user manager classes.
    """
    @abc.abstractmethod
    async def create_user(self, user: User) -> User:
        pass

    @abc.abstractmethod
    async def read_user(self, user_id: int) -> Optional[User]:
        pass

    @abc.abstractmethod
    async def update_user(self, user_id: int, updated_user: User) -> bool:
        pass

    @abc.abstractmethod
    async def delete_user(self, user_id: int) -> bool:
        pass

class InMemoryUserManager(AbstractUserManager):
    """In-memory User Manager

    Stores users in memory.
    """
    _users = field(default=dict())

    async def create_user(self, user: User) -> User:
        if user.id in self._users:
            raise ValueError("User with id already exists.")
        self._users[user.id] = user
        return user

    async def read_user(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)

    async def update_user(self, user_id: int, updated_user: User) -> bool:
        if user_id not in self._users:
            return False
        self._users[user_id] = updated_user
        return True

    async def delete_user(self, user_id: int) -> bool:
        if user_id not in self._users:
            return False
        del self._users[user_id]
        return True