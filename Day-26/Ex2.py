input_dict_cel = {
    "Monday": 12,
    "Tuesday": 34,
    "Friday": 32,
    "Saturday": 31,
    "Sunday": 20
}

output_dict_fern = {day: (temperature * 1.8) + 32 for (day, temperature) in input_dict_cel.items()}
print(output_dict_fern)
