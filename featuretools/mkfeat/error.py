from enum import Enum


class Error(Enum):
    """
    mkfeat과 관련된 일체의 오류를 정의. Exception보다는 반환값으로 API를 정의하고자 함
    """
    OK = 0
    ERR_GENERAL = -1
    ERR_INVALID_ARG = -2
    ERR_COLUMN_COUNT_MISMATCH = -3
    ERR_ONGOING = -4
    ERR_DATA_NOT_FOUND = -5
    ERR_LABEL_NOT_FOUND = -6
    ERR_COLUMN_HAS_NO_NAME_OR_TYPE = -7
    ERR_COLUMN_MULTI_KEY = -8
    ERR_COLUMN_MULTI_LABEL = -9
    ERR_COLUMN_NO_KEY = -10
    ERR_COLUMN_KEY_AND_LABEL = -11
    ERR_STOPPED = -12
    ERR_COLUMN_TYPE = -13
