# Testausdokumentti

Ohjelman testaus on toteutettu yksikkö- sekä integraatiotestien osalta automatisoidun testityökalu [Unittest](https://docs.python.org/3/library/unittest.html) avulla. 

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavia UserService sekä ExerciseService luokkia testataan vastaavilla
[UserServiceTest](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/src/tests/services/user_service_test.py) 
sekä [ExerciseServiceTest](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/src/tests/services/exercise_service_test.py) luokilla. Testejä varten käytetään oikeita luokkia, mutta testaukseen luotua erillistä testi-tietokantaa (test.sqlite). 

## Repositorio

UserRepository sekä ExerciseRepository luokkia testataan luokilla [UserRepositoryTest](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/src/tests/repositories/user_repository_test.py) sekä [ExerciseRepositorytest](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/src/tests/repositories/exercise_repository_test.py).

### Testikattavuus

Sovelluksen testien haarautumiskattavuus on 91%

![](https://github.com/JenniLiljakko/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/testikattavuus.jpg)

## Järjestelmätestaus

Järjestelmätestaus on suoritettu manuaalisesti.

## Ohjelmaan jääneet laatuongelmat

