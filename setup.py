try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

opts = dict(name='ligpy',
            description='Detailed kinetic model of lignin pyrolysis',
            long_description='This program constructs and solves a detailed '
                             'kinetic model of lignin pyrolysis as described '
                             'in the journal article linked to in the README '
                             'at https://github.com/houghb/ligpy',
            license=open('LICENSE').read(),
            author='Blake Hough',
            packages=['ligpy', 'ligpy/tests'],
            package_data={'ligpy': ['data/*.*', 'data/DFT/*.*',
                                    'data/DFT/fission_reactions/*.*',
                                    'data/DFT/initiation_reactions/*.*',
                                    'sample_results/README.md',
                                    'sample_results/Pinus_ponderosa-max973K-'
                                    '15.0CperMin-2760.0end-0cool/*.*',
                                    'sample_results/Pinus_ponderosa-max973K-'
                                    '15.0CperMin-2760.0end-0cool/results_dir/'
                                    '*.*',
                                    'sample_results/Pseudotsuga_menziesii-'
                                    'max773K-162.0CperMin-1965.92592593end-'
                                    '0cool/*.*',
                                    'sample_results/Pseudotsuga_menziesii-'
                                    'max773K-162.0CperMin-1965.92592593end-'
                                    '0cool/results_dir/*.*']},
            include_package_data=True
            )


if __name__ == '__main__':
    setup(**opts)
