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

    # First we will take the required column of Q3 according to the given code of the party
    q3_req_column = f'Q3_{party}'

    # Now we will count how many 1 values there are in this column.
    count_ones = list_of_answers[q3_req_column].value_counts().get(1, 0)

    return count_ones


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
    33
    >>> support_in_multi_party_elections('5')
    134
    >>> support_in_multi_party_elections('6')
    34
    >>> support_in_multi_party_elections('8')
    134
    >>> support_in_multi_party_elections('11')
    134
    >>> support_in_multi_party_elections('12')
    19
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
    """
    party_label = codes_for_answers.loc[codes_for_answers['Code'] == party_code, 'Label']
    if not party_label.empty:
        return party_label.values[0].split(' - ')[0]
    else:
        return "Party code not found"

def parties_with_different_relative_order() -> list:
    """
    Returns a list of pairs of parties whose relative order is different between the two election methods.

    >>> parties_with_different_relative_order()
    [('מחל', 'פה'), ('שס', 'כן')]
    [('מחל', 'פה'), ('ל', 'אמת')]
    """
    for num in range(1,18):
        result_q3=support_in_multi_party_elections(str(num))
        party_name_=get_party_name(num)
        result_q2=support_in_one_party_elections(party_name_)
# ..............

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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    party = input("Enter party code or 'parties_with_different_relative_order': ")
    if party == "parties_with_different_relative_order":
        print(parties_with_different_relative_order())
    else:
        print(support_in_one_party_elections(party), support_in_multi_party_elections(party))
