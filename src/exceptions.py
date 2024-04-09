import sys
'''
import sys is a line of code in Python that imports the sys module from the Python standard library. 
The sys module provides access to some variables and functions related to the Python interpreter and 
the current Python environment.
More oftenly used for:
1) Accession commad line arguments
2) Working with path and file operations
3) Handling exceptions and errors
4) Interacting with interpreter
5) Handling standard input/output/stream errors
6) Managing memory and resources
7) Handling environment variables
'''
import logging
#from src.logger import logging 

# This import is from logging.py which will write the logs for the exception occured here
#We will write custom exception handling
# Below code will be common for all projects to handle exception
def error_message_detail(error,error_detail:sys):
    # this is find the exception
    _,_,exc_tb=error_detail.exc_info() # this will exc_info will be stored in variable "exc_tb" which will give whih folder, which line we are getting exception
    # this is find the exception
    # for ore details regarding custom exception search in goggle "https://docs.python.org/3/tutorial/errors.html"
    file_name=exc_tb.tb_frame.f_code.co_filename
    # Now will the error name and error message
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        
        # This we will find the error with line number
        file_name,exc_tb.tb_lineno,str(error)
        #It constructs an error message string with information about the error, including the script name, line number, and the error message itself.
        #The function then returns this error message.
        )
    
#This is a custom exception class named CustomException that inherits from Python's built-in Exception class.
class CustomException(Exception): # this creates exception named as custom exception which inherits from base "Exception"
    def __init__(self,error_message,error_detail:sys): #THis is custructor method which takes 2 parameter error messge and error detail
        super().__init__(error_message) #Calling the construtor "__init__" with the argument
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

# Whenever we print error from here the error prints        
    def __str__(self):
        return self.error_message    
        
        
# Now this exception handling code will be used over the project

# We will test this exception code whether it is correct or not?

if __name__=='__main__':
    
    try:
        a=1/10
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e,sys)