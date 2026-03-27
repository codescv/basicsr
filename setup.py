from setuptools import find_packages, setup
import os

version = '1.4.2'

def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

setup(
    name='basicsr',
    version=version,
    description='Open Source Image and Video Restoration Toolbox',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/XPixelGroup/BasicSR',
    author='XPixel Group',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
    ],
    license='Apache License 2.0',
    setup_requires=['numpy'],
    install_requires=[
        'addict',
        'future',
        'lmdb',
        'numpy',
        'opencv-python',
        'pillow',
        'pyyaml',
        'requests',
        'scikit-image',
        'scipy',
        'tqdm',
    ],
    packages=find_packages(exclude=('options', 'datasets', 'models', 'trainers', 'utils')),
    zip_safe=False)
