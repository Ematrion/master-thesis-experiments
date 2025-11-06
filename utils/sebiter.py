import itertools
import math

'''
Define an iterator on all possible seedings in a single elimination bracket

'''


class UMNC:
    # 'unordered multinomial coeficient'
    def __init__(self, labels):
        self.labels = labels
        
        self.n = len(labels)
        self.iterator = itertools.combinations(self.labels, self.n//2)
        
        self.len = int(math.factorial(self.n)/(math.pow(math.factorial(self.n//2),2) * 2))
        self.it = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.it < self.len:
            self.it += 1
            return next(self.iterator)
        else:
            raise StopIteration


class reprSEB:
    '''
    Define the iterator recursively using the UMNC coeficient.
    '''
    def __init__(self, labels):
        self.size = len(labels)
        if self.size == 2:
            self.classes = iter([(min(labels), max(labels))])
            self.len = 1
        else:
            self.labels = list(range(self.size))
            self.labelisation = {index: label for index, label in zip(self.labels, labels)}

            self.half = self.labels[0:len(self.labels)//2]

            self.len = int(math.factorial(self.size)/math.pow(2, self.size-1))

            self.left = reprSEB(self.half)
            self.right = reprSEB(self.half)
            self.splits = UMNC(self.labels)
            self.classes = self.__iterator__() # maybe not necessary
    
    def __iterator__(self):
        return itertools.product(self.left, self.right, self.splits)
        
    def __len__(self):
        return self.len
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.size == 2:
            return next(self.classes)
        else:
            left, right, left_labels = next(self.classes) # type: ignore
            right_labels = [i for i in self.labels if i not in left_labels]
            seeding = [left_labels[i] for i in left]+[right_labels[i] for i in right]
            return tuple([self.labelisation[i] for i in seeding])