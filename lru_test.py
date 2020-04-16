from lru_cache import *

def main():
    lruCache = LRUCache(5)
    lruCache.put(1,"Abc")
    lruCache.put(3,"Bcd")
    lruCache.put(5,"Cde")
    
    assert lruCache.cache == {1: "Abc", 3: "Bcd", 5: "Cde"}
    print("Test Case passed! --> put()")

    lruCache.put(7,"Def")
    lruCache.put(9,"Efg")
    
    #print(lruCache.get_cache())
    assert lruCache.cache == {1: "Abc", 3: "Bcd", 5: "Cde", 7: "Def", 9: "Efg"}
    print("Test Case passed! --> put()")

    assert lruCache.get(2) == -1
    print("Test Case passed! --> get()")

    assert lruCache.get(3) == "Bcd"
    print("Test Case passed! --> get()")

    #print(lruCache.get_cache())
    assert lruCache.get_cache() == {1: "Abc", 3: "Bcd", 5: "Cde", 7: "Def", 9: "Efg"}
    print("Test Case passed! --> get_cache()")

    lruCache.put(11,"E11")
    lruCache.put(13,"F13")
    #print(lruCache.get_cache())
    assert lruCache.cache == {3: 'Bcd', 7: 'Def', 9: 'Efg', 11: 'E11', 13: 'F13'}
    print("Test Case passed! --> put()")

    assert lruCache.get(5) == -1
    print("Test Case passed! --> get()")
    
    print("\n\n*** All test cases are passed for LRU cache ***")

if __name__ == "__main__":
    main()