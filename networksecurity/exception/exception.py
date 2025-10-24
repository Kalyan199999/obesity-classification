import sys

from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    """
    Base class for all exceptions in the networksecurity module.
    """

    def __init__(self, err_message,err_details:sys):
        self.err_message = err_message

        _,_,exc_tb= err_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename


    def __str__(self):
        return "Error Occured in python script name [ {0} ] line number [ {1} ] error message [{2}]".format( self.filename , self.lineno , str(self.err_message) )
    
# if __name__ == "__main__":
#     try:
#         logger.logging.info("Entered the try block!")
#         a = 10 / 0
#         print(f"Result is:{a}")
#     except Exception as e:
#         raise NetworkSecurityException("Error Occured", sys) from e
#     except NetworkSecurityException as nse:
#         print(nse)

        