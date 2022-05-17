import pytorchgui as rc
from random import random

import torch
import matplotlib.pyplot as plt


# let's define some nodes
# to easily see something in action, we create one node generating random numbers, and one that prints them

class PrintNode(rc.Node):
    """Prints your data"""

    title = 'Print'
    init_inputs = [
        rc.NodeInputBP(),
    ]
    init_outputs = []
    color = '#A9D5EF'

    # we could also skip the constructor here
    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        print(
            self.input(0)  # get data from the first input
        )


class MatplotlibShow(rc.Node):
    """Prints your data"""

    title = 'Matplotlib show image'
    init_inputs = [
        rc.NodeInputBP(),
    ]
    init_outputs = []
    color = '#b5143c'

    # we could also skip the constructor here
    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        try:
            plt.imshow(self.input(0))
            plt.show()
        except Exception as e:
            print(e)


class RandNode(rc.Node):
    """Generates random values"""

    title = 'Rand'
    init_inputs = [
        rc.NodeInputBP(dtype=rc.dtypes.Data(default=1)),
        rc.NodeInputBP(dtype=rc.dtypes.Data(default=None)),
        rc.NodeInputBP(dtype=rc.dtypes.Data(default=None)),
    ]
    init_outputs = [
        rc.NodeOutputBP(),
    ]
    color = '#fcba03'

    def update_event(self, inp=-1):
        # random float at shape from input
        shape = (self.input(0),)
        shape += (self.input(1),) if self.input(1) is not None else ()
        shape += (self.input(2),) if self.input(2) is not None else ()
        # print(shape)
        val = torch.randn(shape).to(self.device)

        # setting the value of the first output
        self.set_output_val(0, val)


class TensorFromConst(rc.Node):
    """Generate a tensor"""

    title = 'Tensor'
    init_inputs = [
        rc.NodeInputBP(),
        rc.NodeInputBP(dtype=rc.dtypes.Data(default=1)),
        rc.NodeInputBP(dtype=rc.dtypes.Data(default=None)),
        rc.NodeInputBP(dtype=rc.dtypes.Data(default=None)),
    ]
    init_outputs = [
        rc.NodeOutputBP(),
    ]
    color = '#ee4c2c'

    def update_event(self, inp=-1):
        shape = (self.input(1),)
        shape += (self.input(2),) if self.input(2) is not None else ()
        shape += (self.input(3),) if self.input(3) is not None else ()
        val = torch.zeros(shape).to(self.device) + self.input(0)
        self.set_output_val(0, val)


class ConstNode(rc.Node):
    """Generate a constant"""

    title = 'Const'
    init_inputs = [
        rc.NodeInputBP(dtype=rc.dtypes.Data(default=1)),
    ]
    init_outputs = [
        rc.NodeOutputBP(),
    ]
    color = '#fcba03'

    def update_event(self, inp=-1):
        self.set_output_val(0, self.input(0))


class AddNode(rc.Node):
    """Adds data"""

    title = 'Add'
    init_inputs = [
        rc.NodeInputBP(),
        rc.NodeInputBP(),
    ]
    init_outputs = [
        rc.NodeOutputBP(),
    ]
    color = '#A9D5EF'

    # we could also skip the constructor here
    def __init__(self, params):
        super().__init__(params)

    def update_event(self, inp=-1):
        self.set_output_val(0, self.input(0) + self.input(1))


export_nodes = [
    PrintNode,
    RandNode,
    AddNode,
    ConstNode,
    MatplotlibShow,
    TensorFromConst
]
