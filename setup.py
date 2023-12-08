from setuptools import find_packages, setup

setup(
    name="py-tvm-server",
    version="0.0.1",
    description="TVM executor as a server",
    license="MIT",
    packages=find_packages(exclude=["test"]),
    author="Amin Rezaei",
    author_email="a.rezaei@top.team",
    keywords=[],
    entry_points={
        "console_scripts": [
        ],
    },
    url="https://github.com/AminRezaei0x443/py-tvm-server",
    install_requires=[],
    extras_require={},
)
