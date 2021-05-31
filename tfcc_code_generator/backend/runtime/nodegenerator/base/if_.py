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
from ...proto.operations import base_pb2


class If(NodeGenerator):
    @classmethod
    def accept(cls, node: ir.node.Node):
        return isinstance(node, ir.node.base.If)

    @property
    def operation(self):
        operation = base_pb2.If()
        operation.then_graph_name = self.node.then_graph_name
        operation.then_graph_capture_count = self.node.then_graph_capture_count
        operation.else_graph_name = self.node.else_graph_name
        operation.else_graph_capture_count = self.node.else_graph_capture_count

        return operation
