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
        # Check if the student 't' is in college 'Cp-1'
        print( "Now demote student", t)
        print ("t ",t)
        print( "p " , p)
        print ("matching[p - 1]: ", matching[p - 1])
        if t not in matching[p - 1]:
            raise ValueError(f"Student {t} should be in matching to college {p - 1}")
        # Check that all colleges have at least one student
        for college, students in matching.items():
            if len(students) < 1:
                raise ValueError(f"All colleges must contain at least 1 student. College number {college} has only {len(students)} students.")

        # While p > up
        while p > up:
            print ("while loop")
            # Remove student 't' from college 'cp-1'
            matching[p - 1].remove(t)
            # Add student 't' to college 'cp'
            matching[p].append(t)
            # Decrement t and p
            t -= 1
            p -= 1
            print (matching)

        return matching


if __name__ == '__main__':
    # Initial matching
    matching = {
        1: [1, 6],  # c1
        2: [2, 3],  # c2
        3: [4, 5]  # c3
    }
    # Parameters
    UP = 1
    DOWN = 3
    I = 2

    # Print initial matching
    print("Initial Matching:")
    for college, students in matching.items():
        print(f"College {college}: {students}")

    # Apply the demote function
    demote(matching, I, DOWN, UP)

    # Print updated matching
    print("\nUpdated Matching:")
    for college, students in matching.items():
        print(f"College {college}: {students}")

