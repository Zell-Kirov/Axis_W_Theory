# Sgr A* – Orbital Parameters of S-stars

This dataset contains confirmed orbital parameters for nine S-stars orbiting the supermassive black hole at the center of the Milky Way (Sgr A*). All data are sourced from peer-reviewed publications, primarily from the GRAVITY Collaboration, Gillessen et al., and Peißker et al.

## Columns

| Column       | Description                                      | Units         |
|--------------|--------------------------------------------------|---------------|
| `name`       | Identifier of the S-star                         | —             |
| `mass`       | Stellar mass                                     | Solar masses (M☉) |
| `temperature`| Effective temperature                            | Kelvin (K)    |
| `eccentricity`| Orbital eccentricity                            | —             |
| `inclination`| Orbital inclination                              | Degrees       |
| `omega`      | Argument of periapsis                            | Degrees       |
| `Omega`      | Longitude of ascending node                      | Degrees       |
| `Tp`         | Time of periapsis passage                        | Julian year   |
| `P`          | Orbital period                                   | Years         |
| `q`          | Periapsis distance                               | Astronomical Units (AU) |
| `v`          | Velocity at periapsis                            | km/s          |

## Notes

- All values are taken directly from published orbital fits.
- No values are estimated or simulated.
- This dataset is compatible with the Axis_W model. You may compute:
  - `velocity_sim = v / 3e5`
  - `mass_sim = mass`
  - `omega_W` using your preferred torsion model

## Sources

- GRAVITY Collaboration (2018–2020)
- Gillessen et al. (2009, 2017)
- Peißker et al. (2020)

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

