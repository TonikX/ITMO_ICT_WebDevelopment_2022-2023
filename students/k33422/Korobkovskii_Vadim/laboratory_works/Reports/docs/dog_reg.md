**Таблица для хранения данных о зарегистрированных собаках.**
 
`Таблица имеет следующие поля:`
:

  1. Поле "show_dog_number" хранит порядковый номер собаки на выставке

  2. Поле "dog_status" хранит статус собаки, который надо выбрать из списка

  3. Поле "reg_dog_date" хранит дату регистрации собаки

  4. Поле "bill" хранит статус счёта, который надо выбрать из списка

  5. Поле "checkup" хранит статус медосмотра, который надо выбрать из списка
        
  6. Поле "checkup_date" хранит дату медосмотра

  7. Поле "participant_dog" является внешним ключом к таблице Dog

  8. Поле "show_dog" является внешним ключом к таблице Show

  9. Поле "show_medal" хранит полученную на выставке (или не полученную) медаль, которую надо выбрать из списка 

## Списки для выбора:

### Cписок для поля "dog_status"

``` python
status_choices = (
        ("Участвовал/Participated", "Участвовал/Participated"),
        ("Снят/Suspended", "Снят/Suspended"),
        ("Не допущен/Not allowed", "Не допущен/Not allowed"),
        ("Неявка/Absence", "Неявка/Absence")
)
```
### Cписок для поля "bill"

``` python
bill_choices = (
        ("Оплачен/Paid", "Оплачен/Paid"),
        ("Не оплачен/Not paid", "Не оплачен/Not paid")
)
```
### Cписок для поля "checkup"

``` python
checkup_choices = (
        ("Пройден/Passed", "Медосмотр успешно пройден/Medical examination was successfully passed"),
        ("Не пройден/Not passed", "Медосмотр не был пройден/Medical examination was not passed")
)
```
### Cписок для поля "show_medal"

``` python
medals = (
        ("Золото/Gold", "Золото за первое место/Gold for first place"),
        ("Серебро/Silver", "Серебро за второе место/Silver for second place"),
        ("Бронза/Bronze", "Бронза за третье место/Bronze for third place"),
        ("Медаль от зрителей/Audience award", "Медаль как приз зрительских симпатий/Medal as audience sympathy prize")
)
```

