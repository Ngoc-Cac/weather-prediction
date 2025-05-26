from fastapi import Body


predict_example_body = Body(
    openapi_examples={
        'simple': {
            'summary': 'A simple example',
            'value': {
                "city_coords": [49.25, -123.12],
                "day_1": {
                    "humidity": 77.38,
                    "pressure": 972.80,
                    "temperature": 286.14,
                    "wind_direction": 209.50,
                    "wind_speed": 0.00
                }
            }
        },
        'full': {
            'summary': 'Example with all seven days',
            'value': {
                "city_coords": [49.25, -123.12],
                "day_1": {
                    "humidity": 77.38,
                    "pressure": 972.80,
                    "temperature": 286.14,
                    "wind_direction": 209.50,
                    "wind_speed": 0.00
                },
                "day_2": {
                    "humidity": 71.63,
                    "pressure": 1009.75,
                    "temperature": 285.52,
                    "wind_direction": 162.91,
                    "wind_speed": 0.54
                },
                "day_3": {
                    "humidity": 49.54,
                    "pressure": 1018.41,
                    "temperature": 284.37,
                    "wind_direction": 87.16,
                    "wind_speed": 0.62
                },
                "day_4": {
                    "humidity": 43.13,
                    "pressure": 1023.16,
                    "temperature": 283.75,
                    "wind_direction": 147.91,
                    "wind_speed": 0.41
                },
                "day_5": {
                    "humidity": 43.17,
                    "pressure": 1015.66,
                    "temperature": 284.82,
                    "wind_direction": 125.70,
                    "wind_speed": 0.37
                },
                "day_6": {
                    "humidity": 47.75,
                    "pressure": 1018.04,
                    "temperature": 285.59,
                    "wind_direction": 102.08,
                    "wind_speed": 0.37
                },
                "day_7": {
                    "humidity": 58.79,
                    "pressure": 1014.41,
                    "temperature": 285.94,
                    "wind_direction": 97.00,
                    "wind_speed": 0.29
                }
            }
        }
    }
)