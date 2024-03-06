from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = "Received status code is not to equal to expected"
    WRONG_ELEMENT_COUNT = "number of elements items is not equel expected"