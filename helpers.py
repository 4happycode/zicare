from enum import Enum

class SortType(str, Enum):
    asc     = 'ascending'
    desc    = 'descending'


class SortBy(str, Enum):
    id              = 'id'
    ktp             = 'ktp'
    first_name      = 'first_name'
    last_name       = 'last_name'
    created_date    = 'created_date'

    # if there is an addition, place above here 
