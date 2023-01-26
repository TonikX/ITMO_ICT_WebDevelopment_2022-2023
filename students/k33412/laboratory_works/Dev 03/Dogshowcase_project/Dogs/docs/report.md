# View a report for the specified show

Creates a report

**URL** : `/report/<year>`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Data constraints** : `{}`

## Success Responses

**Code** : `200 OK`

**Content** : `{}`

```json
{
    "participant_count": 3,
    "breeds": [
        {
            "breed": "b",
            "count": 1
        },
        {
            "breed": "h",
            "count": 2
        }
    ],
    "best_grades": [
        {
            "participant": 1,
            "ex_sum": 29
        },
        {
            "participant": 2,
            "ex_sum": 28
        },
        {
            "participant": 4,
            "ex_sum": 32
        }
    ],
    "medals": [
        {
            "breed": "b",
            "medals_count": 1
        },
        {
            "breed": "h",
            "medals_count": 3
        }
    ]
}```
