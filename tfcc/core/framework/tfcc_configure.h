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

#include <map>
#include <string>
#include <tuple>
#include <utility>

#include "utils/tfcc_spinlock.h"

namespace tfcc {

class Scope;

template <class T>
class Configure {
  SpinLock _mtx;
  std::map<std::tuple<const Scope*, std::string>, T> _dataMap;

 private:
  static Configure& getDefault();

 private:
  Configure();

 public:
  static T getConfigure(const std::string& name, bool& existed);
  static T getConfigure(const std::string& name, T defaultValue);
  static T getConfigure(const std::string& name);
  static void removeConfigures(const Scope* scope);
};

}  // namespace tfcc
