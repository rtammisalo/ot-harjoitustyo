# Ohjelmistotekniikan harjoitustyö
## Sovellus
Sovellus on aritmetiikan harjoitustyökalu. Käyttäjä voi harjoitella kerto-, jako-, yhteen- ja vähennyslaskuja satunnaisilla tehtävillä. Käyttäjä voi myös muuttaa tehtävien asetuksia. Käyttäjällä on oma tili ja tilillä henkilökohtaiset asetustiedostot eri harjoituksiin.

Tällä hetkellä on vielä toteuttamatta vain erillinen keypad vastaamiseen alkuperäisestä määrittelydokumentista.

## Asennusohjeet

Aja komento projektin juuressa:
```bash
poetry install
```

## Käyttöohjeet

Ohjelma käyttää tietokantaa käyttäjien tallentamiseen. Uuden tietokannan voi halutessaan luoda ajamalla komento:
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

## Julkaisut

[Release 2, viikko 6](https://github.com/rtammisalo/ot-harjoitustyo/releases/tag/viikko6)

[Release 1, viikko 5](https://github.com/rtammisalo/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

### Käyttöohje
[Käyttöohje](dokumentaatio/kayttoohje.md)

### Määrittelydokumentti
[Vaatimusmäärittely](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

### Tuntikirjanpito
[Tunnit](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/tunnit.md)

### Arkkitehtuuri
[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
