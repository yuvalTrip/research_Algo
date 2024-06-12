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
    54

    >>> support_in_one_party_elections('אמת')
    34

    >>> support_in_one_party_elections('ל')
    14

    >>> support_in_one_party_elections('ת')
    26
    >>> support_in_one_party_elections('מרצ')
    19
    """
    q2_support = list_of_answers['Q2']  # Get the correct column from the DB
    # print(codes_for_answers['Label'].unique())  # Debugging: print all unique labels
    party_code = codes_for_answers.loc[(codes_for_answers['Value'] == 'Q2') & (codes_for_answers['Label'].str.startswith(party)), 'Code']
    #print(f"Party: {party}, Party Code: {party_code}")  # Debugging
    if party_code.empty:
        return 0
    support_count = (q2_support == party_code.iloc[0]).sum()
    #print(f"Support Count for Party '{party}' (Code: {party_code.iloc[0]}): {support_count}")  # Debugging
    return support_count


def support_in_multi_party_elections(party: str) -> int:
    """
    Returns the number of people who would support a given party in an alternative election system (Q3).

    >>> support_in_multi_party_elections('מחל')
    162

    >>> support_in_multi_party_elections('פה')
    131
    >>> support_in_multi_party_elections('שס')
    39
    >>> support_in_multi_party_elections('כן')
    93
    >>> support_in_multi_party_elections('אמת')
    85
    >>> support_in_multi_party_elections('ל')
    38
    >>> support_in_multi_party_elections('ת')
    61
    >>> support_in_multi_party_elections('מרצ')
    66
    """
    questionName = codes_for_questions.loc[codes_for_questions['Label'].str.startswith(party, na=False), 'Variable'].values[0]
    return int(list_of_answers[questionName].sum())

def parties_with_different_relative_order() -> list:
    """
    Returns a list of pairs of parties whose relative order is different between the two election methods.
    """
    # Calculate support in the current system (Q2)
    q2_support = list_of_answers['Q2'].value_counts().reset_index()
    q2_support.columns = ['Code', 'Count']

    # Calculate support in the alternative system (Q3)
    q3_columns = [col for col in list_of_answers.columns if col.startswith('Q3')]
    q3_support = list_of_answers[q3_columns].apply(pd.Series.value_counts).fillna(0).iloc[1].reset_index()
    q3_support.columns = ['Code', 'Count']

    # Extract numerical part from 'Q3_X' to match with q2_support 'Code'
    q3_support['Code'] = q3_support['Code'].str.extract('_(\d+)').astype(int)

    # Ensure Code columns are integers
    q2_support['Code'] = q2_support['Code'].astype(int)
    q3_support['Code'] = q3_support['Code'].astype(int)

    q2_ranking = q2_support.sort_values(by='Count', ascending=False).reset_index(drop=True)
    q3_ranking = q3_support.sort_values(by='Count', ascending=False).reset_index(drop=True)

    q2_order = q2_ranking['Code'].tolist()
    q3_order = q3_ranking['Code'].tolist()

    different_orders = []
    for i in range(len(q2_order)):
        for j in range(i + 1, len(q2_order)):
            q2_party1, q2_party2 = q2_order[i], q2_order[j]
            if q2_party1 in q3_order and q2_party2 in q3_order:
                q3_index1, q3_index2 = q3_order.index(q2_party1), q3_order.index(q2_party2)
                if q3_index1 > q3_index2:
                    party1 = get_party_name(q2_party1)
                    party2 = get_party_name(q2_party2)
                    if (party1, party2) not in different_orders and (party2, party1) not in different_orders:
                        different_orders.append((party1, party2))

    return different_orders

def get_party_name(party_code: int) -> str:
    """
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

if __name__ == '__main__':
        party = input()
        if party == "parties_with_different_relative_order":
            print(parties_with_different_relative_order())
        else:
            print(support_in_one_party_elections(party), support_in_multi_party_elections(party))