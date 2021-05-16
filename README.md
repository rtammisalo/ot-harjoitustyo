# Ohjelmistotekniikan harjoitustyö: Aritmetiikan harjoitustyökalu
## Sovellus
Sovellus on tarkoitettu aritmetiikan harjoitteluun. Käyttäjä voi harjoitella kerto-, jako-, yhteen- ja vähennyslaskuja satunnaisilla tehtävillä. Käyttäjä voi myös muuttaa tehtävien asetuksia. Käyttäjällä on oma tili ja tilillä henkilökohtaiset asetustiedostot eri harjoituksiin.

## Asennusohjeet

Asenna Poetry käyttämällä kurssin ohjeita: [Poetryn asennusohjeet](https://ohjelmistotekniikka-hy.github.io/python/poetry).

Poetryn asentamisen jälkeen aja seuraava komento projektin juuressa:
```bash
poetry install
```

## Käyttöohjeet

Ohjelma käyttää tietokantaa käyttäjien tallentamiseen. Jos olet käyttänyt aikaisempia versioita, tulee käyttäjän ensin luoda uusi tietokanta. Uuden tietokannan voi  luoda ajamalla komento:
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

Tehty testikattavuusraportti löytyy projektin juuren alle luodun 'htmlcov' hakemiston 'index.html' tiedostosta.

Pylint:
```bash
poetry run invoke lint
```

## Julkaisut

[Release 2, viikko 6](https://github.com/rtammisalo/ot-harjoitustyo/releases/tag/viikko6)

[Release 1, viikko 5](https://github.com/rtammisalo/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tunnit](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/tunnit.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/testaaminen.md)
