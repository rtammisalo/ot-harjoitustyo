# Vaatimusmäärittely

## Sovelluksen käyttötarkoitus
Sovellus on aritmetiikan harjoitusohjelma. Ohjelman avulla voi sisäänkirjautunut käyttäjä 
harjoitella nopeita kerto-, jako-, yhteen- ja vähennyslaskuja. Jokaisella käyttäjällä on järjestelmässä
käyttäjänimi ja salasana, jolla hänet autentikoidaan.

## Sovelluksen käyttäjäroolit
Sovelluksella on vain tavallisia käyttäjätilejä. Käyttäjä voidaan tunnistaa uudelleen tilinsä nojalla.

## Käyttöliittymä
Alla kuvassa piirrettynä kevyt luonnos sovelluksen graafisesta käyttöliittymästä.

![Luonnos](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/uiluonnos.png)

Luonnoksesta poiketen toteutettiin asetuksien vaihtaminen erikseen valittavassa asetusnäkymässä.

## Sovelluksen ominaisuudet

- Käyttäjä voi luoda uuden tilin.
  - Tilillä on nimi, salasana ja oma asetustiedosto. Käyttäjän tiedot (nimi ja Passlibillä hashattu salasana) talletetaan tietokantaan.
- Käyttäjä joutuu kirjautumaan sisään omalla tilillään.
  - Kirjautuessaan sisään käyttäjä voi avautuvasta näkymästä valita:
    1. Yhteenlaskuharjoituksia
    2. Vähennyslaskuharjoituksia
    3. Kertolaskuharjoituksia
    4. Jakolaskuharjoituksia
    5. Satunnaisharjoituksia
    6. Tehdä muutoksia harjoituksien asetuksiin (operandien suuruudet, ajastimen käyttö, aikaraja)
  - Harjoituksiin vastataan joko näppäimistöllä tai hiirellä (ikkunaan piirretään vastaamista varten pieni keypad). Harjoituksissa on myös mahdollista käyttää ajastusta.

## Mahdollisia lisäominaisuuksia
- Admin-tili, joka voi tutkia kaikkien käyttäjien tietoja tai tuhota tilejä
- Jonkinlainen "sudden death" tyylinen time attack-harjoitusmuoto, jossa on esim. 2 minuuttia aikaa ja ensimmäinen virhe lopettaa harjoituksen.
- Aikaisempien suoritusten seuraamiseen tarkoitettu näkymä, josta näkee miten harjoittelu parantanut laskunopeutta tai vähentänyt virheitä
- Kevyttä algebrajumppaa, neliöksi täydentäminen jne
- Trigonometriaa, trigonometristen identiteettien harjoittelua
