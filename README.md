# Tehtävägeneraattori

Sovellus on Helsingin Yliopiston Ohjelmistotekniikka(TKT20002)- kurssin harjoitustyö. 

Sovelluksen avulla käyttäjä ratkaisee sovelluksen tarjoamia tehtäviä. Tehtäville on useampi vaikeusaste.
Generaattori antaa palautteen tehtävän onnistumisesta (oikein/väärin).

Tehtävägeneraattoriin luodaan käyttäjä sekä salasana, joiden avulla kirjautuminen sovellukseen onnistuu.

## Release

[**RELEASE 1**](https://github.com/JenniLiljakko/ot-harjoitustyo/releases/tag/viikko5)

[**RELEASE 2**](https://github.com/JenniLiljakko/ot-harjoitustyo/releases/tag/viikko6)

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


### Käynnistäminen

Käynnistä sovellus komennolla:
```bash
poetry run invoke start
```
### Testit

Aja testit läpi komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Luo testikattavuusraportti seuraavalla komennolla:
```bash
poetry run invoke coverage-report
```

### Pylint

[Pylintrc](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/.pylintrc) tiedoston tarkistukset suoritetaan komennolla:

```bash
poetry run invoke pylint
```


## Dokumentaatio

* [Käyttöohje ](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

* [Työaikakirjanpito ](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

* [Vaatimusmäärittely](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
  
* [Arkkitehtuuri](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
  
  
  
  
