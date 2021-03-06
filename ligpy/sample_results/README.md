# Sample results using DDASAC

This directory contains two folders with sample output generated from running `ligpy.py` on cmole.  cmole is the computer at the University of Washington where the original work for this paper was completed, and several of the modules in this package are specific to cmole's directory structure and software environment (see the documentation).

This directory has been included so that future users can see the output format that was generated on cmole using our modified DDASAC code, and to provide sample files for use with the `explore_ligpy_results` notebook.  If users would like to use our analysis scripts to generate plots or compute lumped yields, etc, they should reformat the results from their ODE solvers to match the format shown in the `ddasac_results_1.out` file in the results_dir folder of these sample simulations (or revise the analysis code to reflect their result structure).
