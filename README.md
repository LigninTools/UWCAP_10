### A Kinetic Model for Lignin Pyrolysis (ligpy)
------

Biomass valorization through thermochemical conversion of lignocellulosic feedstocks is limited by our lack of detailed kinetic models. In addition to adding mechanistic understanding, more detailed models are needed to optimize industrial biomass pyrolysis processes for producing fuels and chemicals. To this end, we developed a kinetic model for lignin pyrolysis involving ~100 species and 400 reactions which is capable of predicting the temporal evolution of molecules and functional groups during lignin pyrolysis. The model provides information beyond the lumped yields of common pyrolysis models without any fitting, allowing it to cover a wider range of feedstocks and reaction conditions. Good agreement is observed with slow pyrolysis experiments, and an exhaustive global sensitivity analysis using over two million simulations sheds light on reactions that contribute most to the variance in model predictions (sensitivity analysis results and a package to visualize them are available  [here](https://github.com/houghb/savvy)). Model predictions for fast pyrolysis are available, however, recently developed experimental techniques for kinetically-controlled fast pyrolysis of biomass have yet to be applied to lignin.

*ligpy* is the package developed to solve the kinetic model we describe in our 2016 IECR paper, ***[Detailed kinetic modeling of lignin pyrolysis for process optimization](http://pubs.acs.org/doi/abs/10.1021/acs.iecr.6b02092)***.

Please read the documentation for instructions on using ligpy.

**ligpy documentation:** [![Documentation Status](https://readthedocs.org/projects/ligpy/badge/?version=latest)](http://ligpy.readthedocs.io/en/latest/?badge=latest)  
**Cite ligpy:** [![DOI](https://zenodo.org/badge/doi/10.5281/zenodo.53202.svg)](http://dx.doi.org/10.5281/zenodo.53202)


-------
### Software dependencies and license information

**Programming language:**  
Python version 2.7 (https://www.python.org)

**Python packages needed:**  
NumPy (version 1.10.4 was used but any updated version should be compatible)

The ODE solver that we used for our research is a modified version of DDASAC that is unfortunately not open source.  We chose this solver because it performed the best on the stiff set of ODEs in this model, but future users can modify the code (by replacing our `ddasac_utils.py` module) to use other solvers, such as those in the python package scipy.integrate.

**License information:**   
ligpy is licensed under a BSD 2-clause “Simplified” License. The objective behind this choice of licensing is to make the content reproducible and make it useful for as many people as possible. We want to maximize the two-way collaborations with minimum restrictions, so that developers of other projects can easily utilize, patch, improve, and cite this code. Please refer to the [license](https://github.com/houghb/ligpy/blob/master/LICENSE) for full details.

----------
### Summary of folder contents

**[explore_ligpy_results.ipynb](https://github.com/houghb/ligpy/blob/master/explore_ligpy_results.ipynb)** - This is a Jupyter Notebook that can be used to load the results of lignin pyrolysis simulations generated by ligpy.  It generates detailed reports about the pyrolysis products and offers some plots to get started exploring the data.

**[doc](https://github.com/houghb/ligpy/tree/master/doc)** - Contains the project documentation files that are used to build the documentation at readthedocs.org

**[ligpy](https://github.com/houghb/ligpy/tree/master/ligpy)** - Contains modules to build and run the lignin pyrolysis model.
- `analysis_tools.py`: loads the results from DDASAC output files and performs analysis to describe pyrolysis products in terms of carbon functional groups, concentrations and mass fractions of molecular species, and lumped components.
- `constants.py`: constant values or objects used by other modules.
- `ddasac_utils.py`: functions to setup and run our modified DDASAC solver.  This module will need to be replaced/revised by users without access to DDASAC.
- `equivalent_compositions.py`: calculates the equivalent composition of lignin in terms of our model components from experimental elemental analysis measurements.
- `generate_bash_script.py`: an interactive module that writes a bash script which sets up the proper directory structure and runs the ligpy model on cmole, a computer at the University of Washington.  Future users without access to cmole will need to configure their own script to do this (or it is straightforward to skip this bash script and run ligpy from the command line).
- `ligpy.py`: builds and solves the ligpy kinetic model.
- `ligpy_utils.py`: utility functions used by many of the other modules in this program.
- `read_enthalpies.ipynb`: a notebook for analyzing the density functional theory experiments we performed to assign kinetic parameters for some reactions we added.  This file is included for reference only.
- `revisions_to_faravelli.py`: contains the code we used to make some changes to the original kinetic scheme our model is modified from.  This file is included for reference and should not need to be run in the future.

**[ligpy/data](https://github.com/houghb/ligpy/tree/master/ligpy/data)** - Contains data files that define the reactions and kinetic parameters which make up the kinetic model, and define the initial composition of various lignin species in terms of our model components.

**[ligpy/data/DFT](https://github.com/houghb/ligpy/tree/master/ligpy/data/DFT)** - Contains the files required to set up, and the results from, our DFT analysis that was used to estimate kinetic parameters for new reactions in the scheme.

**[ligpy/sample_results](https://github.com/houghb/ligpy/tree/master/ligpy/sample_results)** - Contains two folders with the results from running the ligpy program using DDASAC.

**[ligpy/tests](https://github.com/houghb/ligpy/tree/master/ligpy/tests)** - Contains unit tests.
