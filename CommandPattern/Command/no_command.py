from command_abc import AbsCommand


# this is the null pattern btw
class NoCommand(AbsCommand):
    def __init__(self, args):
        self._command = args[0]
        pass

    def execute(self):
        print('no command named %s' % self._command)