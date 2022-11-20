from images.models import Photo, Color, Keyword
import csv


def run():
    # photos = Photo.objects.all()
    # for photo in photos:
    #     print(photo.photo_id, photo.photo_image_url)
    with open('scripts/keywords.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ai_score = -1
            if row["ai_score"]:
                ai_score = row["ai_score"]
            keyword = Keyword(
                photo=Photo.objects.get(pk=row["photo_id"]),
                keyword=row["keyword"],
                ai_score=ai_score
            )
            keyword.save()
            # photo = Photo(
            #     photo_id=row['photo_id'],
            #     photo_url=row['photo_url'],
            #     photo_image_url=row['photo_image_url'],
            #     photo_width=row['photo_width'],
            #     photo_height=row['photo_height'],
            #     photo_description=row['photo_description'],
            #     photographer_username=row['photographer_username'],
            #     photographer_first_name=row['photographer_first_name'],
            #     photographer_last_name=row['photographer_last_name'],
            #     blur_hash=row['blur_hash'],
            # )
            # photo.save()
