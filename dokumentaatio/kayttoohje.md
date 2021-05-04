# Käyttöohje

## Ohjelman käynnistäminen

Ohjelma käynnistetään projektin juuresta komennolla:
``` bash
poetry run invoke start
```

Jos käyttäjä haluaa, niin hän voi tyhjentää käyttäjien tietokannan komennolla:
``` bash
poetry run invoke build
```

## Sisäänkirjautuminen

Ohjelma tukee käyttäjä-tilejä. Käyttäjän tulee siis ennen käyttöä kirjautua sisään tai luoda uusi tunnus.

## Harjoituksien valitseminen

Sisäänkirjauduttuaan käyttäjä voi valita eri harjoitusmuotoja tai muuttaa niiden asetuksia Settings-näkymästä.

## Asetukset

Asetusnäkymässä on listassa kaikki harjoituksien eri asetukset kategorioittain. Asetuksia voi vaihtaa kirjoittamalla uuden
arvon kenttään ja painamalla 'Accept'-nappia, jonka jälkeen ohjelma tallentaa uudet hyväksytyt asetukset tiedostoon.

## Harjoittelu

Harjoittelunäkymässä on näkyy uusi halutun tyyppinen kysymys, käytetty aika ja (jos päällä) jäljellä oleva aika. Vastaukset tehdään kirjoittamalla kenttään
näppäimistöllä ja painamalla enteriä. Käyttäjä voi myös käyttää ruudulla näkyvää 'Answer'-nappia. Kun käyttäjä on vastannut, valitsee ohjelma uuden kysymyksen
ja näyttää sen ruudulla, sekä oliko edellinen oikein ja edelliseen kysymykseen kuluneen ajan. Näkymästä pääsee takaisin painamalla 'Back'-nappia.
