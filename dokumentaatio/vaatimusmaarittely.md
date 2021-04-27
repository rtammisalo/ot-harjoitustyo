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

![Luonnos](https://github.com/rtammisalo/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/uiluonnos.png)

## Sovelluksen ominaisuudet

- Käyttäjä voi luoda uuden tilin (Toteutettu aikaisemmin)
  - Tilillä on nimi ja salasana (Toteutettu aikaisemmin)
- Käyttäjä joutuu kirjautumaan sisään omalla tilillään (Toteutettu aikaisemmin)
  - Kirjautuessaan sisään käyttäjä voi avautuvasta näkymästä valita:
    1. Yhteenlaskuharjoituksia (Tehty)
    2. Vähennyslaskuharjoituksia (Tehty)
    3. Kertolaskuharjoituksia (Toteutettu aikaisemmin)
    4. Jakolaskuharjoituksia (Tehty)
    5. Satunnaisharjoituksia
  - Harjoitusnäkymissä käyttäjä voi ennen harjoittelun alkua muuttaa harjoituksen asetuksia, esim. kuinka monta numeroa operandeissa on tai antaa harjoitukselle aikaraja. (Tehty)
  - Harjoituksiin vastataan joko näppäimistöllä tai hiirellä (ikkunaan piirretään vastaamista varten pieni keypad) (Näppäimistöllä vastaaminen toteutettu)

## Mahdollisia lisäominaisuuksia
- Admin-tili, joka voi tutkia kaikkien käyttäjien tietoja tai tuhota tilejä
- Aikaisempien suoritusten seuraamiseen tarkoitettu näkymä, josta näkee miten harjoittelu parantanut laskunopeutta tai vähentänyt virheitä
- Kevyttä algebrajumppaa, neliöksi täydentäminen jne
- Trigonometriaa, trigonometristen identiteettien harjoittelua
