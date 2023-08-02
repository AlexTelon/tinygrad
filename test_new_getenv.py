from tinygrad.helpers import getenv

# Get an environment variable (it will be cached)
flag = getenv("FLAG", 0)
assert flag == 0

# Modify the cache manually
getenv.cache["FLAG"] = 1

# Flag is however still 0 since its just an integer value.
assert flag == 0

# Get the environment variable again (it will return the cached value)
assert getenv("FLAG", 1) == 1

# Use a temporary cache
with getenv.temporary_cache(FLAG=2):
    assert getenv("FLAG") == 2
assert getenv("FLAG") == 1
