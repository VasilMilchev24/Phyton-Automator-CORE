class AutomationError(Exception):
    pass

class ElementNotFoundError(AutomationError):
    def __init__(self, selector: str, message: str = None):
        if message is None:
            message = f"Element not found for selector: {selector}"
        super().__init__(message)
        self.selector = selector

class NavigationError(AutomationError):
    def __init__(self, url: str, message: str = None):
        if message is None:
            message = f"Failed to navigate to URL: {url}"
        super().__init__(message)
        self.url = url

class ActionFailedError(AutomationError):
    def __init__(self, action: str, selector: str = None, message: str = None):
        if message is None:
            msg = f"Action '{action}' failed"
            if selector:
                msg += f" on selector: {selector}"
            message = msg
        super().__init__(message)
        self.action = action
        self.selector = selector
