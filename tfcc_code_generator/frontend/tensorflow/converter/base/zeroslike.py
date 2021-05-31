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

import numpy as np
from tensorflow.python.framework.ops import Operation
import ir.framework
import ir.node
from ..converter import Converter
from ... import common


# implement for https://tensorflow.google.cn/api_docs/python/tf/raw_ops/ZerosLike?hl=en
class ZerosLike(Converter):
    def __call__(self, op: Operation, graph: ir.framework.Graph):
        if not self.accept(op):
            return False

        inp_strs = [inp.name for inp in op.inputs]
        oup_strs = [oup.name for oup in op.outputs]

        get_shape_output = graph.context.create_symbol_name(oup_strs[0])
        graph.append_node(
            ir.node.base.GetShape(op.name + ":0", graph, inp_strs, [get_shape_output])
        )

        dtype = graph.get_symbol(inp_strs[0]).dtype
        value = np.asarray([0], dtype=dtype.numpy_dtype)
        graph.append_node(
            ir.node.base.CreateTensor(
                op.name + ":1",
                graph,
                [get_shape_output],
                oup_strs,
                dtype=dtype,
                value=value,
            )
        )
        return True
