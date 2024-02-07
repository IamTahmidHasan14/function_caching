#FUNCTION CACHING
print()
from functools import lru_cache
# from time import sleep
import time

@lru_cache(maxsize=None)
def fx(n):
  time.sleep(2)
  return (n * n + 1)

print(fx(6))
print("Done for 6")