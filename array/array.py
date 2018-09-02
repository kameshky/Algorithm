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
    
"""
before executing the code python interpreter defines many variables such as __name__
if we are running our script as a main program rather than importing it "__name__" 
variable get assigned value "__main__"

one use case is if we do not want some code to run if the file is imported rather than 
run as a main program

https://stackoverflow.com/questions/419163/what-does-if-name-main-do
"""
if __name__ == "__main__":
    main()
    