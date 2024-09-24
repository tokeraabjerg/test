#==========================================================================================================================
#  ?                                                     ABOUT
#  @author         :  Toke Raabjerg
#  @email          :  tokermc@hotmail.com
#  @repo           :  automated-3d-scanning
#  @createdOn      :  24/09
#  @description    :  This handles the initiziation of point-cloud-processing.
#==========================================================================================================================

#===========================================================================
#  todo                             TODO
#    
#    Start making it
#    
# 
#===========================================================================


import addition

arg1=""
arg2=""

def takeInputs():
    arg1 = input("First number:")
    arg2 = input("Second number:")

    if(arg1.isdigit() and arg2.isdigit()):
        print([float(arg1), float(arg2)])
        return [float(arg1), float(arg2)]
    else:
        print("All arguments are not digits, please try again")
        takeInputs()

def mainScope():
    InputArg = input("1: Addition \nX:close \n")

    if(InputArg == "X"):
        return print("Closing calculator")
    
    match InputArg:
        case "1":
            print("---- Addition ----")
            addition.addit(takeInputs())
        case _:
            print("Invalid input, try again")
            mainScope()

mainScope()