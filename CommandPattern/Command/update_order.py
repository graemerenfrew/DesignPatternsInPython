from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand

class UpdateOrder(AbsCommand, AbsOrderCommand):
    #implement the abstract properties
    name = "UpdateQuantity"
    description = "UpdateQuantity Number"

    def __init__(self, args):
        self.newqty = args[1]

    def execute(self):
        oldqty = 5
        #simulate db update
        print("updated database")
        #simulate logging
        print("log: updated qty from %s to %s " % (oldqty, self.newqty))