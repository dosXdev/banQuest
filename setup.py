from setuptools import find_packages, setup
import os

# Get more https://pypi.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS = [
    "Development Status :: Stable",
    # Product description
    "Environment :: Web Environment",
    "Framework :: Django",
    "Intended Audience :: Customers",
    # Licence used (none yet)
    # "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent",
    # Supported versions, Python 2, Python 3 or both.
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Internet :: WWW/HTTP :: WSGI",
    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
    "Topic :: Software Development :: Libraries :: Python Modules",
]

EXCLUDE_FROM_PACKAGES = ["project","project.*"]

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name="bankQuest",
    version="1.0.0",
    description="TBD",
    long_description=read('README.md (TBD)'),
    classifiers=CLASSIFIERS,
    keywords="TBD",
    author="TBD",
    author_email="TBD",
    maintainer="TBD",
    maintainer_email="TBD",
    url="TBD (github link)",
    license="GPL",
    platforms="OS Independent",
    install_requires=["Django==5.0.2"],
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    zip_safe=False,
    project_urls={
        'Documentation': 'https://docs.djangoproject.com/',
        'Funding': 'TBD',
        'Source': 'TBD',
        'Tracker': 'TBD',
    },
)
