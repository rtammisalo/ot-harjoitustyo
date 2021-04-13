# Ohjelmistotekniikan harjoitustyö
## Sovellus
Sovellus on aritmetiikan harjoitustyökalu. Käyttäjä voi harjoitella kerto-, jako-, yhteen- ja vähennyslaskuja satunnaisilla tehtävillä. Käyttäjä voi myös muuttaa tehtävien asetuksia.

Tällä hetkellä on vain toteutettu sisäänkirjautuminen ja kertolasku ilman asetuksien vaihtamista.

## Asennusohjeet

```bash
poetry install
```

## Käyttöohjeet

Ohjelma ei vielä tallenna mitään tietokantaan, joten ei tarvita erillisiä `build` komentoja. Aja ohjelma komennolla:
```bash
poetry run invoke start
``` 

Testaus ja testikattavuus:
```bash
poetry run invoke test
poetry run invoke coverage-report
```

## Määrittelydokumentti
[Vaatimusmäärittely](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

## Tuntikirjanpito
[Tunnit](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/tunnit.md)
