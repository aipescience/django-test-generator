from setuptools import setup, find_packages

version = 'v0.1.2'

setup(
    name='django-test-generator',
    packages=find_packages(),
    license=u'Apache License (2.0)',
    version=version,
    description='A set of mixins to automatically generate test for generic Django views and DRF Viewsets.',
    author='Jochen Klar',
    author_email='jklar@aip.de',
    maintainer=u'AIP E-Science',
    maintainer_email=u'escience@aip.de',
    url='https://github.com/aipescience/django-test-generator',
    download_url='https://github.com/aipescience/django-test-generator/archive/%s.tar.gz' % version,
    keywords=['testing', 'django'],
    classifiers=[],
)
