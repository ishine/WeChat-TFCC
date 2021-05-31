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

import onnx
import ir.node
import ir.framework
import frontend.onnx.common
from ..converter import Converter


class Reshape(Converter):
    def __call__(
        self,
        node_proto: onnx.NodeProto,
        graph_proto: onnx.GraphProto,
        graph: ir.framework.Graph,
    ):
        if not self.accept(node_proto):
            return False

        shape_symbol = graph.get_symbol(node_proto.input[1])
        if shape_symbol.is_vector():
            graph.append_node(
                ir.node.base.Reshape(
                    node_proto.name, graph, node_proto.input, node_proto.output
                )
            )
        else:
            to_vector_output_name = graph.context.create_symbol_name(
                node_proto.output[0]
            )
            graph.append_node(
                ir.node.base.ToVector(
                    node_proto.name + ":0",
                    graph,
                    [node_proto.input[1]],
                    [to_vector_output_name],
                )
            )
            graph.append_node(
                ir.node.base.Reshape(
                    node_proto.name + ":1",
                    graph,
                    [node_proto.input[0], to_vector_output_name],
                    node_proto.output,
                )
            )

        return True

    @property
    def accept_versions(self) -> set:
        # TODO support Reshape-1
        return set([5])
