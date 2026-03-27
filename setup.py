from setuptools import find_packages, setup
import os

version = '1.4.2'

def readme():
    if os.path.exists('README.md'):
        with open('README.md', encoding='utf-8') as f:
            return f.read()
    return "Fixed BasicSR for Easy-Wav2Lip"

setup(
    name='basicsr',
    version=version,
    description='Open Source Image and Video Restoration Toolbox (Fixed)',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/codescv/basicsr',
    author='XPixel Group',
    python_requires='>=3.7',
    license='Apache License 2.0',
    # 彻底删除 setup_requires=['numpy']，避开源码编译和安全拦截
    install_requires=[
        'addict',
        'future',
        'lmdb',
        'numpy<2.0.0',
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
