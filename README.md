# Ohjelmistotekniikan harjoitustyö
## Sovellus
Sovellus on aritmetiikan harjoitustyökalu. Käyttäjä voi harjoitella kerto-, jako-, yhteen- ja vähennyslaskuja satunnaisilla tehtävillä. Käyttäjä voi myös muuttaa tehtävien asetuksia.

Tällä hetkellä on vielä toteuttamatta muut harjoitusnäkymät kuin kertolaskuharjoitukset. 

## Asennusohjeet

```bash
poetry install
```

## Käyttöohjeet

Ohjelma käyttää tietokantaa käyttäjien tallentamiseen. Aja ensin  `build` komento. 
```bash
poetry run invoke build
```

Aja ohjelma komennolla:
```bash
poetry run invoke start
``` 

Testaus ja testikattavuus:
```bash
poetry run invoke test
poetry run invoke coverage-report
```

## Dokumentaatio
### Määrittelydokumentti
[Vaatimusmäärittely](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

### Tuntikirjanpito
[Tunnit](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/tunnit.md)

### Arkkitehtuuri
[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
