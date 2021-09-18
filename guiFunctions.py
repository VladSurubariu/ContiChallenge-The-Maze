def sumUpTuples(tuple1, tuple2):
     return tuple(map(sum, zip(tuple1, tuple2)))


#print(sumUpTuples((100,100),(40,-460)))