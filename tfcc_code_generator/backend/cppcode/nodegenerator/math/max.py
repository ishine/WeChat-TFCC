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


class Max(NodeGenerator):
    @classmethod
    def accept(cls, node: ir.node.Node):
        return isinstance(node, ir.node.math.Max)

    @property
    def code(self):
        if self._node.inputs[0].is_value() and self._node.inputs[1].is_value():
            return "auto {outputs[0]} = std::max({inputs[0]}, {inputs[1]});\n".format(
                **self.fmt_dict
            )
        else:
            return "auto {outputs[0]} = tfcc::math::max({inputs[0]}, {inputs[1]});\n".format(
                **self.fmt_dict
            )
