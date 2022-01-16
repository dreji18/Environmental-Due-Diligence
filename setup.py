############################################################################################
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
############################################################################################
from setuptools import setup, find_packages

def readme():
    with open("README.md") as f:
        README = f.read()
    return README


#with open("requirements.txt") as f:
#    required = f.read().splitlines()

#with open("requirements-optional.txt") as f:
#    optional_required = f.read().splitlines()

setup(
    name="EnvBert",
    version="0.2.2",
    description="Predicts classes of environmental due diligence",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/dreji18/environmental-due-diligence",
    author="Afreen Aman, Deepak John Reji",
    author_email="afreenaman90@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    package_dir={'EnvBert':'EnvBert'},
    package_data={'EnvBert': ['data/*.csv']},
    license_files=("LICENSE",),
    install_requires=['numpy>=1.19.5', 'transformers>=4.6.1', 'tensorflow>=2.1.0', 'sklearn', 'pandas', 'sentence_transformers>=2.1.0']
    #extras_require={"full": optional_required,},
)