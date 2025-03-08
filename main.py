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

            #Convert str to int
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

    #Loop to calculate algorithms' average happiness and duration rating
    for algorithm in stats.keys():
        avg_hapiness = stats[algorithm]['total_happiness'] / stats[algorithm]['session_count']
        avg_duration = stats[algorithm]['total_duration'] / stats[algorithm]['session_count']
        stats[algorithm]['avg_happiness'] = avg_hapiness
        stats[algorithm]['avg_duration'] = avg_duration

    #Find highest happiness and longest duration rating
    highest_avg_happiness = 0
    longest_average_duration = 0
    highest_happiness_alg = ''
    longest_average_duration_alg = ''
    
    for algorithm in stats.keys():
        if stats[algorithm]['avg_happiness'] >= highest_avg_happiness:
            highest_avg_happiness = stats[algorithm]['avg_happiness']
            highest_happiness_alg = algorithm
        if stats[algorithm]['avg_duration'] >= longest_average_duration:
            longest_average_duration = stats[algorithm]['avg_duration']
            longest_average_duration_alg = algorithm

    #Result
    print("Euphoria User Engagement Analysis Report")
    print("----------------------------------------")
    print("Average Happiness Rating per Algorithm:")
    for algorithm in stats.keys():
        print(f"- {algorithm}: {stats[algorithm]['avg_happiness']:.2f}")
    print("\nTotal Number of Sessions per Algorithm:")
    for algorithm in stats.keys():
        print(f"- {algorithm}: {stats[algorithm]['session_count']}")
    print("\nAverage Session Duration per Algorithm:")
    for algorithm in stats.keys():
        print(f"- {algorithm}: {stats[algorithm]['avg_duration']:.2f} minutes")
    print("\nHighest Average Happiness Rating:")
    print(f"- {highest_happiness_alg} with an average happiness rating of {highest_avg_happiness:.2f}")
    print("\nLongest Average Session Duration:")
    print(f"- {longest_average_duration_alg} with an average session duration of {longest_average_duration:.2f} minutes")

if __name__ == "__main__":
    main()