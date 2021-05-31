# Copyright 2021 Wechat Group, Tencent
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import ir.node
from backend.cppcode.nodegenerator.nodegenerator import NodeGenerator


class MaxPool(NodeGenerator):
    @classmethod
    def accept(cls, node: ir.node.Node):
        return isinstance(node, ir.node.nn.MaxPool)

    @property
    def code(self):
        if len(self.inputs[0].shape) == 4:
            return "auto {outputs[0]} = tfcc::nn::max_pool2d({inputs[0]}, {nhwc}, {node.kernels[0]}, {node.kernels[1]}, {node.pads[0]}, {node.pads[1]}, {node.strides[0]}, {node.strides[1]});\n".format(
                nhwc="true"
                if self.node.data_format == self.node.DataFormat.NHWC
                else "false",
                **self.fmt_dict
            )
        elif len(self.inputs[0].shape) == 3:
            return "auto {outputs[0]} = tfcc::nn::max_pool1d({inputs[0]}, {nwc}, {node.kernels[0]}, {node.pads[0]}, {node.strides[0]});\n".format(
                nwc="true"
                if self.node.data_format == self.node.DataFormat.NWC
                else "false",
                **self.fmt_dict
            )
        else:
            raise NotImplementedError
