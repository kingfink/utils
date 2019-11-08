from setuptools import setup, find_packages

setup(
    name='utils',
    version=0,
    description='Personal utilities',
    url='https://github.com/kingfink/utils',
    author='Tim Finkel',
    license='',
    packages=find_packages(),
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'u=utils.cli:main'
        ]
    },
    install_requires=[
        'pyperclip'
    ]
)