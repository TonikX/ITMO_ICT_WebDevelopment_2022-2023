**Таблица для хранения данных о расписании на выставках.**
 
`Таблица имеет следующие поля:`
:

  1. Поле "show_breed" хранит выступающую на ринге породу, которую надо выбрать из списка

  2. Поле "show_time" хранит дату и время начала выступления на ринге

  3. Поле "ring_number" хранит номер ринга

  4. Поле "show_class" хранит возрастной класс выступающих на ринге собак, который надо выбрать из списка

  5. Поле "show_schedule" является внешним ключом к таблице Show

## Списки для выбора:

### Cписок для поля "show_breed"

``` python
breeds = (
        ('Корги/Corgi', 'Корги/Corgi'),
        ('Немецкая овчарка/German shepherd', 'Немецкая овчарка/German shepherd'),
        ('Бигль/Beagle', 'Бигль/Beagle'),
        ('Пудель/Poodle', 'Пудель/Poodle'),
        ('Ретривер/Retriever', 'Ретривер/Retriever'),
        ('Самоед/Samoyed', 'Самоед/Samoyed'),
        ('Доберман/Doberman', 'Доберман/Doberman')
)
```
### Cписок для поля "show_class"

``` python
class_types = (
        ("Baby", "Собаки от 4 до 6 месяцев/Dogs from 4 to 6 months old"),
        ("Puppy", "Собаки от 6 до 9 месяцев/Dogs from 6 to 9 months old"),
        ("Junior", "Собаки от 9 до 18 месяцев/Dogs from 9 to 18 months old"),
        ("Intermediate", "Собаки от 15 до 24 месяцев/Dogs from 15 to 24 months old"),
        ("Open", "Собаки от 15 месяцев/Dogs from 15 months old"),
        ("Work", "Собаки от 15 месяцев с дипломом/Dogs from 15 months with diploma old"),
        ("Champions", "Собаки от 15 месяцев при наличии сертификата Чемпиона страны-члена FCI/Dogs from 15 months old with FCI Member country Champion certificate"),
        ("Veteran", "Собаки от 8 лет/Dogs from 8 years old")
)
```
