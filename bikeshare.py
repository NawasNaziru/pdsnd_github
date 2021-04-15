import time
import pandas as pd
import numpy as np
import datetime as dt
import click

CITY_DATA = { 'chicago': 'chicago.csv',
              'new_york_city': 'new_york_city.csv',
              'washington': 'washington.csv' }

days_of_week = ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
            'saturday')
months = ('all','january', 'february', 'march', 'april', 'may', 'june')


def user_selected(prompt_message, options=('yes', 'no', 'all')):
    """
    Generic function for prompting user to respond with one of the valid available options
    
    Returns user selection from given options
    """

    while True:
        user_selected = input(prompt_message).lower().strip()
        # exit the program if the input is exit
        if user_selected == 'exit':
            raise SystemExit
        # handle the situation when the user input is only one.
        elif ',' not in user_selected:
            if user_selected in options:
                break
        # what if in the situation the user input is more than one?
        elif ',' in user_selected:
            user_selected = [i.strip().lower() for i in user_selected.split(',')]
            if list(filter(lambda o: o in options, user_selected)) == user_selected:
                break
        
        prompt_message = ("\nThere was a problem. Check well, choose and enter correctly one of the presented options the formatting\n")
         

    return user_selected



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print("Note: To exit the program, just input exit into the prompt.\n")
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = user_selected("\nFor which city or cities do you want to see data, "
                      "new_york_city, Chicago or Washington? Please make use of commas "
                      "to separate the names and type the names as you see them here especially how new_york_city contains underscores.\n>", CITY_DATA.keys())

    # TO DO: get user input for month (all, january, february, ... , june)
        month = user_selected("\nStarting from the month of January to June, for which month(s) do you want to see data? Type all if you want to see data across all of the months. Please don't forget to use commas to separate the names.\n>", months)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = user_selected("\nFor which day(s) of the week do you want to get data? Type all if you want to see data for all the days. Please don't forget to use commas to separate the names.\n>", days_of_week)

   # confirm the user input
        verify_user_action = user_selected("\nDo you really want to see data based on your following selection?" "\n\n City(ies): {}\n Month(s): {}\n Weekday(s)"
                              ": {}\n\n Yes\n No\n\n>"
                              .format(city, month, day))
        if verify_user_action == 'yes':
            break
        else:
            print("\n Ok! It means you want to do something else. Go ahead!")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
<<<<<<< HEAD
    start_time = time.time()

=======
    
>>>>>>> documentation
    print("\n Loading the data of your choice...")

    # If user selected more than one city hence, in form of a list
    if isinstance(city, list):
        dframe = pd.concat(map(lambda city: pd.read_csv(CITY_DATA[city]), city),
                       sort=True)
    # If user input just one city, no need of any data merging
    else:
        dframe = pd.read_csv(CITY_DATA[city])

    # add new columns
    dframe['Start Time'] = pd.to_datetime(dframe['Start Time'])
    dframe['Month'] = dframe['Start Time'].dt.month
    dframe['day_of_week'] = dframe['Start Time'].dt.weekday_name
    dframe['Start Hour'] = dframe['Start Time'].dt.hour

    #If user selects all months
    if month == "all":
        dframe = dframe
    # if user input more than one month
    elif isinstance(month, list):
        dframe = pd.concat(map(lambda month: dframe[dframe['Month'] ==
                          (months.index(month))], month))
    # if user input just one month not all
    else:
        dframe = dframe[dframe['Month'] == (months.index(month))]
        
    # if user selects all days
    if day == "all":
        dframe = dframe
    # if user input more than one day
    elif isinstance(day, list):
        dframe = pd.concat(map(lambda day: dframe[dframe['day_of_week'] ==
                           (day.title())], day))
    # if user input just one day
    else:
        dframe = dframe[dframe['day_of_week'] == day.title()]
<<<<<<< HEAD

    print("\nThis took %s seconds." % (time.time() - start_time))    
=======
        
>>>>>>> documentation
    print('-'*40)

    return dframe


def time_stats(dframe):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_most_common = dframe['Month'].mode()[0]
    print('The most popular month for travels is: ' +
          str(months[month_most_common-1]).title())

    # TO DO: display the most common day of week
    day_most_common = dframe['day_of_week'].mode()[0]
    print('The most popular day of the week is: ' +
          str(day_most_common))

    # TO DO: display the most common start hour
    hour_most_common = dframe['Start Hour'].mode()[0]
    print('The most popular start hour is: ' +
          str(hour_most_common) + '.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(dframe):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    start_station_most_common = str(dframe['Start Station'].mode()[0])
    print("The most commonly used start station is: " +
          start_station_most_common)


    # TO DO: display most commonly used end station
    end_station_most_common = str(dframe['End Station'].mode()[0])
    print("The most commonly used end station is: " +
          end_station_most_common)

    # TO DO: display most frequent combination of start station and end station trip
    dframe['Start-End_Station'] = (dframe['Start Station'] + ' - ' +
                                   dframe['End Station'])
    start_end_most_common = str(dframe['Start-End_Station']
                                            .mode()[0])
    print("The most frequent start-end stations combination is: " + start_end_most_common)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(dframe):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is", dframe['Trip Duration'].sum(), "\n")

    # TO DO: display mean travel time
    print("The mean travel time is", dframe['Trip Duration'].mean(), "\n")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(dframe):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types_counts = dframe['User Type'].value_counts()
    print("The counts of user types is as follows:", user_types_counts)

    # TO DO: Display counts of gender
    gender_counts = dframe['Gender'].value_counts()
    print("This is the gender counts from the data:", gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    
    earliest_birth_year = int(dframe['Birth Year'].min())
    print("\nThe birth year of the most elderly who rode a bike is: ", earliest_birth_year)
    most_recent_birth_year = int(dframe['Birth Year'].max())
    print("The birth year of the youngest person who rode a bike is : ", most_recent_birth_year)
        
    most_common_birth_year = int(dframe['Birth Year'].mode()[0])
    print("The most common year in the birth years of users is:", most_common_birth_year)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def show_raw_data(dframe):
    """
    Display raw data 5 lines at a time.   
    """    
    print("\nYou opted to see raw data.")
    # this variable holds the last position user stopped at in viewing the raw data
    last_position = 1
    while True:
        raw_request = user_selected('\nWould you like to see some raw data? Type Yes or No.\n')
        if raw_request == 'yes':
            print(dframe[last_position:last_position + 5])
            last_position = last_position+5
            if user_selected("Do you want to keep printing raw data?"
                      "\n\nYes\nNo\n\n>") == 'yes':
                continue
            else:
                break
        else:
            break
    
    return last_position



def main():
    while True:
        click.clear()
        city, month, day = get_filters()
        dframe = load_data(city, month, day)
        
        while True:
<<<<<<< HEAD
            click.clear()
=======
>>>>>>> documentation
            user_selected_data = user_selected("\nChoose the information you would "
                                 "like to see.\n\n [ts] For Time Stats\n [ss] "
                                 "For Station Stats\n [tds] For Trip Duration Stats\n "
                                 "[us] For User Stats\n [rd] For Raw Data\n "
                                 "[r] Restart\n\n>",
                                 ('ts', 'ss', 'tds', 'us', 'rd', 'r'))
<<<<<<< HEAD
=======
            click.clear()
>>>>>>> documentation
            if user_selected_data == 'ts':
                time_stats(dframe)
            elif user_selected_data == 'ss':
                station_stats(dframe)
            elif user_selected_data == 'tds':
                trip_duration_stats(dframe)
            elif user_selected_data == 'us':
                user_stats(dframe)
            elif user_selected_data == 'rd':
                show_raw_data(dframe)
            elif user_selected_data == 'r':
                break
<<<<<<< HEAD
        restart = user_selected('\nWould you like to restart? Enter Yes or No.\n')
        if restart.lower() != 'yes':
            click.clear()
=======

        restart = user_selected('\nWould you like to restart? Enter Yes or No.\n')
        if restart.lower() != 'yes':
>>>>>>> documentation
            break


if __name__ == "__main__":
	main()
