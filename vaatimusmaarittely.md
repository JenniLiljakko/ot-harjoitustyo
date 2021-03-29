# Vaatimusmäärittely

### Sovelluksen tarkoitus:

Tehtävägeneraattori antaa käyttäjälle tehtäviä, jotka käyttäjä ratkaisee. Ohjelma kertoo käyttäjälle oliko ratkaisu oikein vain väärin, oikean ratkaisun kohdalla ohjelma myös näyttää mallivastauksen.
Tehtävistä saa pisteitä, ja lopuksi näytetään saadut pisteet. 
Ohjelmaan kirjaudutaan sisään, ja siinä voi olla useita eri tasoisia käyttäjiä.

### Käyttäjät:

Ohjelmalla on aluksi yksi käyttäjärooli, eli peruskäyttäjä. Myöhemmin lisätään pääkäyttäjä, joka voi hallinnoida eri käyttäjiä sekä nähdä tilastoja.

### Käyttöliittymäluonnos:


### Peruskäyttäjän toiminnot:


#### Ennen kirjautumista
* Käyttäjä voi luoda käyttäjätunnuksen sovellukseen
* Tunnus sisältää vähintään 2 merkkiä
* Sovellukseen kirjaudutaan luodulla tunnuksella
* Jos tunnusta ei ole olemassa, ilmoittaa ohjelma siitä virheilmoituksella

#### Kirjautumisen jälkeen

* Käyttäjä valitsee vaikeustason tehtävilleen
* Käyttäjä vastaa tehtäviin, ja saa niistä pisteitä
* Lopuksi käyttäjä näkee saamansa pisteet
* Käyttäjä voi kirjautua ulos ohjelmasta


### Jatkokehitysideat:

* Generaattorissa voi valita tehtävien aiheen
* Uusi käyttäjä aloittaa vaikeustasolta 1, ja suorittamalla kaikki tehtävät oikein pääsee hän jatkamaan seuraavalle vaikeustasolle
* Mikäli käyttäjä jää jumiin, on mahdollista saada vinkki tehtävän ratkaisuun "apua" nappia painamalla
* Top- listat 
* Käyttäjätunnuksien yhteyteen salasana
* Tulosten resetointi käyttäjäkohtaisesti
