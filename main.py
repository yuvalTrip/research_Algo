import openpyxl as openpyxl
import pandas as pd

# Load the CSV files
codes_for_questions = pd.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/codes_for_questions.csv")
codes_for_answers = pd.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/codes_for_answers.csv")
list_of_answers = pd.read_csv("https://raw.githubusercontent.com/erelsgl-at-ariel/research-5784/main/06-python-databases/homework/list_of_answers.csv")

# print(list_of_answers)
# writer = pd.ExcelWriter("df.xlsx")
# list_of_answers.to_excel(writer)
# writer._save()
#
# writer = pd.ExcelWriter("df0.xlsx")
# codes_for_questions.to_excel(writer)
# writer._save()
#
# writer = pd.ExcelWriter("df1.xlsx")
# codes_for_answers.to_excel(writer)
# writer._save()
def support_in_one_party_elections(party: str) -> int:
    """
    Returns the number of people who support a given party in the current election system (Q2).
    Explanation about DB- in 'list_of_answers' db, there is column named 'Q2'- there are numbers between range
    1 to 17- according parties ID as written in db 'codes_for_answers'.
    So each get it ID , the choser choose 1 number according the party he chose.

    >>> support_in_one_party_elections('מחל')
    134

    >>> support_in_one_party_elections('פה')
    109

    >>> support_in_one_party_elections('שס')
    13
    >>> support_in_one_party_elections('כן')
    33
    >>> support_in_one_party_elections('ב')
    134
    >>> support_in_one_party_elections('אמת')
    34
    >>> support_in_one_party_elections('ל')
    134
    >>> support_in_one_party_elections('ת')
    134
    >>> support_in_one_party_elections('מרצ')
    19
    """
    q2_support = list_of_answers['Q2'] #get the correct column from the DB
    party_code = codes_for_answers.loc[(codes_for_answers['Value'] == 'Q2') & (codes_for_answers['Label'].str.contains(party)), 'Code']
    if party_code.empty:
        return 0
    return (q2_support == party_code.iloc[0]).sum()


def get_party_code(party_name: str) -> int:
    """
    Returns the numerical code of the party given its name.

    >>> get_party_code('מחל')
    1

    >>> get_party_code('פה')
    2
    """
    for index, row in codes_for_answers.iterrows():
        if row['Label'].startswith(party_name):
            return row['Code']
    return "Party name not found"


def support_in_multi_party_elections(party: str) -> int:
    """
    Returns the number of people who would support a given party in an alternative election system (Q3).

    >>> support_in_multi_party_elections('1')
    162

    >>> support_in_multi_party_elections('2')
    131

    >>> support_in_multi_party_elections('3')
    39

    >>> support_in_multi_party_elections('4')
    93
    >>> support_in_multi_party_elections('5')
    101
    >>> support_in_multi_party_elections('6')
    85
    >>> support_in_multi_party_elections('8')
    38
    >>> support_in_multi_party_elections('11')
    61
    >>> support_in_multi_party_elections('12')
    66
    """
    # First we will take the required column of Q3 according to the given code of the party
    q3_req_column = f'Q3_{party}'

    # Now we will count how many 1 values there are in this column.
    count_ones = list_of_answers[q3_req_column].value_counts().get(1, 0)

    return count_ones

def get_party_name(party_code: int) -> str:
    """
    Helper function for the last function.
    Returns the name of the party given its code.

    >>> get_party_name(1)
    'מחל'

    >>> get_party_name(2)
    'פה'

    >>> get_party_name(3)
    'שס'

    >>> get_party_name(4)
    'כן'

    >>> get_party_name(5)
    'ב'
    """
    party_label = codes_for_answers.loc[codes_for_answers['Code'] == party_code, 'Label']
    if not party_label.empty:
        return party_label.values[0].split(' - ')[0]
    else:
        return "Party code not found"
#
# def parties_with_different_relative_order() -> list:
#     """
#     Returns a list of pairs of parties whose relative order is different between the two election methods.
#
#     >>> parties_with_different_relative_order()
#     [('ל', 'פה'), ('שס', 'כן')]
#     [('מחל', 'פה'), ('ל', 'ת')]
#     """
#     #ל Q2=134
#     #ת Q2=134
#
#     # ל Q3=38
#     # ת Q3=61
#
#     for num in range(1,18):
#         result_q3=support_in_multi_party_elections(str(num))
#         party_name_=get_party_name(num)
#         result_q2=support_in_one_party_elections(party_name_)
# # ..............

    # # Calculate support in the current system (Q2)
    # q2_support = list_of_answers['Q2'].value_counts().reset_index()
    # q2_support.columns = ['Code', 'Count']
    #
    # # Calculate support in the alternative system (Q3)
    # q3_columns = [col for col in list_of_answers.columns if col.startswith('Q3')]
    # q3_support = list_of_answers[q3_columns].apply(pd.Series.value_counts).sum(axis=1).reset_index()
    # q3_support.columns = ['Code', 'Count']
    #
    # # Rank the parties based on support in Q2
    # q2_ranking = q2_support.sort_values(by='Count', ascending=False).reset_index(drop=True)
    # q3_ranking = q3_support.sort_values(by='Count', ascending=False).reset_index(drop=True)
    #
    # q2_order = q2_ranking['Code'].tolist()
    # q3_order = q3_ranking['Code'].tolist()
    #
    # different_orders = []
    # for i, q2_party in enumerate(q2_order):
    #     for j, q3_party in enumerate(q3_order):
    #         if q2_party != q3_party and q2_party in q3_order and q3_party in q2_order:
    #             q2_index = q2_order.index(q3_party)
    #             q3_index = q3_order.index(q2_party)
    #             if q2_index < i and j < q3_index:
    #                 different_orders.append((q2_party, q3_party))
    # return different_orders

def get_party_code(party_code: int) -> str:
    """
    Returns the party code (letters on the ballot) given its numerical code.

    >>> get_party_code(1)
    'מחל'

    >>> get_party_code(2)
    'פה'
    """
    party_label = codes_for_answers.loc[codes_for_answers['Code'] == party_code, 'Label']
    if not party_label.empty:
        return party_label.values[0].split(' - ')[0]
    else:
        return "Party code not found"

def parties_with_different_relative_order() -> list:
    """
    Returns a list of pairs of parties whose relative order is different between the two election methods.
    """
    # Calculate support in the current system (Q2)
    q2_support = list_of_answers['Q2'].value_counts().reset_index()
    q2_support.columns = ['Code', 'Count']

    # Calculate support in the alternative system (Q3)
    q3_columns = [col for col in list_of_answers.columns if col.startswith('Q3')]
    q3_support = list_of_answers[q3_columns].apply(pd.Series.value_counts).fillna(0).sum(axis=1).reset_index()
    q3_support.columns = ['Code', 'Count']

    # Ensure Code columns are strings
    q2_support['Code'] = q2_support['Code'].astype(str)
    q3_support['Code'] = q3_support['Code'].astype(str)

    q2_ranking = q2_support.sort_values(by='Count', ascending=False).reset_index(drop=True)
    q3_ranking = q3_support.sort_values(by='Count', ascending=False).reset_index(drop=True)

    q2_order = q2_ranking['Code'].tolist()
    q3_order = q3_ranking['Code'].tolist()

    # Convert q3_order to a list of integers
    q3_order_int = [int(float(code)) for code in q3_order]
    print (q3_order_int)

    different_orders = []
    for i in range(len(q2_order)):
        for j in range(i + 1, len(q2_order)):
            q2_party1, q2_party2 = q2_order[i], q2_order[j]
            # Convert to float and then to int
            q2_party1 = int(float(q2_party1))
            q2_party2 = int(float(q2_party2))

            # Get indices in q3_order_int
            q3_index1, q3_index2 = q3_order_int.index(q2_party1), q3_order_int.index(q2_party2)
            if q3_index1 > q3_index2:
                party1 = get_party_code(q2_party1)
                party2 = get_party_code(q2_party2)
                if (party1, party2) not in different_orders and (party2, party1) not in different_orders:
                    different_orders.append((party1, party2))

    return different_orders


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    party = input("Enter party code or 'parties_with_different_relative_order': ")
    if party == "parties_with_different_relative_order":
        print(parties_with_different_relative_order())
    else:
        print(support_in_one_party_elections(party), support_in_multi_party_elections(party))
