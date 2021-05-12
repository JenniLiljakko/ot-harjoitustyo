# Vaatimusmäärittely
päivitetty 12.toukokuuta 2021

### Sovelluksen tarkoitus:

Tehtävägeneraattori antaa käyttäjälle tehtäviä, jotka käyttäjä ratkaisee. Ohjelma kertoo käyttäjälle oliko ratkaisu oikein vain väärin.
Ohjelmaan kirjaudutaan sisään, ja siihen voi luoda uuden käyttäjän.

### Käyttäjät:

Ohjelmalla on aluksi yksi käyttäjärooli, eli peruskäyttäjä.

### Käyttöliittymäluonnos:

![](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/tehtavageneraattori_luonnos.jpg)

### Peruskäyttäjän toiminnot:


#### Ennen kirjautumista
* Käyttäjä voi luoda käyttäjätunnuksen sovellukseen (**tehty**)
* Tunnus sisältää vähintään 2 merkkiä(**tehty**)
* Sovellukseen kirjaudutaan luodulla tunnuksella (**tehty**)
* Jos tunnusta ei ole olemassa, ilmoittaa ohjelma siitä virheilmoituksella (**tehty**)

#### Kirjautumisen jälkeen

* Käyttäjä valitsee vaikeustason tehtävilleen (**tehty**)
* Käyttäjä voi kirjautua ulos ohjelmasta (**tehty**)

### Vaatimukset:

* Tehtävägeneraattori toimii Linux- ja OSX-käyttöjärjestelmillä (**tehty**)
* Käyttäjien tiedot talletetaan paikalliselle levylle (**tehty**)


### Jatkokehitysideat:

* Generaattorissa voi valita tehtävien aiheen
* Uusi käyttäjä aloittaa vaikeustasolta 1, ja suorittamalla kaikki tehtävät oikein pääsee hän jatkamaan seuraavalle vaikeustasolle
* Mikäli käyttäjä jää jumiin, on mahdollista saada vinkki tehtävän ratkaisuun "apua" nappia painamalla
* Top- listat 
* Käyttäjätunnuksien yhteyteen salasana (**tehty**)
* Tulosten resetointi käyttäjäkohtaisesti
* Ajastin tehtävien yhteyteen
