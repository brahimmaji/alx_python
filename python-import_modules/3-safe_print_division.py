def safe_print_division(a, b):
    result=a/b
    try:
         b > 0 
            
    except:
        print("Error") 
    finally:
        print("the result of {:d}/{:d} = {:d}".format(a,b,result))    