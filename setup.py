# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(name='cloud-utils',
      version='1.0',
      description='Python Cloud Utilities',
      author='Arie Abramovici',
      author_email='beast@google.com',
      packages=['cloud_utils'],
      entry_points={'console_scripts': ['list_instances = cloud_utils.list_instances:main']},
      install_requires=['boto', 'boto3', 'botocore', 'google-api-python-client',
                        'google-auth', 'texttable', 'futures', 'python-dateutil', 'pytz'],
      zip_safe=False)
