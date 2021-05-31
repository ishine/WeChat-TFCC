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


class Unstack(test.Test):
    def getRandomTestData(self):
        dims = np.random.randint(2, 5)
        axis = np.random.randint(0, dims)
        shape = np.random.randint(1, 10, dims)
        expectShape = np.copy(shape).tolist()
        expectShape.pop(axis)
        expectShape = np.asarray(expectShape)

        a = np.random.uniform(-1.0, 1.0, shape)
        expects = []
        for e in np.split(a, shape[axis], axis):
            e = np.reshape(e, expectShape)
            expects.append(e)

        result = {
            "a": a,
            "axis": np.asarray([axis], dtype=np.int32),
        }
        for i, e in enumerate(expects):
            result["expect_" + str(i)] = e

        return result
