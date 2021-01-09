from setuptools import setup

setup(name='monitor_manager',
    url='https://github.com/carlos.devworks/monitor_manager',
    project_urls={
        'Documentation': 'https://carlos.devworks.github.io/monitor_manager',
    },
    license='MIT',
    author='carlos.devworks',
    author_email='carlos.devworks@protonmail.com',
    packages=['monitor_manager'],
    install_requires=['wmi ; platform_system=="Windows"'],
    description='A Python module to caputre and change monitor brightness on Windows and Linux',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only'
    ],
    python_requires='>=3.6'
    )

