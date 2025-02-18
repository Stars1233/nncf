# Copyright (c) 2025 Intel Corporation
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tests.cross_fw.install.common import load_nncf_modules

EXCLUDED_MODULES_PATTERNS = (
    "nncf\\.openvino.*",
    "nncf\\.tensorflow.*",
    "nncf\\.torch.*",
    "nncf\\.experimental\\.tensorflow.*",
    "nncf\\.experimental\\.torch.*",
    "nncf\\.experimental\\.openvino.*",
    "^(?!nncf(?:\\.experimental)*\\.onnx.*?\\.).*?openvino_[^\\.]*",
    "^(?!nncf(?:\\.experimental)*\\.onnx.*?\\.).*?torch_[^\\.]*",
    "^(?!nncf(?:\\.experimental)*\\.onnx.*?\\.).*?tf_[^\\.]*",
)

load_nncf_modules(EXCLUDED_MODULES_PATTERNS)
