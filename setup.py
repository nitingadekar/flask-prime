from setuptools import setup, find_packages

requires = [
    'flask',
    'flask-sqlalchemy',
    'os'
]

setup(
    name='prime_flask',
    version='0.0',
    description='A two sided prime no. check rest api with Flask',
    author='Nitin Gadekar',
    author_email='niteengadekar@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)
