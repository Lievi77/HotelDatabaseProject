from setuptools import setup

setup(
    name="travelCLI",
    version="1.0",
    description='CLI Tool for travelApp Database for CSI2132',
    author='Christopher Aris',
    py_modules=["controller"],
    install_requires=[
        'Click', 
        'psycopg2',
        'colorama'
    ],
    entry_points= '''
        [console_scripts]
        controller=controller:session
    '''
)