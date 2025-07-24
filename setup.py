from setuptools import setup, find_packages

setup(
    name='openai_tracker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'requests',
        'tiktoken',
    ],
    entry_points={
        'console_scripts': [
            'openai-tracker=openai_tracker.main:main',
        ],
    },
)
