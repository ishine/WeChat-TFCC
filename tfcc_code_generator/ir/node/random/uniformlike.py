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

from ir.node import Node
import ir.framework
from ir.common import get_broadcast_shape


class UniformLike(Node):
    def update_attributes(self, dtype, high: float, low: float):
        assert isinstance(high, float)
        assert isinstance(low, float)
        self._dtype = ir.framework.DataType(dtype)
        self._high = high
        self._low = low

    def inference(self):
        assert len(self.inputs) == 1
        assert len(self.outputs) == 1
        assert self.inputs[0].is_vector()
        assert self.inputs[0].dtype == ir.framework.DataType.UINT32
        assert isinstance(self.inputs[0].shape[0], int)

        if self.inputs[0].is_constant():
            shape = list(self.inputs[0].data.tolist())
        else:
            shape = [
                self.create_shape_name("normal_like")
                for _ in range(self.inputs[0].shape[0])
            ]

        self.outputs[0].stype = ir.framework.SymbolType.VARIABLE
        self.outputs[0].dtype = self.dtype
        self.outputs[0].shape = shape

    @property
    def dtype(self):
        return self._dtype

    @property
    def high(self):
        return self._high

    @property
    def low(self):
        return self._low

    @property
    def attributes(self):
        return {"dtype": self.dtype, "high": self.high, "low": self.low}
