# Act 2A - What's Following Output
# ## print = [10, 20, 30, 40, 50, 60]
# ## print = [10, 20, 30, 40, 50, 60, 60]

sampleList = [10, 20, 30, 40, 50]
sampleList.append(60) #.appends adds to the END of the list
print(sampleList)

sampleList.append(60)
print(sampleList)

# Act 2b - Reversing a List & Tuple
print('\n\nAct 2B')
aList = [100, 200, 300, 400, 500]
aTuple = (10, 20, 30, 40, 50)

aList.reverse()
ReverseTuple = reversed(aTuple)    # Reverses Tuple In Variable Format
ReverseTuple = tuple(ReverseTuple) # ReversedTuple is reverted back into a Tuple
print(aList)
print(ReverseTuple)

# Act 2b OFFICAL WAY
print(" \nAct 2b via Teacher's Answers ")
aList = [100, 200, 300, 400, 500]
aTuple = (10, 20, 30, 40, 50)

aList = aList[::-1] # [::-1] Counts From Last Value In List
print(aList)
aTuple = aTuple[::-1]
print(aTuple)

