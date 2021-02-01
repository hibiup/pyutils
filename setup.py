"""
Example of how to use setuptools
"""

__version__ = "1.0.0"

from setuptools import setup, find_packages


# Read description from README file.
def long_description():
    from os import path
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        return f.read()


def get_depends():
    with open('requirements.txt') as f:
        return f.read().splitlines()


# 使用 unittest 测试框架
import unittest
def get_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup(
    author='Jeff Wang',
    author_email='jeffwji@test.com',
    name="pyutils",
    long_description=long_description(),

    # 命令行："python setup.py --version" 可以获得版本号。
    version=__version__,

    ### 指定或排除目录或模块：
    # find_package 想限制查找的访问，以下表示查找除了 tests 和 test 目录之外的所有其他目录下的项目文件。
    packages=find_packages(
        exclude=['tests', 'test']
    ),

    install_requires=get_depends(),

    # python setup.py test
    test_suite='setup.get_test_suite',
)
