# Tehtävägeneraattorin käyttöohje
Lataa ensin tehtävägenraattorin uusin release

## Käynnistys


```bash
#Asenna ensin riippuvuudet komennolla:

poetry install

#Alusta sovellus komennolla:

poetry run invoke build

--------------------------------

#Käynnistä tehtävägeneraattori komennolla:

poetry run invoke start
```

## Kirjautuminen ja käyttäjän luominen

Kun käynnistät sovelluksen, avautuu ensin kirjautumisnäkymä:

![](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/login.jpg)

Tarvitset sovelluksen käyttöön oman käyttäjän sekä salasanan.
Painamalla 'Create a new user?' pääset ikkunaan jossa voit luoda uuden käyttäjän:

![](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/create_user.jpg)

Kun olet valinnut itsellesi sopivan käyttäjänimen ja salasanan, paina 'Create New User', tämä sulkee ikkunan ja palaa takaisin kirjautumisnäkymään.

Nyt voit kirjautua sisään uudella juuri luomallasi käyttäjätunnuksella sekä salasanalla. Paina lopuksi 'Login'

## Tehtävägeneraattorin pääsivu


