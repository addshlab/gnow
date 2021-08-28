from setuptools import setup, find_packages

setup(
    name='gnow',
    version='0.1',
    description='This is a wrapper command to make git add/commit/push easier.',
    url='https://github.com/addshlab/gnow',
    author='addshlab',
    author_email='info@add.sh',
    license='MIT',
    keywords='git',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Topic :: Software Development :: Version Control :: Git',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        "console_scripts":[
            "gnow=gnow.command:run",
        ]
    },
)
