# Arkkitehtuurikuvaus

## Rakenne

Ohjelman pakkausrakenne on seuraavanlainen:

![pakkausrakenne](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pakkausrakenne.jpg)

'Ui' sisältää käyttöliittymän,
'Services' sovelluslogiikan,
'Repositories' pysyväistallennuksen.
sekä 'Entities' sisältää sovelluksen käyttämiä tietokohteita.

## Käyttöliittymä

Ohjelman käyttöliitymässä on neljä eri näkymää, jotka on toteutettu omina luokkinaan:

* Kirjautuminen (avautuu käynnistyksessä)
* Uuden käyttäjän luonti
* Pääsivu
* Tehtävänäkymä

Käyttöliittymän jokainen näkymä on oma ikkunansa. Kirjautumisikkunasta pystyy aukaisemaan erillisen 'Uuden käyttäjän luonti'- näkymän, joka näkyy yhdessä kirjautumisikkunan kanssa. Samoin pääsivulla tehtävänäkymä aukeaa pääsivun yhteyteen. 

Käyttöliittymä on eriytetty sovelluslogiikasta. Käyttöliittymän näkymistä vastaa **Ui-** luokka, joka kutsuu **Service-** luokan metodeja. 

## Sovelluslogiikka 

Sovelluslogiikan muodostavat User- sekä Exercise-luokat, jotka kuvastavat käyttäjää sekä tehtävägeneraattorin tehtäviä.

![](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/tietomalli.jpg)




## Luokkakaavio

![luokkakaavio](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luokkakaavio.jpg)
