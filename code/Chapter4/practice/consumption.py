import statistics

consumptions = {
    "New York": {
        "water": [331, 368, 263, 213, 392, 323, 416, 261, 229, 343, 342, 494],
        "electricity": [211, 283, 249, 251, 301, 378, 353, 369, 234, 234, 362, 341],
    },
    "Los Angeles": {
        "water": [425, 262, 431, 416, 216, 390, 483, 297, 211, 287, 413, 390],
        "electricity": [217, 492, 482, 311, 346, 216, 242, 313, 341, 202, 218, 395],
    },
    "Chicago": {
        "water": [209, 283, 249, 251, 301, 378, 353, 369, 234, 234, 362, 341],
        "electricity": [410, 343, 255, 315, 410, 239, 485, 229, 452, 392, 334, 482],
    },
    "Houston": {
        "water": [217, 492, 482, 311, 346, 216, 242, 313, 341, 202, 218, 395],
        "electricity": [229, 409, 341, 364, 277, 286, 231, 333, 431, 308, 427, 349],
    },
}

for city in consumptions:
    water = consumptions[city]["water"]
    electricity = consumptions[city]["electricity"]

    consumptions[city]["average_water_consumption"] = statistics.mean(water)
    consumptions[city]["average_electricity_consumption"] = statistics.mean(electricity)

print(consumptions)