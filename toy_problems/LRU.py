class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.size =0
        self.cache = {}
        self.lru = {}
  def put(self,key,val):
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
      