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

#include "identity.h"

#include <algorithm>

#include "tfcc_runtime/framework/graph.h"
#include "tfcc_runtime/proto/operations/base.pb.h"
#include "tfcc_runtime/utils/commutils.h"

namespace tfcc {
namespace runtime {
namespace base {

template <class T>
static const char* _wrapper_identity_v1(
    const tfcc::Tensor<T>* a, tfcc::Variable<T>* result) noexcept {
  try {
    *result = tfcc::data::copy(*a);
  } catch (std::exception& e) {
    thread_local std::string reason = e.what();
    return reason.c_str();
  }
  return nullptr;
}

template <class T>
static const char* _wrapper_identity_v2(const std::vector<T>* a, std::vector<T>* result) noexcept {
  *result = *a;
  return nullptr;
}

template <class T>
static const char* _wrapper_identity_v3(const T* a, T* result) noexcept {
  *result = *a;
  return nullptr;
}

template <tfcc::runtime::common::DataType DTYPE>
std::string Identity<DTYPE>::getOperationTypeUrl() const {
  tfcc::runtime::operations::base::Identity operation;
  return get_protobuf_type_url(operation);
}

template <tfcc::runtime::common::DataType DTYPE>
std::set<unsigned> Identity<DTYPE>::getOperationVersions() const {
  std::set<unsigned> versions = {tfcc::runtime::operations::base::Identity::VERSION_1};
  return versions;
}

template <tfcc::runtime::common::DataType DTYPE>
std::unique_ptr<OperationResource> Identity<DTYPE>::process(
    const tfcc::runtime::model::Node& node, Graph& graph) const {
  if (node.inputs_size() != 1 || node.outputs_size() != 1) {
    return nullptr;
  }
  if (!node.operation().Is<tfcc::runtime::operations::base::Identity>()) {
    return nullptr;
  }
  auto& symbolManager = getSymbolManager(graph);
  if (symbolManager.getSymbolInfo(node.outputs(0)).dtype != DTYPE ||
      symbolManager.getSymbolInfo(node.inputs(0)).dtype != DTYPE) {
    return nullptr;
  }

  std::unique_ptr<OperationResource> resource(new OperationResource);
  tfcc::runtime::operations::base::Identity operation;
  node.operation().UnpackTo(&operation);

  auto& jit = getJIT(graph);

  const auto& inputInfo = symbolManager.getSymbolInfo(node.inputs(0));
  if (is_tensor(inputInfo.stype)) {
    const tfcc::Tensor<T>* inputSymbol = symbolManager.getTensor(node.inputs(0), T());
    tfcc::Variable<T>* outputSymbol = symbolManager.getVariable(node.outputs(0), T());
    callFunction(jit, _wrapper_identity_v1<T>, inputSymbol, outputSymbol);
  } else if (is_vector(inputInfo.stype)) {
    const std::vector<T>* inputSymbol = symbolManager.getVector(node.inputs(0), T());
    std::vector<T>* outputSymbol = symbolManager.getVector(node.outputs(0), T());
    callFunction(jit, _wrapper_identity_v2<T>, inputSymbol, outputSymbol);
  } else if (is_value(inputInfo.stype)) {
    const T* inputSymbol = symbolManager.getValue(node.inputs(0), T());
    T* outputSymbol = symbolManager.getValue(node.outputs(0), T());
    callFunction(jit, _wrapper_identity_v3<T>, inputSymbol, outputSymbol);
  } else {
    // error
    return nullptr;
  }

  return resource;
}

std::vector<std::unique_ptr<Operation>> get_identity_operations() {
#define DEFINE_FUNC(dtype) \
  operations.emplace_back(std::unique_ptr<Operation>(new Identity<dtype>()));
  std::vector<std::unique_ptr<Operation>> operations;
  TFCC_RUNTIME_FOR_ALL_DATA_TYPE(DEFINE_FUNC);
  return operations;
}

}  // namespace base
}  // namespace runtime
}  // namespace tfcc
