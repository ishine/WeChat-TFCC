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
from backend.runtime.nodegenerator.nodegenerator import NodeGenerator
from ...common import data_type_to_proto
from ...proto.operations import random_pb2


class UniformLike(NodeGenerator):
    @classmethod
    def accept(cls, node: ir.node.Node):
        return isinstance(node, ir.node.random.UniformLike)

    @property
    def operation(self):
        operation = random_pb2.UniformLike()
        if self.outputs[0].is_integer():
            operation.low.int64_value = self.node.low
            operation.high.int64_value = self.node.high
        elif self.outputs[0].is_floating_point():
            operation.low.double_value = self.node.low
            operation.high.double_value = self.node.high
        else:
            raise RuntimeError("Unknow value")
        return operation
