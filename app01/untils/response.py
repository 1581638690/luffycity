class BaseResponse(object):
    def __init__(self):
        self.code=1000
        self.data=None
        self.error=None
        self.token=None
    @property
    def dict(self):
        return self.__dict__
