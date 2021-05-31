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

#include <cstddef>
#include <set>

#include "tfcc_mklregister.h"

namespace tfcc {
namespace fusionop {

class TempRegister : public Register {
  size_t _offset;

 public:
  TempRegister(std::set<size_t> positions, size_t priority, RegisterManager& manager);
  virtual ~TempRegister();

  /**
   * Store register data.
   */
  virtual void store() override;

  /**
   * Load register data.
   */
  virtual void load() override;
};

}  // namespace fusionop
}  // namespace tfcc
