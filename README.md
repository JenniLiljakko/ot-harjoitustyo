# Tehtävägeneraattori

Sovelluksen avulla käyttäjä ratkaisee sovelluksen antamia tehtäviä. Tehtäville on useampi vaikeusaste.
Tehtävägeneraattori vaatii tunnuksen luomisen, ja kirjautumisen sisään salasanan avulla.

## Edistyminen:

* Sovellus on edistynyt viime viikosta
* Sovelluksella on nyt toimiva sisäänkirjautumisnäkymä, sekä 'uuden käyttäjän luonti' näkymä
* Kirjautuminen vaatii tunnuksen ja salasanan, tunnuksen tulee olla ainakin 2 merkkiä pitkä
    - ohjelma ilmoittaa mikäli:
    - tunnusta ei ole vielä olemassa,
    - mikäli salasana on väärä
    - kun tunnus ja salasana on oikein (sisäänkirjautuminen onnistui)     
* Sovelluksella on pääsivu, jolla on listattuna eri vaikeustasot, sekä tehtävänumerot nappien takana.
    - **siirtymistä kirjautumisikkunasta pääsivulle ei ole vielä toteutettu**
* Sovelluksen sovelluslogiikka on eriytetty käyttöliittymästä
* Pylint on otettu käyttöön
* Sovelluksella on arkkitehtuuritiedosto dokumentaatio hakemiston alla
* **Testausta ei ole vielä aloitettu**
* **Virtuaalityöasemaa en ole saanut toimimaan fuksiläppärillä useista yrityksistä huolimatta, joten en ole pystynyt tarkastamaan ohjelman toimivuutta sen kautta**


## Asentaminen

```bash
#Asenna sovellus komennolla:

poetry install

#Alusta sovellus komennolla:

poetry run invoke build

#Käynnistä/suorita komennolla:

poetry run invoke start
```

## Muuta:

### Testikattavuus: (huom! Ei vielä käytössä/testausta ei aloitettu)

```bash
#Testikattavuusraportin voi luoda seuraavalla komennolla:
poetry run invoke coverage-report
```

### Pylint
Tarkistukset voi suorittaa seuraavalla komennolla:

```bash
poetry run invoke pylint
```


## Dokumentaatio

* [Työaikakirjanpito ](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

* [Vaatimusmäärittely](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
  
* [Arkkitehtuuri](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
  
  
  
  
