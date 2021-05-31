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


class IRFFT(Node):
    def update_attributes(self, length: int):
        assert isinstance(length, int) and length > 0
        self._length = length

    def inference(self):
        assert len(self.inputs) == 1
        assert len(self.outputs) == 1
        assert self.inputs[0].is_tensor()
        assert self.inputs[0].dtype == ir.framework.DataType.COMPLEX64

        shape = self.inputs[0].shape
        shape[-1] = self.length

        self.outputs[0].stype = ir.framework.SymbolType.VARIABLE
        self.outputs[0].dtype = ir.framework.DataType.FLOAT
        self.outputs[0].shape = shape

    @property
    def length(self):
        return self._length

    @property
    def attributes(self):
        return {"length": self.length}
