from setuptools import setup

requires = ["requests>=2.14.2"]

setup(
    name='your_package',
    version='0.1',
    description='Awesome library',
    url='https://github.com/whatever/whatever',
    author='yourname',
    author_email='your@address.com',
    license='MIT',
    keywords='sample setuptools development',
    packages=[
        "your_package",
        "your_package.subpackage",
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
