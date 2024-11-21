from enum import Enum

class FileMode(Enum):
    """ DTO for file mod  """
    READ = "r"
    WRITE = "w"
    APPEND_WRITE = "a"