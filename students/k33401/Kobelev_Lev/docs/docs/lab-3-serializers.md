# Serializers
## Tag
``` python
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
```
## Game System
``` python
class GameSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
```
## Review
- Получение:
``` python
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'author', 'publish_date', 'is_edited']
```
- Создание:
``` python

```
- Обновление:
``` python

```