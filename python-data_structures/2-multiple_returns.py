def multiple_returns(sentence):
    length=len(sentence)
    first=sentence[0:1]
    if sentence != "" :
        print("Length: {:d} - First character: {}".format(length, first))

    else:
        print("Length: {:d} - First character: None".format(length))   
   # return length,first
