class BaseModule:
    core = None
    hooks = []

    def __init__(self, core):
        self.core = core

    def activate(self, hooks=None):
        if hooks is None:
            return
        for hook in hooks:
            hook_name, action_name, action = hook
            self.hooks.append([hook_name, action_name])
            self.core.hooks.add(hook_name, action_name, action)

    def deactivate(self):
        for hook in self.hooks:
            hook_name, action_name = hook
            self.core.hooks.remove(hook_name, action_name)
