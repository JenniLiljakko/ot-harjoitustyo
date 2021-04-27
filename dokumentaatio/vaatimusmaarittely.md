# Vaatimusmäärittely

### Sovelluksen tarkoitus:

Tehtävägeneraattori antaa käyttäjälle tehtäviä, jotka käyttäjä ratkaisee. Ohjelma kertoo käyttäjälle oliko ratkaisu oikein vain väärin, oikean ratkaisun kohdalla ohjelma myös näyttää mallivastauksen.
Tehtävistä saa pisteitä, ja lopuksi näytetään saadut pisteet. 
Ohjelmaan kirjaudutaan sisään, ja siinä voi olla useita eri tasoisia käyttäjiä.

### Käyttäjät:

Ohjelmalla on aluksi yksi käyttäjärooli, eli peruskäyttäjä (**tehty**). Myöhemmin lisätään pääkäyttäjä, joka voi hallinnoida eri käyttäjiä sekä nähdä tilastoja.

### Käyttöliittymäluonnos:

![](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/tehtavageneraattori_luonnos.jpg)

### Peruskäyttäjän toiminnot:


#### Ennen kirjautumista
* Käyttäjä voi luoda käyttäjätunnuksen sovellukseen (**tehty**)
* Tunnus sisältää vähintään 2 merkkiä(**tehty**)
* Sovellukseen kirjaudutaan luodulla tunnuksella (**tehty**)
* Jos tunnusta ei ole olemassa, ilmoittaa ohjelma siitä virheilmoituksella (**tehty**)

#### Kirjautumisen jälkeen

* Käyttäjä valitsee vaikeustason tehtävilleen (**tehty**)
* Käyttäjä vastaa tehtäviin, ja saa niistä pisteitä
* Lopuksi käyttäjä näkee saamansa pisteet
* Käyttäjä voi kirjautua ulos ohjelmasta (**tehty**)

### Vaatimukset:

* Tehtävägeneraattori toimii Linux- ja OSX-käyttöjärjestelmillä
* Käyttäjien tiedot talletetaan paikalliselle levylle


### Jatkokehitysideat:

* Generaattorissa voi valita tehtävien aiheen
* Uusi käyttäjä aloittaa vaikeustasolta 1, ja suorittamalla kaikki tehtävät oikein pääsee hän jatkamaan seuraavalle vaikeustasolle
* Mikäli käyttäjä jää jumiin, on mahdollista saada vinkki tehtävän ratkaisuun "apua" nappia painamalla
* Top- listat 
* Käyttäjätunnuksien yhteyteen salasana (**tehty**)
* Tulosten resetointi käyttäjäkohtaisesti
* Ajastin tehtävien yhteyteen
