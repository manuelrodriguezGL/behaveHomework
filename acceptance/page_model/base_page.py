class BasePage:
    def __init__(self, context):
        self.driver = context.driver
        self.context = context
