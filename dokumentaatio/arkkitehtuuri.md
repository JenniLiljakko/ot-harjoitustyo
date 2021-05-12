# Arkkitehtuurikuvaus

## Rakenne

Ohjelman pakkausrakenne on seuraavanlainen:

![pakkausrakenne](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pakkausrakenne.jpg)

* [UI](https://github.com/JenniLiljakko/ot-harjoitustyo/tree/master/src/ui) sisältää käyttöliittymän
* [Services](https://github.com/JenniLiljakko/ot-harjoitustyo/tree/master/src/services) sovelluslogiikan
* [Repositories](https://github.com/JenniLiljakko/ot-harjoitustyo/tree/master/src/repositories) pysyväistallennuksen
* [Entities](https://github.com/JenniLiljakko/ot-harjoitustyo/tree/master/src/entities) sisältää sovelluksen käyttämiä tietokohteita

## Käyttöliittymä

Ohjelman käyttöliitymässä on neljä eri näkymää, jotka on toteutettu omina luokkinaan:

* Kirjautuminen (avautuu käynnistyksessä)
* Uuden käyttäjän luonti
* Pääsivu
* Tehtävänäkymä

Käyttöliittymän jokainen näkymä on oma ikkunansa. Kirjautumisikkunasta pystyy aukaisemaan erillisen 'Uuden käyttäjän luonti'- näkymän, joka näkyy yhdessä kirjautumisikkunan kanssa. Samoin pääsivulla tehtävänäkymä aukeaa pääsivun yhteyteen. 

Käyttöliittymä on eriytetty sovelluslogiikasta. Käyttöliittymän näkymistä vastaa **Ui-** luokka, joka kutsuu **Service-** luokan metodeja. 

## Sovelluslogiikka 


Sovelluslogiikan muodostavat [User-](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/src/entities/user.py) sekä [Exercise-](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/src/entities/exercise.py) luokat, jotka kuvastavat käyttäjää sekä tehtävägeneraattorin tehtäviä.

![](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/tietomalli.jpg)

Toiminnallisuudesta vastaavat [UserService](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/src/services/user_service.py) sekä [ExerciseService](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/src/services/exercise_service.py) luokkien tarjoamat metodit. 

Esimerkiksi:

**UserService**
* login(username, password)
* create(username, password)

**ExerciseService**
* get_exercise_number_list(level)
* check_answer(answer, exercise_number)

Tallennuksesta vastaavat pakkauksen repositories luokat [UserRepository](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/src/repositories/user_repository.py) sekä [ExerciseRepository](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/src/repositories/exercise_repository.py).


## Luokkakaavio

![luokkakaavio](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/luokkakaavio.jpg)
