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

#pragma once

#include <cstdint>
#include <memory>
#include <vector>

#include "tfcc.h"

#include "tfcc_runtime/framework/symbolmanager.h"
#include "tfcc_runtime/framework/types.h"
#include "tfcc_runtime/operations/operation.h"
#include "tfcc_runtime/proto/common.pb.h"

namespace tfcc {
namespace runtime {
namespace base {

class If : public Operation {
 public:
  std::string getOperationTypeUrl() const override;
  std::set<unsigned> getOperationVersions() const override;
  std::unique_ptr<OperationResource> process(
      const tfcc::runtime::model::Node& node, Graph& graph) const override;
};

std::vector<std::unique_ptr<Operation>> get_if_operations();

}  // namespace base
}  // namespace runtime
}  // namespace tfcc
