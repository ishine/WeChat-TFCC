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
import test


class BatchMul(test.Test):
    @property
    def classPrefix(self):
        return "batch_mul"

    def calculate(self, x):
        result = np.asarray([1.0], dtype=np.float)
        for i in range(x.shape[0]):
            result = result * x[i]
        return result

    def getRandomTestData(self):
        dims = np.random.randint(1, 5)
        shape = np.random.randint(1, 10, dims)
        shape = [np.random.randint(1, 15)] + shape

        a = np.random.uniform(0.0001, 1.0, shape)

        expect = self.calculate(a)
        return {"a": a, "expect": expect}
