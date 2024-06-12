import sqlite3, requests

#in this task i used the help of GPT and from the examples learned in class

with open("poll.db", "wb") as file:
    response = requests.get("https://github.com/erelsgl-at-ariel/research-5784/raw/main/06-python-databases/homework/poll.db")
    file.write(response.content)
db = sqlite3.connect("poll.db")
cur = db.cursor()

def net_support_for_candidate1(candidate_a: str, candidate_b: str) -> int:
    """
    This function accepts the names of two candidates for Prime Minister, and returns the number of people
    who prefer candidate A over candidate B, minus those who prefer B over A.

    Parameters:
    candidate_a (str): The name of the first candidate.
    candidate_b (str): The name of the second candidate.

    Returns:
    int: The preference count (A over B minus B over A).
    >>> net_support_for_candidate1("ניר ברקת","גדעון סער")
    -20
    >>> net_support_for_candidate1("בני גנץ","יאיר לפיד")
    47
    >>> net_support_for_candidate1("נפתלי בנט","ניר ברקת")
    45
    >>> net_support_for_candidate1("בנימין נתניהו","יולי אדלשטיין")
    11
    >>> net_support_for_candidate1("יולי אדלשטיין","בנימין נתניהו")
    -11
    >>> net_support_for_candidate1("בני גנץ","יולי אדלשטיין")
    61
    >>> net_support_for_candidate1("גדעון סער","בני גנץ")
    51
    """
    # Prepare and execute a SQL query to select the 'Label' and 'Variable' columns
    # from the 'codes_for_questions' table where the 'Label' column matches either candidate_a or candidate_b
    cur.execute('''
        SELECT Label, Variable
        FROM codes_for_questions
        WHERE Label = ? OR Label = ?
    ''', (candidate_a, candidate_b))

    # Retrieves all (remaining) rows of a query result, returning a list.
    results = cur.fetchall()

    # Build a dictionary from the query results
    result_dict = {}
    for label, variable in results:
        result_dict[label] = variable

    # Get the specific codes for each candidate
    candidate1Code = result_dict[candidate_a]
    candidate2Code = result_dict[candidate_b]

    # Query to count the preferences
    query = 'SELECT COUNT({}) FROM list_of_answers WHERE {} {} {}'

    # Execute the query to count the number of people who prefer candidate2 over candidate1
    format_query1=query.format(candidate1Code, candidate1Code, '<', candidate2Code)
    result1 = cur.execute(format_query1).fetchone()[0]

    # Execute the query to count the number of people who prefer candidate1 over candidate2
    format_query2=query.format(candidate2Code, candidate1Code, '>', candidate2Code)
    result2 = cur.execute(format_query2).fetchone()[0]

    # Calculate and return the net support
    diff=result1 - result2
    return diff


def condorcet_winner()->str:
    """
    Determine the Condorcet winner, which is the candidate that is preferred by the majority over each of the other candidates.

    Returns:
    str: The name of the candidate who is preferred over all other candidates, or None if no such candidate exists.

    >>> condorcet_winner()
    'נפתלי בנט'
    """
    # Fetch the list of candidate names related to question 6
    cur.execute('''
        SELECT Label
        FROM codes_for_questions
        WHERE SUBSTR(Variable, 1, 2) = 'Q6'
        ''')

    # Fetch all rows from the cursor
    rows = cur.fetchall()

    # Initialize an empty list to store candidate codes
    candidate_codes = []

    # Extract the first column from each row and append to the list
    for row in rows:
        candidate_codes.append(row[0])

    # Check if a candidate is preferred over all other candidates
    def is_preferred(candidate, others):
        for other in others:
            if other != candidate:
                support = net_support_for_candidate1(candidate, other)
                if support <= 0:
                    return False
        return True
    #####################################################################################################################
    # Find the winning candidate
    winning_candidate = next((cand for cand in candidate_codes if is_preferred(cand, candidate_codes)), None)

    return winning_candidate

if __name__ == '__main__':
    party = input()
    if party == "condorcet_winner":
        print(condorcet_winner())
    else:
        candidate1,candidate2 = party.split(",")
        print(net_support_for_candidate1(candidate1,candidate2))