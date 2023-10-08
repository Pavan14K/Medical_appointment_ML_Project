import sys
#We will write custom exception handling
# Below code will be common for all projects to handle exception
def error_message_detail(error,error_detail:sys):
    # this is find the exception
    _,_,exc_tb=error_detail.exc_info()
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
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)

# Whenever we print error from here the error prints        
    def __str__(self):
        return self.error_message    
        
        
# Now this exception handling code will be used over the project