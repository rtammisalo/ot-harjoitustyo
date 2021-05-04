# Arkkitehtuuri

## Sovelluksen yleisrakenne

Sovellus perustuu pitkälti referenssisovelluksen tapaiseen rakenteeseen, jossa kaikki käyttöliittymään liittyvä on sijoitettu ui-paketin alle. Ui-paketin alaisuudessa on myös alipaketti components, joka sisältää eri käyttöliittymänäkymien teossa käytettäviä komponentteja, kuten eri asetusten yksilölliset asetusframet. 

Services-pakkauksen alaisuudessa ovat sovelluksen MainService ja laskujen luontiin ja tarkastukseen tarkoitettu ArithmeticService. Käyttöliittymän eri luokat käsittelevät sovelluslogiikan asioita yleisesti vain MainServicen kautta.

Repositories-pakkaus sisältää massamuistiin tallennukseen käytettävät SettingsRepository ja UserRepository luokat. Näiden ansioista ohjelmalla on "pysyvä" käsitys käyttäjistä ja heidän henkilökohtaisista asetuksista.

Entities-pakkauksen luokilla on tarkoitus mallintaa ohjelman toisiinsa liittyviä käsitekokonaisuuksia, kuten käyttäjä (User) tai käyttäjän asetukset (Settings).

### Pakkauskaavio
![Pakkauskaavio](kuvat/pakkauskaavio.png)

### Sekvenssikaavio
Alla sekvenssikaavio käyttäjän onnistuneesta sisäänkirjautumisesta.
![Sekvenssikaavio sisäänkirjautumisesta](kuvat/Sisäänkirjautuminen.png)

## Sovelluslogiikan kuvaus

Sovelluslogiikassa keskeisinä elementteinä ovat seuraavat käsitteet entities-paketin luokkina :
-User: käyttäjään liittyvä tieto. Nimi, salasana, asetukset.
-Settings: käyttäjän henkilökohtaiset ohjelman käyttöasetukset, kuten mikä on yhteenlaskutehtävien aikaraja tai minkä lukujen väliltä kertolaskun eri operandit valitaan.
-Operaatiot: Näistä binääri-operaatio luokista luodaan kysymykset mihin käyttäjä voi kirjoittaa vastauksensa.

Koko sovelluksen sitoo yhteen services-paketin MainService, jonka avulla voidaan kirjata käyttäjä sisään, luoda uusia käyttäjiä, ja saadaan myös viittaus toimivaan ArithmeticServiceen, joka on alipalvelu käyttäjälle esitettävien kysymyksien luomista ja vastauksen tarkistamista vasrten. Käyttöliittymän luokat saavat tarvitsemansa sovelluslogiikan palvelut MainServicen kautta riippuvuuden injektoinnilla. MainService käyttää UserRepositorya ja sen kautta SettingsRepositorya talletettavan tiedon käsittelyyn.

Sovelluksen tallennustiedon käsittely tehdään referenssisovelluksestakin tutuilla Repository-patternilla. Repositories-pakkauksen UserRepository tarjoaa mahdollisuuden tallentaa käyttäjän tiedot (nimi, salasana ja id) SQLite-tietokantaan. Koska jokaiseen käyttäjään liittyy sovelluksessa olennaisesti hänen oma henkilökohtainen asetustiedosto, on UserRepositoryllä myös viittaus SettingsRepositoryyn. SettingsRepositoryn tehtävänä on lukea hakemistosta käyttäjän oma .csv-tyyppinen asetustiedosto ja myös tarvittaessa tallettaa uudet asetukset tiedostoon.

Riippuvuuksien injektoinnin ansioista voidaan testauksessa käyttää stub-repositoryjä, kun halutaan vain yksikkötestata vain yhden luokan toiminnallisuutta.

Kaikki luokat voivat käyttää src-hakemiston juuresta löytyvää Config-luokkaa, jonka luokkamuuttujat antavat polut projektin juuressa olevasta .env tiedostosta löytyviin käyttäjän asettamiin default asetustiedostoon, käyttäjien asetustiedostojen hakemistoon sekä tietokantaan.
