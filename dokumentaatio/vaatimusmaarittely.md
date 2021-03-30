# Vaatimusmäärittely

## Sovelluksen käyttötarkoitus
Sovellus on aritmetiikan harjoitusohjelma. Ohjelman avulla voi sisäänkirjautunut käyttäjä 
harjoitella nopeita kerto-, jako-, yhteen- ja vähennyslaskuja. Jokaisella käyttäjällä on järjestelmässä
käyttäjänimi ja salasana, jolla hänet autentikoidaan. Myöhemmin voidaan lisätä myös mahdollisuus käyttäjälle
seurata aikaisempia suorituksia.

## Sovelluksen käyttäjäroolit
Sovelluksella on aluksi vain tavallisia käyttäjätilejä. Käyttäjä voidaan tunnistaa uudelleen tilinsä nojalla.

## Käyttöliittymä
Alla kuvassa piirrettynä kevyt luonnos sovelluksen graafisesta käyttöliittymästä.

Kuva tähän.

## Sovelluksen ominaisuudet

- Käyttäjä voi luoda uuden tilin
  - Tilillä on nimi ja salasana
- Käyttäjä joutuu kirjautumaan sisään omalla tilillään
  - Kirjautuessaan sisään käyttäjä voi avautuvasta näkymästä valita:
    1. Yhteenlaskuharjoituksia
    2. Vähennyslaskuharjoituksia
    3. Kertolaskuharjoituksia
    4. Jakolaskuharjoituksia
    5. Satunnaisharjoituksia
  - Harjoitusnäkymissä käyttäjä voi ennen harjoittelun alkua muuttaa harjoituksen asetuksia, esim. kuinka monta numeroa operandeissa on tai antaa harjoitukselle aikaraja.
  - Harjoituksiin vastataan joko näppäimistöllä tai hiirellä (ikkunaan piirretään vastaamista varten pieni keypad)

## Mahdollisia lisäominaisuuksia
- Admin-tili, joka voi tutkia kaikkien käyttäjien tietoja tai tuhota tilejä
- Aikaisempien suoritusten seuraamiseen tarkoitettu näkymä, josta näkee miten harjoittelu parantanut laskunopeutta tai vähentänyt virheitä
- Kevyttä algebrajumppaa, neliöksi täydentäminen jne
- Trigonometriaa, trigonometristen identiteettien harjoittelua