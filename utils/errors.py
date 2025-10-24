class AutomationError(Exception):
    pass

class MCPConnectionError(AutomationError):
    pass

class PlanExecutionError(AutomationError):
    pass
