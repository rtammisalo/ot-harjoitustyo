# Ohjelmistotekniikan harjoitustyö
## Sovellus
Sovellus on aritmetiikan harjoitustyökalu. Käyttäjä voi harjoitella kerto-, jako-, yhteen- ja vähennyslaskuja satunnaisilla tehtävillä. Käyttäjä voi myös muuttaa tehtävien asetuksia. Käyttäjällä on oma tili ja tilillä henkilökohtaiset asetustiedostot eri harjoituksiin.

Tällä hetkellä on vielä toteuttamatta vain satunnaisharjoittelu alkuperäisestä määrittelydokumentista.

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

Pylint:
```bash
poetry run invoke lint
```

## Releases
### Release 1 (viikko 5)
[Release 1](https://github.com/rtammisalo/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio
### Määrittelydokumentti
[Vaatimusmäärittely](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

### Tuntikirjanpito
[Tunnit](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/tunnit.md)

### Arkkitehtuuri
[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
