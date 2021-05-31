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

#include "getdimension.h"

#include <algorithm>

#include "tfcc_runtime/framework/graph.h"
#include "tfcc_runtime/proto/operations/base.pb.h"
#include "tfcc_runtime/utils/commutils.h"

namespace tfcc {
namespace runtime {
namespace base {

template <class SRC, class DST>
static const char* _wrapper_get_dimension(
    const tfcc::Tensor<SRC>* a, size_t axis, DST* result) noexcept {
  if (axis >= a->shape().size()) {
    return "GetDimension: axis error";
  }
  *result = static_cast<DST>(a->shape(axis));
  return nullptr;
}

template <tfcc::runtime::common::DataType SRC_DTYPE, tfcc::runtime::common::DataType DST_DTYPE>
std::string GetDimension<SRC_DTYPE, DST_DTYPE>::getOperationTypeUrl() const {
  tfcc::runtime::operations::base::GetDimension operation;
  return get_protobuf_type_url(operation);
}

template <tfcc::runtime::common::DataType SRC_DTYPE, tfcc::runtime::common::DataType DST_DTYPE>
std::set<unsigned> GetDimension<SRC_DTYPE, DST_DTYPE>::getOperationVersions() const {
  std::set<unsigned> versions = {tfcc::runtime::operations::base::GetDimension::VERSION_1};
  return versions;
}

template <tfcc::runtime::common::DataType SRC_DTYPE, tfcc::runtime::common::DataType DST_DTYPE>
std::unique_ptr<OperationResource> GetDimension<SRC_DTYPE, DST_DTYPE>::process(
    const tfcc::runtime::model::Node& node, Graph& graph) const {
  if (node.inputs_size() != 1 || node.outputs_size() != 1) {
    return nullptr;
  }
  if (!node.operation().Is<tfcc::runtime::operations::base::GetDimension>()) {
    return nullptr;
  }
  auto& symbolManager = getSymbolManager(graph);
  if (symbolManager.getSymbolInfo(node.outputs(0)).dtype != DST_DTYPE ||
      symbolManager.getSymbolInfo(node.inputs(0)).dtype != SRC_DTYPE) {
    return nullptr;
  }

  std::unique_ptr<OperationResource> resource(new OperationResource);
  tfcc::runtime::operations::base::GetDimension operation;
  node.operation().UnpackTo(&operation);

  auto& jit = getJIT(graph);

  const tfcc::Tensor<SRC>* inputSymbol = symbolManager.getTensor(node.inputs(0), SRC());
  DST* outputSymbol = symbolManager.getValue(node.outputs(0), DST());

  callFunction(jit, _wrapper_get_dimension<SRC, DST>, inputSymbol, operation.axis(), outputSymbol);

  return resource;
}

std::vector<std::unique_ptr<Operation>> get_get_dimension_operations() {
#define DEFINE_FUNC(src_dtype, dst_dtype) \
  operations.emplace_back(std::unique_ptr<Operation>(new GetDimension<src_dtype, dst_dtype>()));
  std::vector<std::unique_ptr<Operation>> operations;
  TFCC_RUNTIME_FOR_ALL_DATA_TYPE_ARG2(DEFINE_FUNC);
  return operations;
}

}  // namespace base
}  // namespace runtime
}  // namespace tfcc
