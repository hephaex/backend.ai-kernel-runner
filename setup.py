from setuptools import setup, find_packages
from pathlib import Path

from ai.backend.kernel.version import VERSION


requires = [
    'async_timeout>=1.1',
    'aiozmq>=0.7',
    'uvloop>=0.8',
    'simplejson',
    'namedlist',
    'janus',
    'msgpack-python',
]
build_requires = [
    'wheel',
    'twine',
]
test_requires = [
    'pytest>=3.1',
    'pytest-asyncio',
    'pytest-mock',
    'asynctest',
    'flake8',
]
dev_requires = build_requires + test_requires + [
    'pytest-sugar',
]
ci_requires = []


setup(
    name='backend.ai-kernel-runner',
    version=VERSION,
    description='User code executors for Backend.AI kernels',
    long_description=Path('README.rst').read_text(),
    url='https://github.com/lablup/backend.ai-kernel-runner',
    author='Lablup Inc.',
    author_email='joongi@lablup.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Environment :: No Input/Output (Daemon)',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    packages=[
        'ai.backend.kernel',
        'ai.backend.kernel.python',
        'ai.backend.kernel.c',
        'ai.backend.kernel.cpp',
        'ai.backend.kernel.golang',
        'ai.backend.kernel.rust',
        'ai.backend.kernel.java',
        'ai.backend.kernel.haskell',
    ],
    python_requires='>=3.6',
    install_requires=requires,
    extras_require={
        'build': build_requires,
        'test': test_requires,
        'dev': dev_requires,
        'ci': ci_requires,
        # kernel-specific requirements
        'python': ['IPython', 'pandas', 'numpy', 'matplotlib'],
        'c': [],
        'cpp': [],
        'golang': [],
        'rust': [],
        'java': [],
        'haskell': [],
    },
)