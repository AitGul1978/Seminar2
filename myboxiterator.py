class MyIterator(): 
    def __init__( self, L ): 
        self.L = L 
        
    def __iter__(self): 
        self.idx = 0
        return self 
    
    def __next__(self): 
        if self.idx < len(self.L): 
            item = self.L[self.idx] 
            self.idx += 1
            return item 
        else: 
            raise StopIteration 
