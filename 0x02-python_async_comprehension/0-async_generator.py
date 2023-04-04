#!/usr/bin/env python3
"""
Task 0
"""
import asyncio
from typing import Generator
import random

async def async_generator() -> Generator[float, None, None]:
   """
   The coroutine will loop 10 times, each time asynchronously wait 1 second
   """

   for _ in range(10):
       await asyncio.sleep(1)
       yield random.random() * 10


