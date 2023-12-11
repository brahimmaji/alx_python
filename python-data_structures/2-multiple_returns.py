def multiple_returns(sentence):
    length = len(sentence)
    first = None if length == 0 else sentence[0]
    return length,first
#def multiple_returns(sentence):
  #  length=len(sentence)
 #   first = None if length == 0 else sentence[0]
#    print("Length: {:d} - First character: {}".format(length, first))

if __name__ == '__main__':
    sentence = ''
    length, first = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first))
