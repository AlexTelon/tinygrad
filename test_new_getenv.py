from tinygrad.helpers import getenv, Context, ContextVar

FLAG = getenv("FLAG", 0)
assert FLAG == 0

FLAG.value = 1
assert FLAG == 1

# Get the environment variable again (it will return the cached value)
assert getenv("FLAG") == 1
assert FLAG == 1


# Use a temporary cache
with Context(FLAG=2):
    assert FLAG == 2
    assert getenv("FLAG") == 2

assert FLAG == 1
assert getenv("FLAG") == 1

STRING = getenv("STRING", "")
assert STRING == ""

print('all ok')