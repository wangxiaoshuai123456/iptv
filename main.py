# coding=utf-8
import os
import pytest
import sys

if __name__ == '__main__':
    # sys.path.append('/root/jenkins-auto-test-build')
    # sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '/root/jenkins-auto-test-build')))
    pytest.main()
    os.system("allure generate ./allure-results -o  allure-report --clean")
