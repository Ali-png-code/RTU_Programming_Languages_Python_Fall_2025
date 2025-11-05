"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [68, 70, 72, 75, 71, 69, 73]
city_population = {"New York": 8468000,
    "Los Angeles": 3899000,
    "Chicago": 2706000,
    "Houston": 2320000,
    "Phoenix": 1680000}

# TODO: Compute aggregates
average_temperature = sum(temperatures) / len(temperatures)
largest_city = max(city_population, key=city_population.get) # type: ignore
largest_population = city_population[largest_city]


average_temperature = 0
largest_city = ""
largest_population = 0
total_population = 0

# TODO: Print results
print("Average temperature:", round(average_temperature, 2), "°F")
print("Largest city:", largest_city, "-", largest_population)
print("Total population:", total_population)
