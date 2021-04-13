# Ohjelmistotekniikan harjoitustyö
## Sovellus
Sovellus on aritmetiikan harjoitustyökalu. Käyttäjä voi harjoitella kerto-, jako-, yhteen- ja vähennyslaskuja satunnaisilla tehtävillä. Käyttäjä voi myös muuttaa tehtävien asetuksia.

Tällä hetkellä on vain toteutettu sisäänkirjautuminen ja kertolasku ilman asetuksien vaihtamista.

## Asennusohjeet

Asennus ohjeet ovat samat kuin referenssisovelluksessa, mutta kirjataan ne ylös:
```bash
poetry install
```
Käynnistykseen ei tarvita build komentoja vielä:
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
