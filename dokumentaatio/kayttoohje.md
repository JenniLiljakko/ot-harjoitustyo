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

Kun olet valinnut itsellesi sopivan käyttäjänimen ja salasanan, syötä ne vapaisiin tekstikenttiin ja paina 'Create New User' nappia.
Tämä sulkee ikkunan, ja palaa aiempaan kirjautumisnäkymään.

Nyt voit kirjautua sisään uudella juuri luomallasi käyttäjätunnuksella sekä salasanalla. Paina lopuksi 'Login'

## Tehtävägeneraattorin pääsivu

Kirjautumisen jälkeen pääset tehtävägeneraattorin pääsivulle:

![](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/paasivu.jpg)

Pääsivulla on valittavissa tehtävän vaikeustaso sekä tehtävät, aloita vaikeutasosta 1 (Level 1) sekä tehtävästä 1.
Pääset tehtävänäkymään painamalla tehtävänumeroa.

Kirjaudu ulos painamalla pääsivun alareunassa olevaa 'Log out?' nappia.

## Tehtävänäkymä

![](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/tehtavanakyma.jpg)

Kirjoita vastauksesi vapaaseen tekstikenttään, vahvista vastauksesi painamalla 'Submit' nappia.
Tehtävägeneraattori antaa välittömästi viestin tehtävän onnistumisesta.
Kun olet valmis, sulje tehtävänäkymän ikkuna.
