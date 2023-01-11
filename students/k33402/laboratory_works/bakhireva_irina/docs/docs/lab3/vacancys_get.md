# [ GET ] /vacancys/

## Информация

Получение списка вакансий в системе

**Method**: `GET`  
**Authorization**: `Token`  
**Role**: `-`

## Параметры

### В строке запроса

**specialization** - отображать только по конкретной специализации

## Ответ

```json
[
	{
		"id": 1,
		"company": {
			"id": 1,
			"name": "Quirky Xanthic Mule Of Conversion"
		},
		"specs": [
			{
				"id": 7,
				"name": "Программист Unity(Junior)"
			}
		],
		"salary": 967000,
		"created_date": "2023-01-10T20:48:03.209800Z"
	},
	{
		"id": 2,
		"company": {
			"id": 1,
			"name": "Quirky Xanthic Mule Of Conversion"
		},
		"specs": [
			{
				"id": 9,
				"name": "Программист Unity(Senior)"
			}
		],
		"salary": 407000,
		"created_date": "2023-01-10T20:48:03.541335Z"
	},
	{
		"id": 3,
		"company": {
			"id": 1,
			"name": "Quirky Xanthic Mule Of Conversion"
		},
		"specs": [
			{
				"id": 7,
				"name": "Программист Unity(Junior)"
			}
		],
		"salary": 462000,
		"created_date": "2023-01-10T20:48:03.795702Z"
	},
	{
		"id": 4,
		"company": {
			"id": 1,
			"name": "Quirky Xanthic Mule Of Conversion"
		},
		"specs": [
			{
				"id": 2,
				"name": "Программист JS(Middle)"
			}
		],
		"salary": 293000,
		"created_date": "2023-01-10T20:48:04.040590Z"
	},
	{
		"id": 5,
		"company": {
			"id": 1,
			"name": "Quirky Xanthic Mule Of Conversion"
		},
		"specs": [
			{
				"id": 1,
				"name": "Программист JS(Junior)"
			}
		],
		"salary": 505000,
		"created_date": "2023-01-10T20:48:04.315428Z"
	},
	{
		"id": 6,
		"company": {
			"id": 2,
			"name": "Psychedelic Beaver From Avalon"
		},
		"specs": [
			{
				"id": 4,
				"name": "Программист Python(Junior)"
			}
		],
		"salary": 843000,
		"created_date": "2023-01-10T20:48:05.297231Z"
	},
	{
		"id": 7,
		"company": {
			"id": 2,
			"name": "Psychedelic Beaver From Avalon"
		},
		"specs": [
			{
				"id": 1,
				"name": "Программист JS(Junior)"
			}
		],
		"salary": 811000,
		"created_date": "2023-01-10T20:48:05.558230Z"
	},
	{
		"id": 8,
		"company": {
			"id": 2,
			"name": "Psychedelic Beaver From Avalon"
		},
		"specs": [
			{
				"id": 7,
				"name": "Программист Unity(Junior)"
			}
		],
		"salary": 439000,
		"created_date": "2023-01-10T20:48:05.779734Z"
	},
	{
		"id": 9,
		"company": {
			"id": 2,
			"name": "Psychedelic Beaver From Avalon"
		},
		"specs": [
			{
				"id": 1,
				"name": "Программист JS(Junior)"
			}
		],
		"salary": 898000,
		"created_date": "2023-01-10T20:48:06.024732Z"
	},
	{
		"id": 10,
		"company": {
			"id": 2,
			"name": "Psychedelic Beaver From Avalon"
		},
		"specs": [
			{
				"id": 1,
				"name": "Программист JS(Junior)"
			}
		],
		"salary": 671000,
		"created_date": "2023-01-10T20:48:06.267403Z"
	},
	{
		"id": 11,
		"company": {
			"id": 3,
			"name": "Mature Ladybug Of Magic Completion"
		},
		"specs": [
			{
				"id": 10,
				"name": ""
			}
		],
		"salary": 565000,
		"created_date": "2023-01-10T20:48:07.204261Z"
	},
	{
		"id": 12,
		"company": {
			"id": 4,
			"name": "Quaint Bald Bullmastiff Of Support"
		},
		"specs": [
			{
				"id": 7,
				"name": "Программист Unity(Junior)"
			}
		],
		"salary": 529000,
		"created_date": "2023-01-10T20:48:08.093980Z"
	},
	{
		"id": 13,
		"company": {
			"id": 4,
			"name": "Quaint Bald Bullmastiff Of Support"
		},
		"specs": [
			{
				"id": 7,
				"name": "Программист Unity(Junior)"
			}
		],
		"salary": 904000,
		"created_date": "2023-01-10T20:48:09.710235Z"
	},
	{
		"id": 14,
		"company": {
			"id": 4,
			"name": "Quaint Bald Bullmastiff Of Support"
		},
		"specs": [
			{
				"id": 6,
				"name": "Программист Python(Senior)"
			}
		],
		"salary": 203000,
		"created_date": "2023-01-10T20:48:09.943430Z"
	},
	{
		"id": 15,
		"company": {
			"id": 5,
			"name": "Military Valiant Slug Of Gallantry"
		},
		"specs": [
			{
				"id": 4,
				"name": "Программист Python(Junior)"
			}
		],
		"salary": 933000,
		"created_date": "2023-01-10T20:48:10.867326Z"
	},
	{
		"id": 16,
		"company": {
			"id": 5,
			"name": "Military Valiant Slug Of Gallantry"
		},
		"specs": [
			{
				"id": 5,
				"name": "Программист Python(Middle)"
			}
		],
		"salary": 805000,
		"created_date": "2023-01-10T20:48:11.203605Z"
	},
	{
		"id": 17,
		"company": {
			"id": 6,
			"name": "Frisky Locust Of Imminent Control"
		},
		"specs": [
			{
				"id": 3,
				"name": "Программист JS(Senior)"
			}
		],
		"salary": 459000,
		"created_date": "2023-01-10T20:48:12.185396Z"
	},
	{
		"id": 18,
		"company": {
			"id": 6,
			"name": "Frisky Locust Of Imminent Control"
		},
		"specs": [
			{
				"id": 1,
				"name": "Программист JS(Junior)"
			}
		],
		"salary": 56000,
		"created_date": "2023-01-10T20:48:12.430687Z"
	},
	{
		"id": 19,
		"company": {
			"id": 6,
			"name": "Frisky Locust Of Imminent Control"
		},
		"specs": [
			{
				"id": 6,
				"name": "Программист Python(Senior)"
			}
		],
		"salary": 231000,
		"created_date": "2023-01-10T20:48:12.682870Z"
	},
	{
		"id": 20,
		"company": {
			"id": 7,
			"name": "Dramatic Sceptical Woodlouse Of Essence"
		},
		"specs": [
			{
				"id": 2,
				"name": "Программист JS(Middle)"
			}
		],
		"salary": 284000,
		"created_date": "2023-01-10T20:48:13.755593Z"
	},
	{
		"id": 21,
		"company": {
			"id": 7,
			"name": "Dramatic Sceptical Woodlouse Of Essence"
		},
		"specs": [
			{
				"id": 7,
				"name": "Программист Unity(Junior)"
			}
		],
		"salary": 419000,
		"created_date": "2023-01-10T20:48:14.106270Z"
	},
	{
		"id": 22,
		"company": {
			"id": 7,
			"name": "Dramatic Sceptical Woodlouse Of Essence"
		},
		"specs": [
			{
				"id": 7,
				"name": "Программист Unity(Junior)"
			}
		],
		"salary": 325000,
		"created_date": "2023-01-10T20:48:14.393267Z"
	},
	{
		"id": 23,
		"company": {
			"id": 8,
			"name": "Married Nondescript Dodo From Vega"
		},
		"specs": [
			{
				"id": 1,
				"name": "Программист JS(Junior)"
			}
		],
		"salary": 172000,
		"created_date": "2023-01-10T20:48:15.342301Z"
	},
	{
		"id": 24,
		"company": {
			"id": 8,
			"name": "Married Nondescript Dodo From Vega"
		},
		"specs": [
			{
				"id": 9,
				"name": "Программист Unity(Senior)"
			}
		],
		"salary": 898000,
		"created_date": "2023-01-10T20:48:15.587757Z"
	},
	{
		"id": 25,
		"company": {
			"id": 8,
			"name": "Married Nondescript Dodo From Vega"
		},
		"specs": [
			{
				"id": 8,
				"name": "Программист Unity(Middle)"
			}
		],
		"salary": 986000,
		"created_date": "2023-01-10T20:48:15.820804Z"
	},
	{
		"id": 26,
		"company": {
			"id": 8,
			"name": "Married Nondescript Dodo From Vega"
		},
		"specs": [
			{
				"id": 10,
				"name": ""
			}
		],
		"salary": 426000,
		"created_date": "2023-01-10T20:48:16.085755Z"
	},
	{
		"id": 27,
		"company": {
			"id": 8,
			"name": "Married Nondescript Dodo From Vega"
		},
		"specs": [
			{
				"id": 10,
				"name": ""
			}
		],
		"salary": 624000,
		"created_date": "2023-01-10T20:48:16.318756Z"
	},
	{
		"id": 28,
		"company": {
			"id": 9,
			"name": "Godlike Quixotic Ibis Of Realization"
		},
		"specs": [
			{
				"id": 8,
				"name": "Программист Unity(Middle)"
			}
		],
		"salary": 305000,
		"created_date": "2023-01-10T20:48:17.219261Z"
	},
	{
		"id": 29,
		"company": {
			"id": 9,
			"name": "Godlike Quixotic Ibis Of Realization"
		},
		"specs": [
			{
				"id": 10,
				"name": ""
			}
		],
		"salary": 886000,
		"created_date": "2023-01-10T20:48:17.473754Z"
	},
	{
		"id": 30,
		"company": {
			"id": 10,
			"name": "Clever Wildcat Of Perpetual Serenity"
		},
		"specs": [
			{
				"id": 3,
				"name": "Программист JS(Senior)"
			}
		],
		"salary": 737000,
		"created_date": "2023-01-10T20:48:19.537805Z"
	},
	{
		"id": 31,
		"company": {
			"id": 10,
			"name": "Clever Wildcat Of Perpetual Serenity"
		},
		"specs": [
			{
				"id": 1,
				"name": "Программист JS(Junior)"
			}
		],
		"salary": 845000,
		"created_date": "2023-01-10T20:48:19.780121Z"
	},
	{
		"id": 32,
		"company": {
			"id": 10,
			"name": "Clever Wildcat Of Perpetual Serenity"
		},
		"specs": [
			{
				"id": 4,
				"name": "Программист Python(Junior)"
			}
		],
		"salary": 19000,
		"created_date": "2023-01-10T20:48:20.013105Z"
	},
	{
		"id": 33,
		"company": {
			"id": 11,
			"name": "Serious Light Dragon Of Tenacity"
		},
		"specs": [
			{
				"id": 10,
				"name": ""
			}
		],
		"salary": 13000,
		"created_date": "2023-01-10T20:48:20.891879Z"
	},
	{
		"id": 34,
		"company": {
			"id": 11,
			"name": "Serious Light Dragon Of Tenacity"
		},
		"specs": [
			{
				"id": 10,
				"name": ""
			}
		],
		"salary": 761000,
		"created_date": "2023-01-10T20:48:21.146344Z"
	},
	{
		"id": 35,
		"company": {
			"id": 11,
			"name": "Serious Light Dragon Of Tenacity"
		},
		"specs": [
			{
				"id": 9,
				"name": "Программист Unity(Senior)"
			}
		],
		"salary": 221000,
		"created_date": "2023-01-10T20:48:21.385677Z"
	},
	{
		"id": 36,
		"company": {
			"id": 11,
			"name": "Serious Light Dragon Of Tenacity"
		},
		"specs": [
			{
				"id": 9,
				"name": "Программист Unity(Senior)"
			}
		],
		"salary": 354000,
		"created_date": "2023-01-10T20:48:21.618369Z"
	},
	{
		"id": 37,
		"company": {
			"id": 12,
			"name": "Powerful Able Mantis From Venus"
		},
		"specs": [
			{
				"id": 3,
				"name": "Программист JS(Senior)"
			}
		],
		"salary": 48000,
		"created_date": "2023-01-10T20:48:22.563673Z"
	},
	{
		"id": 38,
		"company": {
			"id": 13,
			"name": "Enlightened Romantic Iguana From Tartarus"
		},
		"specs": [
			{
				"id": 2,
				"name": "Программист JS(Middle)"
			}
		],
		"salary": 941000,
		"created_date": "2023-01-10T20:48:23.546158Z"
	},
	{
		"id": 39,
		"company": {
			"id": 13,
			"name": "Enlightened Romantic Iguana From Tartarus"
		},
		"specs": [
			{
				"id": 4,
				"name": "Программист Python(Junior)"
			}
		],
		"salary": 959000,
		"created_date": "2023-01-10T20:48:23.798402Z"
	},
	{
		"id": 40,
		"company": {
			"id": 14,
			"name": "Competent Venomous Ferret Of Patience"
		},
		"specs": [
			{
				"id": 10,
				"name": ""
			}
		],
		"salary": 359000,
		"created_date": "2023-01-10T20:48:24.802257Z"
	},
	{
		"id": 41,
		"company": {
			"id": 15,
			"name": "Tiny Obedient Crayfish Of Priority"
		},
		"specs": [
			{
				"id": 9,
				"name": "Программист Unity(Senior)"
			}
		],
		"salary": 631000,
		"created_date": "2023-01-10T20:48:25.773157Z"
	},
	{
		"id": 42,
		"company": {
			"id": 15,
			"name": "Tiny Obedient Crayfish Of Priority"
		},
		"specs": [
			{
				"id": 3,
				"name": "Программист JS(Senior)"
			}
		],
		"salary": 540000,
		"created_date": "2023-01-10T20:48:26.029360Z"
	},
	{
		"id": 43,
		"company": {
			"id": 15,
			"name": "Tiny Obedient Crayfish Of Priority"
		},
		"specs": [
			{
				"id": 7,
				"name": "Программист Unity(Junior)"
			}
		],
		"salary": 824000,
		"created_date": "2023-01-10T20:48:26.270862Z"
	},
	{
		"id": 44,
		"company": {
			"id": 15,
			"name": "Tiny Obedient Crayfish Of Priority"
		},
		"specs": [
			{
				"id": 6,
				"name": "Программист Python(Senior)"
			}
		],
		"salary": 239000,
		"created_date": "2023-01-10T20:48:26.519437Z"
	}
]
```