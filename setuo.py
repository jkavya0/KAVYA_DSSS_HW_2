from setuptools import setup, find_packages

setup(
    name='math_quiz_game',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your project may have
        'numpy',
    ],
    entry_points={
        'console_scripts': [
            'math_quiz = math_quiz:math_quiz',
        ],
    },
    tests_require=[
        'unittest',
    ],
    test_suite='tests',
)
