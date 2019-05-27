import os


class ReadEnvConfig:

    @staticmethod
    def get_app_username(context):
        try:
            return os.environ['APP_USERNAME']
        except Exception as e:
            context.logger.error(e.__class__)
            return None

    @staticmethod
    def get_app_password(context):
        try:
            return os.environ['APP_PASSWORD']
        except Exception as e:
            context.logger.error(e.__class__)
            return None
