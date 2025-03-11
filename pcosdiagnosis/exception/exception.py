import sys
from pcosdiagnosis.logging import logger

class PCOSException(Exception): #This custom class inherits from the built-in Exception class in python.
    def __init__(self,error_message,error_details:sys): #This method initializes the class and sets the error message, line number, and file name.
        self.error_message = error_message # Store the custom error message
        _,_,exc_tb = error_details.exc_info() # Retrieve the traceback object
        
        self.lineno=exc_tb.tb_lineno # Extract the line number from the traceback
        self.file_name=exc_tb.tb_frame.f_code.co_filename # Extract the file name from the traceback
    
    # This method returns a formatted string that includes the file name, line number, and error message. 
    # This string is used when the exception is converted to a string, such as when it is printed or logged.
    def __str__(self): 
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
# if __name__=='__main__':
#     try:
#         logger.logging.info("Enter the try block")
#         a=1/0
#         print("This will not be printed",a)
#     except Exception as e:
#            raise PCOSException(e,sys)