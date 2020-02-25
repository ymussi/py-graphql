from setuptools import setup, find_packages

# read the contents of your README file
# from os import path
# this_directory = path.abspath(path.dirname(__file__))
# with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

setup(
    name='pygraphql',
    # other arguments omitted
    # long_description=long_description,
    # long_description_content_type='text/markdown',
    version = '0.0.1',
    setup_requires=["setuptools-git-version"],
    packages = find_packages(),
    description='Estudando o GraphQL',
    author='Yuri Mussi',
    author_email='ymussi@gmail.com',
    license='BSD',
    url='https://github.com/ymussi/py-graphql.git',
    keywords = "Mussi",
    install_requires = ['flask',
                        'Flask-GraphQL==2.0.1',
                        'graphene==2.1.8'],
    zip_safe=False
    ),
