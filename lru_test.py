from lru_cache import *

assert put(1, "One") == null
assert put(2, "Two") == null
assert put(3, "Three") == null

assert get(1) == 0
assert get(4) == 0
assert get(8) == 0

assert get_cache() == {}
assert get_cache() == {}
assert get_cache() == {}
