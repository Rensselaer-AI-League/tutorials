class Vector:
    def __init__(self, val):
        self.val = val
        
    def __add__(self, other):
        return Vector([i + j for i, j in zip(self, other)])
    
    def __iadd__(self, other):
        for i, val in enumerate(other):
            self.val[i] += val
            
    def __getitem__(self, i):
        return self.val[i]