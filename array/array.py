"""
#!/usr/bin/python3
these are shebang lines that defines where the interpreter is located.

#!/usr/bin/env python3
this is used for portability over all operating system
"""

def array():
    
    array = [1,2,3,4]
    
    
    #remove the last item from the list
    array.pop()
    
    #append operation insert item at the end of the list
    array.append(5)
    
    # insert(index, value)
    array.insert(1,3)  
    print("pop append and insert are applied")
    print(array)
    
    array.reverse()
    print("reverse array",array)
    
    #sort in acsending order
    array.sort()
    print("sorted array in order", array)
    
    
def main():
    array()
    
if __name__ == "__main__":
    main()
    