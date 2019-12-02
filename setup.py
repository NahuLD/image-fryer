from setuptools import setup, find_packages

from fryer import VERSION

with open('requirements.txt') as req:
    requirements = req.readlines()

with open('README.md') as read:
    readme = read.read()

setup(
    name='image-fryer',
    author='NahuLD',
    author_email='contact@nahu.me',
    url='https://github.com/NahuLD/image-fryer',
    version=VERSION,
    packages=find_packages(),
    license='MIT',
    description='Your favorite deep frying image library',
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)
