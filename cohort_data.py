def unique_houses(filename):
    """TODO: Create a set of student houses.

    Iterates over the cohort_data.txt file to look for all of the included house names
    and creates a set called "houses" that holds those names.

        ex. houses = set([ "Hufflepuff",
                    "Slytherin",
                    "Ravenclaw",
                    "Gryffindor",
                    "Dumbledore's Army"
            ])

    """
    cohort_file = open(filename)
    houses = set()

    for line in cohort_file:
        line = line.rstrip().split("|")
        houses.add(line[2])
    # print houses
    return houses

unique_houses("cohort_data.txt")

def sort_by_cohort(filename):
    """TODO: Sort students by cohort, skipping instructors.

    Iterates over the data to create a list for each cohort, ordering students
    alphabetically by first name. Puts ghosts into a separate list entitled "ghosts".
    Returns a list of these lists.

        ex. fall_15 = ["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ""Hermione Granger", ... ]
        ex. all_students = [["Colin Creevey", "Dennis Creevey", "Seamus Finnigan", ...],
        ["Lee Jordan", "Andrew Kirke", "Neville Longbottom", ...],
        ["Cormac McLaggen", "Parvati Patil", "Jimmy Peakes", ...], 
        ["Euan Abercrombie", "Katie Bell", "Lavender Brown", ...]]

    """

    # open file
    cohort_file = open(filename)

    # Initialize cohort lists
    all_students = []
    winter_16 = []
    spring_16 = []
    summer_16 = []
    fall_15 = []
    ghosts = []

    for line in cohort_file:
        line = line.rstrip().split("|")
        first_name, last_name, house, instructor, cohort = line

        # Store full name in one variable
        full_name = first_name + " " + last_name
        
        # ghosts
        if cohort == "G":
            ghosts.append(full_name)
        
        # all_students
        if cohort != "G" and cohort != "I":
            all_students.append(full_name)

        #sorting all_students into their respective cohorts

        if cohort == "Winter 2016":
            winter_16.append(full_name)
        elif cohort == "Fall 2015":
            fall_15.append(full_name)
        elif cohort == "Spring 2016":
            spring_16.append(full_name)
        elif cohort == "Summer 2016":
            summer_16.append(full_name)



    cohorts = [sorted(all_students), sorted(winter_16), 
                sorted(spring_16), sorted(summer_16), sorted(fall_15), sorted(ghosts)]

    return cohorts




def students_by_house(filename):
    """TODO: Sort students by house.


    Iterates over the data to create a list for each house, and sorts students
    into their appropriate houses by last name. Sorts ghosts into a list called "ghosts"
    and instructors into a list called "instructors".
    Returns all lists in one list of lists.

        ex. gryffindor = ["Abercrombie", "Bell", "..." ]
        ex. ghosts = ["Baron", "Friar", "..."]
        ex. all_students = [ hufflepuff,
                    gryffindor,
                    ravenclaw,
                    slytherin,
                    dumbledores_army,
                    ghosts,
                    instructors
        ]

    """

    # open file
    cohort_file = open(filename)

    # Initialize lists
    all_students = []
    gryffindor = []
    hufflepuff = []
    slytherin = []
    dumbledores_army = []
    ravenclaw = []
    ghosts = []
    instructors = []


    for line in cohort_file:
        line = line.rstrip().split("|")
        first_name, last_name, house, instructor, cohort = line
        
        # ghosts
        if cohort == "G":
            ghosts.append(last_name)
        elif cohort == "I":
            instructors.append(last_name)
        # all_students
        else:
            all_students.append(last_name)

        #sorting all_students into their respective houses
        if house == "Gryffindor":
            gryffindor.append(last_name)
        elif house == "Hufflepuff":
            hufflepuff.append(last_name)
        elif house == "Slytherin":
            spring_16.append(full_name)
        elif cohort == "Summer 2016":
            summer_16.append(full_name)
        else:
            continue 


    cohorts = [sorted(all_students), sorted(winter_16), 
                sorted(spring_16), sorted(summer_16), sorted(fall_15), sorted(ghosts)]

    return cohorts



    # Code goes here

    return all_students


def all_students_tuple_list(filename):
    """TODO: Create a list of tuples of student data.

    Iterates over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)
        ex. student_list = [
                ("Euan Abercrombie", "Gryffindor", "McGonagall", "Summer 2016"),
                ("Katie Bell", "Gryffindor", "McGonagall", "Summer 2016"),
                # ...
            ]
    """

    student_list = []

    # Code goes here

    return student_list


def find_cohort_by_student_name(student_list):
    """TODO: Given full name, return student's cohort.

    Uses the above list of tuples generated by the preceding function to make a small
    function that, given a first and last name from the command line, returns that
    student's cohort, or returns "Student not found." when appropriate. """

    # Code goes here

    return "Student not found."


##########################################################################################
# Further Study Questions


def find_name_duplicates(filename):
    """TODO: Using set operations, make a set of student last names that have duplicates.

    Iterates over the data to find any last names that exist across all cohorts.
    Uses set operations (set math) to create a set of these names.
    NOTE: Do not include staff -- or do, if you want a greater challenge.

       ex. duplicate_names = set(["Weasley"])

    """

    duplicate_names = set()

    # Code goes here

    return duplicate_names


def find_house_members_by_student_name(student_list):
    """TODO: Create a function that prompts the user for a name via the command line
    and when given a name, print a statement of everyone in their house in their cohort.

    Uses the list of tuples generated by all_students_tuple_list to make a small function
    that, when given a student's first and last name, print students that are in both
    that student's cohort and that student"s house.

    ex: Choose a student: Hermione Granger
        Hermione Granger was in house Gryffindor in the Fall 2015
        cohort.
        The following students are also in their house:
        Seamus Finnigan
        Angelina Johnson
        Harry Potter
        Ron Weasley
        Oliver Wood


    """

    # Code goes here

    return


#########################################################################################

# Here is some useful code to run these functions!

# print unique_houses("cohort_data.txt")
# print sort_by_cohort("cohort_data.txt")
# print hogwarts_by_house("cohort_data.txt")
# all_students_data = all_students_tuple_list("cohort_data.txt")
# print all_students_data
# find_cohort_by_student_name(all_students_data)
# print find_name_duplicates("cohort_data.txt")
# find_house_members_by_student_name(all_students_data)
