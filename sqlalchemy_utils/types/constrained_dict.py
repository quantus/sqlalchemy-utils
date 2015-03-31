from sqlalchemy import types
from sqlalchemy.dialects.postgresql import HSTORE


class ConstrainedDict(types.TypeDecorator):
    """
    TODO: Doc *********************************************************************
    """
    impl = HSTORE

    def __init__(self, item_max_length=None, *args, **kwargs):
        self.item_max_length = item_max_length
        super(ConstrainedDict, self).__init__(*args, **kwargs)

    # TODO: Limiting item length ************************************************
