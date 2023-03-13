# Views

## Book Instances
- Создать:
``` python
class BookInstancesCreateView(CreateAPIView):
    serializer_class = BookInstanceSerializer
    queryset = BookInstanceModel.objects.all()
```
- Получить, обновить, удалить:
``` python
class BookInstancesGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookInstanceSerializer
    queryset = BookInstanceModel.objects.all()
```
- Все:
``` python
class BookInstancesListView(ListAPIView):
    serializer_class = BookInstanceSerializer
    queryset = BookInstanceModel.objects.all()
```

## Book
- Создать:
``` python
class BookCreateView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()
```
- Получить, обновить, удалить:
``` python
class BooksGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()
```
- Все:
``` python
class BookListView(ListAPIView):
    serializer_class = BookSerializer
    queryset = BookModel.objects.all()
```

## Readers
- Создать:
``` python
class ReadersCreateView(CreateAPIView):
    serializer_class = ReaderSerializer
    queryset = ReaderModel.objects.all()
```
- Получить, обновить, удалить:
``` python
class ReadersGetUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = ReaderSerializer
    queryset = ReaderModel.objects.all()
```
- Все:
``` python
class ReadersListView(ListAPIView):
    serializer_class = ReaderSerializer
    queryset = ReaderModel.objects.all()
```
    
## ReadersWithBooks
- Все:
``` python
class ReadersWithBooksListView(ListAPIView):
    serializer_class = ReaderWithBookSerializer
    queryset = ReaderModel.objects.all()
```
