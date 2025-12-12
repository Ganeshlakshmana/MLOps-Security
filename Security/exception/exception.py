from venv import logger
# import custom_exceptions
import sys
from Security.logging.logger import logging

class SecurityException(Exception):
    
    """Base class for all security-related exceptions."""
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message,error_detail)
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()
        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
    
    def __str__(self):
        return f"SecurityException: {self.error_message} (File: {self.file_name}, Line: {self.line_number})"
        


  
