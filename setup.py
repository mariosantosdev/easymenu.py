from setuptools import setup
import os

readme_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
try:
    from m2r import parse_from_file
    readme = parse_from_file(readme_file)
except ImportError:
    # m2r may not be installed in user environment
    with open(readme_file) as f:
        readme = f.read()

setup(
    name='EasyMenu',
    version='0.2.0',
    url='https://github.com/nvrsantos/easymenu.py',
    license='MIT License',
    author='nevr001, KevinAp-5',
    author_email='',
    keywords='menu easy menu_Python python_3.6.x',
    description=u'Uma biblioteca feita para facilitar o desenvolvimento de menu interativo no Python 3.6.x',
    long_description=readme,
    long_description_content_type="text/markdown",
    packages=['EasyMenu'],
    install_requires=['colorama'],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
)
