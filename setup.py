""" Password strength and validation """

from promebuilder import gen_metadata, setup

METADATA = gen_metadata(
    name='password_strength',
    email="pytho_support@prometeia.com",
    url='https://github.com/prometeia/py-password-strength',
    description=__doc__,
    keywords=['password', 'strength', 'policy', 'security'],
)

METADATA.update(dict(
    author='Mark Vartanyan',
    author_email='kolypto@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
))

if METADATA.get('conda_command_tests'):
    # Disabling for generic problem with mplotqueries
    METADATA['conda_command_tests'] = False
if METADATA.get('conda_import_tests'):
    # Disabling for generic problem with mplotqueries
    METADATA['conda_import_tests'] = False


if __name__ == '__main__':
    setup(METADATA)