# =============================================================================
# OmniCo Confidential
# -------------------
# This source code contains proprietary information of OmniCo.
# =============================================================================

def main():
    # Initialize the stats dictionary for each algorithm
    stats = {
        'JoyStream': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'SerenityFlow': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        },
        'DeepPulse': {
            'total_happiness': 0,
            'total_duration': 0,
            'session_count': 0
        }
    }

    # Open the CSV file and read data
    with open('euphoria_data.csv', 'r') as file:
        # Skip the header line
        header = file.readline()

        # Read each line in the file
        for line in file:
            # Remove any trailing whitespace characters like newline
            line = line.strip()

            # Split the line into a list of values
            columns = line.split(',')

            # Assign each column to a variable
            user_id = columns[0]
            algorithm = columns[1]

            # TODO: Define session_duration and happiness_rating variables and convert them to integers
            # Hint: Use the int() function to convert strings to integers
            session_duration = int(columns[2])
            happiness_rating = int(columns[3])

            # Update stats based on the algorithm
            if algorithm in stats:
                stats[algorithm]['total_happiness'] += happiness_rating
                stats[algorithm]['total_duration'] += session_duration
                stats[algorithm]['session_count'] += 1
            else:
                # Handle any unexpected algorithm names
                print(f"Unknown algorithm: {algorithm}")

    # TODO: Calculate averages for each algorithm
    # For each algorithm in the stats dictionary:
    #   - Calculate avg_happiness = total_happiness / session_count
    #   - Calculate avg_duration = total_duration / session_count
    #   - Store these back into the stats dictionary under 'avg_happiness' and 'avg_duration'
    for algorithm in stats.keys():
        avg_hapiness = stats[algorithm]['total_happiness'] / stats[algorithm]['session_count']
        avg_duration = stats[algorithm]['total_duration'] / stats[algorithm]['session_count']
        stats[algorithm]['avg_happiness'] = avg_hapiness
        stats[algorithm]['avg_duration'] = avg_duration


    # TODO: Determine the algorithm with the highest average happiness rating
    # Initialize variables to keep track of the highest average happiness and the corresponding algorithm
    # Loop through stats to compare avg_happiness values
    highest_avg_hapiness = 0
    highest_happiness_alg = ''
    for algorithm in stats.keys():
        if stats[algorithm]['avg_happiness'] >= highest_avg_hapiness:
            highest_avg_hapiness = stats[algorithm]['avg_happiness']
            highest_happiness_alg = algorithm
    
    # TODO: Determine the algorithm with the longest average session duration
    # Initialize variables to keep track of the longest average duration and the corresponding algorithm
    # Loop through stats to compare avg_duration values
    longest_average_duration = 0
    longest_average_duration_alg = ''
    for algorithm in stats.keys():
        if stats[algorithm]['avg_duration'] >= longest_average_duration:
            longest_average_duration = stats[algorithm]['avg_duration']
            longest_average_duration_alg = algorithm

    # TODO: Print the report
    # Use print statements to display the results in a formatted way
    # Follow the structure provided in the example output

    print("Euphoria User Engagement Analysis Report")
    print("----------------------------------------")
    print("Average Happiness Rating per Algorithm:")
    for algorithm in stats.keys():
        print(f"- {algorithm}: {stats[algorithm]['avg_happiness']}")
    print("\nTotal Number of Sessions per Algorithm:")
    for algorithm in stats.keys():
        print(f"- {algorithm}: {stats[algorithm]['session_count']}")
    print("\nAverage Session Duration per Algorithm:")
    for algorithm in stats.keys():
        print(f"- {algorithm}: {stats[algorithm]['avg_duration']:.2f} minutes")
    print("\nHighest Average Happiness Rating:")
    print(f"- {highest_happiness_alg} with an average happiness rating of {highest_avg_hapiness}")
    print("\nLongest Average Session Duration:")
    print(f"- {longest_average_duration_alg} with an average session duration of {longest_average_duration:.2f} minutes")

if __name__ == "__main__":
    main()