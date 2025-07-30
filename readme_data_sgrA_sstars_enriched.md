# README — Fichier `data_upgrade/sgrA_sstars.csv`

## Description générale

Ce fichier contient les paramètres observés et estimés pour 30 étoiles proches du trou noir supermassif Sgr A\*, basés sur les données GRAVITY, EHT, et SIMBAD. Il sert de socle au modèle Axis_W de modélisation magnétogravitationnelle perceptive.

## Colonnes et significations

| Colonne        | Description                                                                                  |
|----------------|----------------------------------------------------------------------------------------------|
| `name`         | Nom identifiant SIMBAD ou GRAVITY                                                            |
| `mass`         | Masse stellaire \( M_\odot \)                                                                |
| `g`            | Gravité surfacique (cm/s²)                                                                    |
| `Teff`         | Température effective de la surface stellaire (Kelvin)                                        |
| `r_star`       | Rayon stellaire estimé (rayons solaires), basé sur masse et température                     |
| `r_env`        | Rayon gravitationnel d’influence locale autour de l’étoile                                   |
| `B_field`      | Champ magnétique local estimé (\( \mu G \))                                                  |
| `temperature`  | Température environnementale de la zone orbitale (Kelvin)                                    |
| `eccentricity` | Excentricité orbitale                                                                         |
| `inclination`  | Inclinaison orbitale (degrés)                                                                 |
| `omega`        | Argument du périastre (degrés)                                                                |
| `Omega`        | Longitude du nœud ascendant (degrés)                                                          |
| `Tp`           | Temps du passage au périastre (jours ou années, selon données GRAVITY)                       |
| `P`            | Période orbitale (années)                                                                     |
| `q`            | Distance au périapse (\( r_{\text{min}} \), parsecs)                                         |
| `v`            | Vitesse orbitale actuelle (km/s)                                                              |

## Équations utilisées pour les estimations

- Rayon stellaire :
  $$ r_\text{star} \approx M^{0.8} \cdot \left(\frac{T}{5778}\right)^{-0.5} $$

- Rayon gravitationnel local :
  $$ r_\text{env} \approx q \cdot \left(\frac{M}{M_{BH}}\right)^{1/3} $$  
  avec \( M_{BH} = 4 \times 10^6~M_\odot \)

- Champ magnétique estimé :
  $$ B(r) \approx B_0 \cdot \left(\frac{r}{r_0}\right)^{-\alpha} $$  
  \( B_0 = 1000~\mu G, \quad r_0 = 0.1~pc, \quad \alpha \approx 1 \)

## Références scientifiques

- Peißker et al., *Astronomy & Astrophysics* (2020–2022)
- GRAVITY Collaboration, *Nature* et *A&A* (2018–2023)
- Gillessen et al. (2017), orbital data et modèles relativistes
- Event Horizon Telescope (EHT), polarisation et champ magnétique de Sgr A\*

## Limitations et hypothèses

- Les estimations de `r_star`, `r_env` et `B_field` sont valables pour étoiles de type séquence principale.
- Le champ magnétique est calculé via décroissance radiale simple ; variations locales non incluses.
- La précision des orbites dépend des publications GRAVITY ; les incertitudes sont minimisées mais non nulles.

## Usage pour Axis_W

- Calcul du ratio \( r_\text{env} / r_\text{star} \) — indicateur de confinement gravitationnel local
- Analyse croisée `B_field` vs. `r_env` — modélisation magnétogravitationnelle
- Modélisation des vitesses perceptives et cartographie tensorielle du noyau galactique

---

