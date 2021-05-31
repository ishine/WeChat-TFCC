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

#include "framework/tfcc_shape.h"
#include "framework/tfcc_variable.h"

namespace tfcc {
namespace relation {

/**
 * Calculate a == b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> equal(const Tensor<T>& a, T b);

/**
 * Calculate a == b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> equal(T a, const Tensor<T>& b);

/**
 * Calculate a == b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> equal(const Tensor<T>& a, const Tensor<T>& b);

/**
 * Calculate a != b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> unequal(const Tensor<T>& a, T b);

/**
 * Calculate a == b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> unequal(T a, const Tensor<T>& b);

/**
 * Calculate a == b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> unequal(const Tensor<T>& a, const Tensor<T>& b);

/**
 * Calculate a > b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> greater(const Tensor<T>& a, T b);

/**
 * Calculate a > b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> greater(T a, const Tensor<T>& b);

/**
 * Calculate a > b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> greater(const Tensor<T>& a, const Tensor<T>& b);

/**
 * Calculate a >= b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> greater_equal(const Tensor<T>& a, T b);

/**
 * Calculate a >= b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> greater_equal(T a, const Tensor<T>& b);

/**
 * Calculate a >= b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> greater_equal(const Tensor<T>& a, const Tensor<T>& b);

/**
 * Calculate a < b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> less(const Tensor<T>& a, T b);

/**
 * Calculate a < b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> less(T a, const Tensor<T>& b);

/**
 * Calculate a < b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> less(const Tensor<T>& a, const Tensor<T>& b);

/**
 * Calculate a <= b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> less_equal(const Tensor<T>& a, T b);

/**
 * Calculate a <= b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> less_equal(T a, const Tensor<T>& b);

/**
 * Calculate a <= b.
 * NOTE: This function support broadcasting.
 * @param a A tensor.
 * @param b A tensor.
 * @return A variable.
 */
template <class T>
Variable<uint8_t> less_equal(const Tensor<T>& a, const Tensor<T>& b);

}  // namespace relation
}  // namespace tfcc
