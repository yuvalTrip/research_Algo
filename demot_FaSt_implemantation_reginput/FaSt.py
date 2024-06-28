import main
def initialize_matching(n, m):
    """
    Initialize the first stable matching.

    :param n: Number of students
    :param m: Number of colleges
    :return: Initial stable matching
    """
    initial_matching = {k: [] for k in range(1, m + 1)}  # Create a dictionary for the matching
    # Assign the first (n - m + 1) students to the first college (c1)
    for student in range(1, n - m + 2):
        initial_matching[1].append(student)
    # Assign each remaining student to the subsequent colleges (c2, c3, ...)
    for j in range(2, m + 1):
        initial_matching[j].append(n - m + j)
    return initial_matching

def get_leximin_tuple(matching, V):
    """
    Generate the leximin tuple based on the given matching and evaluations,
    including the sum of valuations for each college.

    :param matching: The current matching dictionary
    :param V: The evaluations matrix
    :return: Leximin tuple
    """
    leximin_tuple = []
    college_sums = []

    # Iterate over each college in the matching
    for college, students in matching.items():
        college_sum = 0
        # For each student in the college, append their valuation for the college to the leximin tuple
        for student in students:
            valuation = V[student - 1][college - 1]
            leximin_tuple.append(valuation)
            college_sum += valuation
        college_sums.append(college_sum)
    # Append the college sums to the leximin tuple
    leximin_tuple.extend(college_sums)

    # Sort the leximin tuple in descending order
    leximin_tuple.sort(reverse=False)

    return leximin_tuple
def get_unsorted_leximin_tuple(matching, V):
    """
    Generate the leximin tuple based on the given matching and evaluations,
    including the sum of valuations for each college.

    :param matching: The current matching dictionary
    :param V: The evaluations matrix
    :return: UNSORTED Leximin tuple
    """
    leximin_tuple = []
    college_sums = []

    # Iterate over each college in the matching
    for college, students in matching.items():
        college_sum = 0
        # For each student in the college, append their valuation for the college to the leximin tuple
        for student in students:
            valuation = V[student - 1][college - 1]
            leximin_tuple.append(valuation)
            college_sum += valuation
        college_sums.append(college_sum)
    # Append the college sums to the leximin tuple
    leximin_tuple.extend(college_sums)
    return leximin_tuple
def build_pos_array(matching, V):
    """
    Build the pos array based on the leximin tuple and the matching.

    :param leximin_tuple: The leximin tuple
    :param matching: The current matching dictionary
    :param V: The evaluations matrix
    :return: Pos array
    """
    pos = [] # Initialize pos array
    student_index=0
    college_index=0
    leximin_unsorted_tuple=get_unsorted_leximin_tuple(matching,V)
    leximin_sorted_tuple= sorted(leximin_unsorted_tuple)
    while student_index<len (V):
        pos_value=leximin_sorted_tuple.index(leximin_unsorted_tuple[student_index])
        pos.append(pos_value)
        student_index += 1
    while college_index < len(matching):
        pos_value=leximin_sorted_tuple.index(leximin_unsorted_tuple[student_index+college_index])
        pos.append(pos_value)
        college_index += 1
    return pos

def create_L(matching):
    """
        Create the L list based on the matching.
    :param matching: The current matching
    :return: L list
    """
    L = []

    # Create a list of tuples (college, student)
    for college, students in matching.items():
        for student in students:
            L.append((college, student))

    return L
def build_college_values(matching, V):
    """
    Build the college_values dictionary that sums the students' valuations for each college.

    :param matching: The current matching dictionary
    :param V: The evaluations matrix
    :return: College values dictionary
    """
    college_values = {}

    # Iterate over each college in the matching
    for college, students in matching.items():
        college_sum = sum(V[student - 1][college - 1] for student in students)
        college_values[college] = college_sum

    return college_values

def FaSt(S, C, V):

    n = len(S)  # number of students
    m = len(C)  # number of colleges
    L = []  # leximin tuple
    pos = [0] * n  # position array
    i = n - 1  # start from the last student
    j = m-1  # start from the last college
    F = {n}  # initialize the fixed set with the last student

    # Initialize the first stable matching
    initial_matching = initialize_matching(n, m)
    # print("Final Matching:")
    # for college, students in final_matching.items():
    #     print(f"College {college}: {students}")
    print (initial_matching)
    print (V)
    lex_tupl=get_leximin_tuple(initial_matching,V)
    print("lex_tupl: ",lex_tupl)
    # Initialize the leximin tuple L and position array pos
    pos= build_pos_array(initial_matching, V)
    print ("pos:", pos)
    L=create_L(initial_matching)
    print ("L:", L)

    college_values=build_college_values(initial_matching,V)
    #print("college_values: " , college_values)
    print("i: ", i)
    print("j: " , j)
    index=1
    while i > j - 1 and j > 0:

        print("******** Iteration number ",index, "********")
        print("i: ", i)
        print("j: ", j)
        print("college_values[j+1]: ", college_values[j+1])
        print ("V[i-1][j]: ", V[i-1][j])
        print ("college_values: ",college_values)
        if college_values[j+1] >= V[i-1][j]:###need to update after each iteration
            j -= 1
        else:
            if college_values[j + 1] < V[i - 1][j]:
                print ("V[i-1][j]:",V[i-1][j])
            #if V[i][j - 1] > L[j - 1]:
                initial_matching = main.demote(initial_matching, i, j+1, 1)
                print("initial_matching after demote:",initial_matching)
            else:
                if V[i][j - 1] < college_values[j]:
                    j -= 1
                else:
                    # Lookahead
                    k = i
                    t = pos[i]
                    µ_prime = initial_matching.copy()
                    while k > j - 1:
                        if V[k][j - 1] > L[t - 1]:
                            i = k
                            initial_matching = main.demote(µ_prime, k, j, 1)
                            break
                        elif V[k][j - 1] < college_values[j]:
                            j -= 1
                            break
                        else:
                            µ_prime = main.demote(µ_prime, k , j, 1)
                            k -= 1
                            t += 1
                    if k == j - 1 and initial_matching != µ_prime:
                        j -= 1
            #
        # Updates
        college_values = build_college_values(initial_matching, V)  # Update the college values
        lex_tupl = get_leximin_tuple(initial_matching, V)

        print("lex_tupl: ", lex_tupl)
        L = create_L(initial_matching)
        print("L:", L)
        pos = build_pos_array(initial_matching, V)
        print("pos:", pos)

        i -= 1
        index += 1
        print("END while :")
        print("i: ", i)
        print("j: ", j)


    return initial_matching

if __name__ == '__main__':
    # Students
    S = {1, 2, 3, 4, 5, 6, 7}

    # Colleges
    C = {1, 2, 3}

    # Preference Matrix
    V = [
        [9, 8, 7],  # s1's valuations for c1, c2, c3
        [8, 7, 6],  # s2's valuations for c1, c2, c3
        [7, 6, 5],  # s3's valuations for c1, c2, c3
        [6, 5, 4],  # s4's valuations for c1, c2, c3
        [5, 4, 3],  # s5's valuations for c1, c2, c3
        [4, 3, 2],  # s6's valuations for c1, c2, c3
        [3, 2, 1]   # s7's valuations for c1, c2, c3
    ]

    # Run the FaSt algorithm
    final_matching = FaSt(S, C, V)

    # Print the final matching
    print("Final Matching:")
    for college, students in final_matching.items():
        print(f"College {college}: {students}")
