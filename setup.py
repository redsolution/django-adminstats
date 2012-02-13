from setuptools import setup, find_packages
import sys, os

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(name='django-adminstat',
    version=__import__('adminstat').__version__,
    long_description=read('README'),
    description=read('DESCRIPTION'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: Russian',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Utilities',
        ],
    keywords='django admin log',
    author='Ivan Gromov',
    author_email='ivan.gromov@redsolution.ru',
    url='',
    license="AGPLv3",
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Django',],
)
