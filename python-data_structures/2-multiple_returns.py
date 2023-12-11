def multiple_returns(sentence):
    length=len(sentence)
    first=sentence[0:1]
    if sentence != "" :
        print("Length: {:d} - First character: {}".format(length, first))

    else:
        print(None)   
   # return length,first

multiple_returns = __import__('2-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))