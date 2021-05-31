// Copyright 2021 Wechat Group, Tencent
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#include "fusion.h"

#include "tfcc_runtime/operations/fusion/fusionopdynamicshape.h"
#include "tfcc_runtime/operations/fusion/fusionopfixedshape.h"
#include "tfcc_runtime/operations/operation.h"

namespace tfcc {
namespace runtime {
namespace fusion {

static void append_vector(
    std::vector<std::unique_ptr<Operation>>& dst, std::vector<std::unique_ptr<Operation>> src) {
  for (auto& op : src) {
    dst.emplace_back(std::move(op));
  }
}

std::vector<std::unique_ptr<Operation>> get_all_operations() {
  std::vector<std::unique_ptr<Operation>> operations;
  append_vector(operations, get_fusionopfixedshape_operations());
  append_vector(operations, get_fusionopdynamicshape_operations());
  return operations;
}

}  // namespace fusion
}  // namespace runtime
}  // namespace tfcc
