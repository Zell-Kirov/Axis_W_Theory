# NANOGrav Pulsar Timing Dataset

This dataset contains timing residuals and observational parameters for five well-studied millisecond pulsars from the NANOGrav 15-Year Data Set. These pulsars are known for their exceptional rotational stability and are used in gravitational wave detection efforts.

## Columns

| Column         | Description                                 | Units         |
|----------------|---------------------------------------------|---------------|
| `name`         | Pulsar identifier                           | —             |
| `MJD`          | Modified Julian Date of observation         | days          |
| `residual_us`  | Timing residual                             | microseconds  |
| `frequency_MHz`| Observing frequency                         | MHz           |
| `period_s`     | Pulsar rotation period                      | seconds       |
| `DM`           | Dispersion measure                          | pc/cm³        |

## Notes

- Residuals are derived from `.tim` and `.par` files using PINT.
- All data are real and sourced from NANOGrav’s public release.
- This dataset is compatible with Axis_W. You may compute:
  - `velocity_sim` via proxy from `period_s` and `residual_us`
  - `omega_W` using your preferred torsion model

## Sources

- NANOGrav 15-Year Data Set (https://nanograv.org/science/data)
- PINT Timing Software (https://github.com/nanograv/PINT)

## License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0).

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
- NonCommercial — You may not use the material for commercial purposes.

Full license text: https://creativecommons.org/licenses/by-nc/4.0/

© 2025 Gwen Mesmacre

