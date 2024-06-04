def FaSt(S, C, V):
    """
    Second algorithm to find a leximin optimal stable matching
    :param S: List of students
    :param C: List of colleges
    :param V: Valuation matrix where V[i][j] is the valuation of student i for college j
    :return: A stable matching that is leximin optimal
    """
    # Initialize a stable matching
    matching = initialize_stable_matching(S, C, V)
    # Compute the initial leximin value and position array
    leximin_value, pos = compute_leximin_value(matching, V)

    # Iterate to find leximin optimal stable matching
    for i in range(len(S) - 1, -1, -1):
        for j in range(len(C) - 1, 0, -1):
            # Check if moving student i to college j improves the leximin value
            if can_improve_leximin(S[i], C[j], V, leximin_value):
                # If it does improve - perform the demote operation to maintain stability
                demote(matching, S[i], C[j-1], C[j])
                # Recompute the leximin value and position array after the demotion
                leximin_value, pos = compute_leximin_value(matching, V)

    # Return the final stable matching
    return matching


def initialize_stable_matching(S, C, V):
    """
       Initialize a student optimal stable matching.
       This function creates an initial stable matching by assigning students to colleges based on
       their preferences. The first n - m + 1 students are assigned to the highest-ranked college,
       and the remaining students are assigned to the other colleges in sequence.

       :param S: List of students
       :param C: List of colleges
       :param V: Valuation matrix where V[i][j] is the valuation of student i for college j
       :return: A dictionary representing the initial stable matching where each college is a key and the value is a list of assigned students
       """
    # Get the number of students and colleges
    n = len(S)
    m = len(C)
    # Create an empty matching dictionary where each college has an empty list of assigned students
    matching = {c: [] for c in C}

    # Assign the first n - m + 1 students to the highest ranked college (C1)
    for i in range(n - m + 1):
        matching[C[0]].append(S[i])

    # Assign the remaining students to the other colleges in sequence
    for j in range(1, m):
        matching[C[j]].append(S[n - m + j])

    return matching# Return the initialized stable matching



def compute_leximin_value(matching, V):
    """
        Compute the leximin value of the current matching.

        This function calculates the leximin value of the current matching by evaluating the
        valuations of students for their assigned colleges. The leximin value is the sorted
        list of these valuations. It also returns the position array that tracks the positions
        of the valuations in the sorted list.

        :param matching: A dictionary representing the current matching where each college is a key and the value is a list of assigned students
        :param V: Valuation matrix where V[i][j] is the valuation of student i for college j
        :return: A tuple (values, pos) where values is the sorted list of valuations (leximin value) and pos is the position array
        """

    values = []# Initialize an empty list to store the valuations
    for college, students in matching.items():# Iterate over each college and its assigned students in the matching
        for student in students:# Iterate over each student assigned to the current college
            student_index = student - 1  # assuming students are 1-indexed
            college_index = college - 1  # assuming colleges are 1-indexed
            # Append the student's valuation for the current college to the values list
            values.append(V[student_index][college_index])
    # Sort the valuations in non-decreasing order to form the leximin tuple
    values.sort()
    pos = [0] * len(values)# Initialize the position array to track the positions of the valuations
    # Populate the position array with the index of each valuation
    for idx, value in enumerate(values):
        pos[idx] = idx
    # Return the sorted leximin values and the position array
    return values, pos


def can_improve_leximin(student, college, V, leximin_value):
    """
    Check if moving the student to the college improves the leximin value.

    :param student: The student being considered for reassignment
    :param college: The college being considered for the student's reassignment
    :param V: Valuation matrix where V[i][j] is the valuation of student i for college j
    :param leximin_value: The current leximin value
    :return: True if the new leximin value is an improvement, otherwise False
    """
    # Get the current value of the student for the new college
    current_value = V[student - 1][college - 1]  # assuming students and colleges are 1-indexed
    # Create a copy of the current leximin values
    new_values = leximin_value[:]
    # Remove the current value of the student in their current college from the leximin values
    new_values.remove(current_value)
    # Add the current value of the student for the new college to the leximin values
    new_values.append(current_value)
    # Sort the new leximin values to form the new leximin tuple
    new_values.sort()
    # Return True if the new leximin tuple is lexicographically greater than the current leximin tuple
    return new_values > leximin_value


def demote(matching, student_index, down, up):
    """
    Perform the demote operation to maintain stability.

    :param matching: The current matching dictionary
    :param student_index: The student being demoted
    :param down: The current college of the student
    :param up: The new college for the student
    """
    # Move student to college 'down' while reducing the number of students in 'up'
    # Set t to student_index
    t = student_index
    # Set p to 'down'
    p = down

    # While p > up
    while p > up:
        # Remove student 't' from college 'cp-1'
        matching[p - 1].remove(t)
        # Add student 't' to college 'cp'
        matching[p].append(t)
        # Decrement t and p
        t -= 1
        p -= 1


def update_leximin_value(matching, V):
    # Update the leximin value after demotion
    values = []
    for college, students in matching.items():
        for student in students:
            student_index = student - 1  # assuming students are 1-indexed
            college_index = college - 1  # assuming colleges are 1-indexed
            values.append(V[student_index][college_index])
    values.sort()
    return values


# Example usage
S = [1, 2, 3, 4, 5, 6, 7]  # Students
C = [1, 2, 3]  # Colleges
V = [
    [10, 8, 7],  # s1's valuations for c1, c2, c3
    [9, 7, 8],  # s2's valuations for c1, c2, c3
    [6, 5, 8],  # s3's valuations for c1, c2, c3
    [5, 9, 6],  # s4's valuations for c1, c2, c3
    [8, 6, 9],  # s5's valuations for c1, c2, c3
    [7, 10, 5],  # s6's valuations for c1, c2, c3
    [6, 7, 8]  # s7's valuations for c1, c2, c3
]

matching = FaSt(S, C, V)
print("Final Matching:", matching)
