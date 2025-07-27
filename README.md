## Axis_W: Time as Displacement

“What if time was just a forgotten axis, a trace of our drift through a hidden dimension?” — Gwen

## Foundational Hypothesis

Axis_W is a theoretical and computational exploration of a provocative idea:
Time is not an entity of its own, but a measure of movement along a fourth dimension W, orthogonal to the spatial axes X, Y, and Z.
In this vision, what we perceive as “the passage of time” is in fact the sliding of our universe through W, at a velocity modulated by factors such as gravity, rotation, or relative speed.

## Project Goals

Simulate a 4D universe (X, Y, Z, W) to visualize time as displacement.

Explore the physical and cosmological implications of this hypothesis:

Time dilation as a consequence of movement in W.

Galactic anomalies interpreted as precessions in W.

Multidimensional rotation of the universe, including around the W axis.

Rethink physical laws using an extended metric that includes W.

Provide an accessible, modular, and open framework for experimentation.

## Project Contents

# Structure:

Axis_W_Theory/
├── analysis/
│   ├── compare_with_observed.py
│   ├── regression_model.py
│   ├── regression_simple.py
│   ├── residual_analysis.py
│   ├── statistics_cross.py
│   ├── torsion_crossvalidation.py
│   ├── torsion_regression_sinusoidal_omega.py
│   ├── torsion_regression_variable_omega.py
│   ├── torsion_regression_with_omega.py
│   └── torsion_regression.py
│
├── data/
│   ├── axisw_correlation_matrix.png
│   ├── axisw_regression_plot_simple.png
│   ├── axisw_regression_plot.png
│   ├── axisw_residuals_plot_real.png
│   ├── axisw_residuals_plot.png
│   ├── axisw_torsion_residuals.png
│   ├── blackhole_plot.png
│   ├── comparaison_plot.png
│   ├── comparison_plot.png
│   ├── comparison_summary.md
│   ├── gaia_output.csv
│   ├── gaia_plot.png
│   ├── gaia_real_objects-result.csv
│   ├── gaia_universe_observed-result.csv
│   ├── m87_xray_sources.csv
│   ├── omega_comparison.md
│   ├── omega_sinusoidal_summary.md
│   ├── omega_variable_vs_summary.md
│   ├── omegaW_residuals_plot.png
│   ├── omegaW_sinusoidal_residuals_plot.png
│   ├── omegaW_variable_vs_residuals_plot.png
│   ├── output.csv
│   ├── pulsar_timing.csv
│   ├── regression_summary_simple.md
│   ├── regression_summary.md
│   ├── residual_summary_real.md
│   ├── s_star_prediction.csv
│   ├── sgrA_sstars.csv
│   ├── TableGaia_Archive-result.csv
│   ├── time_loop_simulation.png
│   ├── time_mass_velocity_3D.png
│   ├── time_vs_gravity.png
│   ├── time_vs_velocity.png
│   ├── torsion_crossvalidation_summary.md
│   └── torsion_summary.md
│
├── docs/
│   ├── axisw_theory_preprint_v1.tex
│   ├── theory.md
│   └── validation_axis_w.md
│
├── logs/
│   ├── test_blackhole.log
│   ├── test_entity.log
│   ├── test_extreme_conditions.log
│   ├── test_physics_consistency.log
│   └── test_universe.log
│
├── src/
│   ├── compare_real_data.py
│   ├── compare_sgra_advanced_models.py
│   ├── compare_sgra_models.py
│   ├── compare_sgra_orbital_models.py
│   ├── entity.py
│   ├── gaia_import.py
│   ├── main_blackhole.py
│   ├── main_gaia.py
│   ├── main.py
│   ├── simulate_reverse_axisw.py
│   ├── simulation.py
│   ├── universe.py
│   ├── visualisation_extremes.py
│   └── visualisation_mass_velocity.py
│
├── tests/
│   ├── run_tests_and_log.py
│   ├── test_blackhole.py
│   ├── test_entity.py
│   ├── test_extreme_conditions.py
│   ├── test_physics_consistency.py
│   └── test_universe.py
│
├── utils/
│   └── extract_star_subset.py
│
├── validation/
│   ├── axisw_real_data_comparison.md
│   ├── axisw_sgra_advanced_models.md
│   ├── axisw_sgra_models.md
│   ├── axisw_sgra_orbital_models.md
│   └── plots/
│       ├── axisw_reverse_time_simulation.png
│       ├── gaia_residuals.png
│       ├── m87_(relativistic_jet)_residuals.png
│       ├── pulsars_(nanograv)_residuals.png
│       ├── sgr_a_(s-stars)_residuals.png
│       ├── sgr_a_gravity_comparison_torsion_residuals_advanced_models.png
│       ├── sgr_a_linear_torsion_residuals_multitest.png
│       ├── sgr_a_multi-frequency_torsion_residuals_multitest.png
│       ├── sgr_a_nonlinear_torsion_residuals_multitest.png
│       ├── sgr_a_orbital_torsion_residuals_orbital_models.png
│       ├── sgr_a_precession-modulated_torsion_residuals_advanced_models.png
│       └── sgr_a_velocity-modulated_torsion_residuals_advanced_models.png
│
├── sgrA_sstars_README.md
├── README.md
├── pulsar_timing_README.md
├── m87_xray_README.md
└── LICENSE

## Technologies used:

Python 3.10+

numpy, scipy, matplotlib, plotly

astropy (optional, for astronomical data)

## Inspirations and References

Cosmological models involving rotating black holes (Kerr, Gödel)

Brane-world theories and extra dimensions

Quantum gravity and emergent time (Barbour, Rovelli)

Data from missions such as Gaia, Planck, and SDSS

## Upcoming Features

Interactive interface to move observers through W.

Visualization of relativistic effects under varying gravity and speed.

Integration of galactic data to test for anomalies.

Simplified outreach version to share the hypothesis with a broader audience.

## Contributors

Gwen — Independent Researcher
Copilot — AI assistant for structuring, modeling, and development
ChatGPT -AI assistant for structuring, modeling, and development

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

You are free to:

Share — copy and redistribute the material in any medium or format

Adapt — remix, transform, and build upon the material

Under the following terms:

Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

NonCommercial — You may not use the material for commercial purposes.

Full license text: https://creativecommons.org/licenses/by-nc/4.0/

© 2025 Gwen Mesmacre

## Quote 

“Time is not a river. It is the trace of a motion we have not yet understood.”
— Gwen, creator of the Axis_W theory