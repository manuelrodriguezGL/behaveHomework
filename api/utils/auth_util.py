from requests.auth import HTTPBasicAuth


class AuthUtil:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(AuthUtil, cls).__new__(cls)
            cls.instance.username = args[0]
            cls.instance.password = args[1]
            cls.instance.auth = HTTPBasicAuth(cls.instance.username, cls.instance.password)
        return cls.instance
