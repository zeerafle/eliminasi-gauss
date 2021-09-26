from setuptools import setup

setup(
    name='elminasigauss',
    py_modules=['eliminasigauss'],
    install_requires=[
        'Click',
        'numpy',
    ],
    entry_points='''
        [console_scripts]
        gauss=eliminasigauss:eliminasi_gauss_naif
    ''',
)