# M87* – Chandra X-Ray Sources

This dataset contains the 10 brightest X-ray point sources detected in the central region of the galaxy M87, observed by the Chandra X-Ray Observatory. These sources are likely associated with globular clusters or compact objects near the supermassive black hole M87*.

## Columns

| Column              | Description                                      | Units         |
|---------------------|--------------------------------------------------|---------------|
| `source_id`         | Chandra source identifier                        | —             |
| `RA`, `Dec`         | Right ascension and declination (J2000)          | Degrees       |
| `Lx`                | X-ray luminosity (0.3–10 keV)                     | erg/s         |
| `Count_Rate`        | Background-corrected count rate                  | counts/sec    |
| `Hardness_Ratio_21` | (M−S)/(M+S) ratio between medium and soft bands  | —             |
| `Hardness_Ratio_31` | (H−S)/(H+S) ratio between hard and soft bands    | —             |
| `ACS_Obsflag`       | Flag indicating presence in HST ACS field        | 0 or 1        |
| `Optical_Ctrpart`   | Optical counterpart classification               | —             |

## Notes

- All values are extracted from the M87CXO catalog (Chandra 2000–2002).
- Luminosities are computed assuming a distance of 16 Mpc.
- Hardness ratios are indicators of spectral energy distribution.
- This dataset is compatible with Axis_W. You may compute:
  - `velocity_sim` via proxy from `Lx` or `Hardness_Ratio`
  - `omega_W` using your preferred torsion model

## Sources

- Chandra M87CXO Catalog (NASA HEASARC)
- Event Horizon Telescope Collaboration (2019–2024)
- Caltech Imaging Team (Bouman et al.)

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

