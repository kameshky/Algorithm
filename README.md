# Practice Python

Comeback refrence guide to my code and learning. Starting my python practice as a aim to clear an interview for core IT Company. Part of my daily plan.

## Getting Started

I am going to collect important information here about topics generally asked in interview. Also this is going to be my code collection as I understand them.
As big IT companies require good programming knowledge, this will be a guide.

## Starting the journey

### General programming knowledge and know-to of Python 

1. Adding a shebang line:
   - `#!/usr/bin/python3`:Shebang line that defines where the interpreter is located generally on linux.
   - `#!/usr/bin/env python3`:This is used for portability over all Operating System.

2. `if __name__ == "__main__"` :Before executing the code Python iterpreter defines some variables, one of them is `__name__`. If script or program is run as a main program `__name__` is assigned a value `__main__`. If imported from another module, that module's name will be assigned to `__name__`.

   - By doing this main check we assure that following code will run only when script is run as main program.
   
3. Errors are not always bad: If a program generates some error it does not always mean you have done something wrong. Sometimes error can occur due to wrong user input or a process failure. So sometimes errors are expected we just need to handle them.

`try:

     Some code that may generates error
     example: n = 20/0
 
 except ValueError:
                  
                  print("Deviding by zero is not allowed")`
       


### Data Structures

1. Array/List : Usually we can assign only one value per variable. Array let us to use single variable for multiple values.
   - pop()
   - append(): inserts value at the end of the list.
   - reverse()
   - sort()
   - remove(value)
   - insert(index, value)

> A contiguous area of memory which holds values indexed with contiguous integers, normally starting from 0.
