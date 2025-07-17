from setuptools import setup, find_packages

setup(
    name='django-inline-actions',
    version='2.1-patched',
    description='Inline actions for Django admin (patched)',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=2.2',
    ],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
    ],
)
