from setuptools import setup, find_packages

setup(
    name='django-maintenance-mode',
    version='0.1.0',
    description='A Django package to manage maintenance mode.',
    author='Reza Bayat',
    author_email='mrrezabayat@gmail.com',
    url='https://github.com/reza-bayat/django-maintenance-mode',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)