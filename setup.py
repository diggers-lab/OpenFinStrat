from setuptools import find_packages, setup
setup(
    name='OpenFinStrat',
    packages=find_packages(include=['OpenFinStrat']),
    version='0.1.0',
    description='Financial Strategies Library with backtesting framework',
    author='Benjamin  Scialom & Yassir Ouchani',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)