class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.size =0
        self.cache = {}
        self.lru = {}
    def put(self, key, val):
        if(len(self.cache)==self.capacity):
            if(key not in self.cache):
                old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
                self.cache.pop(old_key)
                self.lru.pop(old_key)
                self.cache[key]=val
                self.lru[key]=0
        else:
           if(key not in self.cache):
                self.cache[key]=val
                self.lru[key]=0

    def get (self,key):
        if(key in self.cache):
            count=self.lru[key]
            self.lru[key]=count+1
            return self.cache[key]
        else:
            return None


    def get_cache(self):
        return self.cache
    def get_LRU(self):
        return self.lru
    def get_singleelementfromcache(self,key):
        if key in self.cache:
            return self.cache[key]
        return None
    def current_frequency(self,key):
        if key in self.lru:
            return self.lru[key]
        else:
            return None
lruobj = LRU(2)
lruobj.put(2,"git")
lruobj.put(3,"hub")
lruobj.get(3)
lruobj.put(55,"hmm")
assert(lruobj.get(55))=="hmm"
assert(lruobj.get(2))==None

assert(lruobj.current_frequency(3))==1
assert(lruobj.current_frequency(65)) == None
assert(lruobj.get_singleelementfromcache(2))==None
lruobj.get(3)
lruobj.get(55)
lruobj.get(3)
lruobj.put(25,"sahhhh")
assert(lruobj.get(55))==None
assert(lruobj.current_frequency(55))==None
assert(lruobj.current_frequency(25))==0
lruobj.put(25,"ss")
assert(lruobj.current_frequency(25))==0
print("ALL TESTCASES PASSED")


   