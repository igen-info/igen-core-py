from __future__ import annotations

from threading import Lock
from typing import Any, Dict, Type, TypeVar

__all__ = ["Singleton"]

T = TypeVar("T", bound="Singleton")


class Singleton:
    """Simple thread-safe singleton mixin."""

    _instance_lock: Lock = Lock()
    _instances: Dict[Type["Singleton"], "Singleton"] = {}

    def __new__(cls: Type[T], *args: Any, **kwargs: Any) -> T:  # noqa: D401
        if cls not in cls._instances:
            with cls._instance_lock:
                if cls not in cls._instances:
                    instance = super().__new__(cls)
                    cls._instances[cls] = instance
        return cls._instances[cls]  # type: ignore[return-value]
