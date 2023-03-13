# Serializers

## Book Instance
``` python
class BookInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstanceModel
        fields = "__all__"
```

## Book
``` python
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = "__all__"
```

## Reader
``` python
class ReaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReaderModel
        fields = "__all__"
```

## Reader With Book
``` python
class ReaderWithBookSerializer(serializers.ModelSerializer):
    books_instances = serializers.SlugRelatedField(read_only=True, many=True, slug_field='id')

    class Meta:
        model = ReaderModel
        fields = "__all__"
```
