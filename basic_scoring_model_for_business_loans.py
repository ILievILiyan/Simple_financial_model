from colorama import Fore
from colorama import Style

current_revenue = 0
total_revenue_of_group = 0
total_EBITDA_of_group = 0
total_financial_debt_of_group = 0
list_of_co_debtors = []
total_equity = 0
total_assets = 0

print(f'{Fore.GREEN}Hello! This is a scoring model for applying business loans!'
      f', please fill the following information!{Style.RESET_ALL}')

name_of_company = input(f'{Fore.BLUE}Name of the Company{Style.RESET_ALL} applying for loan: ')
num_of_companies_in_group = int(input(f'{Fore.BLUE}Number of companies in group{Style.RESET_ALL} '
                                      '/including Borrower and Co-debtors only/: '))
if num_of_companies_in_group > 1:
    for index in range(num_of_companies_in_group - 1):
        name_of_co_debtor = input(f'{Fore.BLUE}Name of Co-debtor{Style.RESET_ALL}: ')
        list_of_co_debtors.append(name_of_co_debtor)

loan_amount_applying = float(input(f'The {Fore.GREEN}Amount of loan{Style.RESET_ALL} (in thousands BGN), '
                                   f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} wants to apply: '))
if loan_amount_applying >= 2000:
    print(f'{Fore.RED}Not applicable.{Style.RESET_ALL} Amount must be under 2 000 000 BGN.')
    exit()

stage_of_companies = int(input(f'The {Fore.GREEN}stage status{Style.RESET_ALL} [1,2,3] of Group: '))
if stage_of_companies != 1:
    print(f'{Fore.RED}Not applicable.{Style.RESET_ALL} It is acceptable risk status "Stage 1" only.')
    exit()

if num_of_companies_in_group == 1:
    internal_best_rating_of_companies = int(input(f'The {Fore.GREEN}internal rating{Style.RESET_ALL} of '
                                                  f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL}: '))
else:
    internal_best_rating_of_companies = int(input(f'Enter {Fore.GREEN}The Best internal rating{Style.RESET_ALL} of '
                                                  f'{Fore.BLUE}{name_of_company} and Co-debtors{Style.RESET_ALL}: '))

if internal_best_rating_of_companies >= 6:
    print(f'{Fore.RED}Not applicable.{Style.RESET_ALL} Best rating is above 6 and it is unacceptable.')
    exit()

for index in range(num_of_companies_in_group):
    if index == 0:
        current_revenue = float(input(f'{Fore.GREEN}Revenue{Style.RESET_ALL} of {Fore.BLUE} '
                                      f'{name_of_company}{Style.RESET_ALL} for last year (in thousands BGN): '))
        # Earning before interest, tax, depreciation and amortization:
        EBITDA = float(input(f'{Fore.GREEN}EBITDA{Style.RESET_ALL} of '
                             f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} for last year (in thousands BGN): '))
        # Existing loans:
        financial_debt = float(input(f'The {Fore.GREEN}total financial debt{Style.RESET_ALL} of '
                                     f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} '
                                     f'for last year(in thousands BGN): '))
        equity = float(input(f'{Fore.GREEN}Amount of EQUITY{Style.RESET_ALL} of '
                             f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} '
                             f'for last year(in thousands BGN): '))
        assets = float(input(f'{Fore.GREEN}Total Assets{Style.RESET_ALL} of '
                             f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} '
                             f'for last year(in thousands BGN): '))
    else:
        current_revenue = float(input(f'{Fore.GREEN}Revenue{Style.RESET_ALL} of '
                                      f'{Fore.BLUE}{list_of_co_debtors[index - 1]}{Style.RESET_ALL} '
                                      f'for last year (in thousands BGN): '))
        EBITDA = float(input(f'{Fore.GREEN}EBITDA{Style.RESET_ALL} of {Fore.BLUE}{list_of_co_debtors[index - 1]} '
                             f'{Style.RESET_ALL} for last year (in thousands BGN): '))
        financial_debt = float(input(f'{Fore.GREEN}Total financial debt{Style.RESET_ALL} of '
                                     f'{Fore.BLUE}{list_of_co_debtors[index - 1]}{Style.RESET_ALL} '
                                     f'for last year (in thousands BGN): '))
        equity = float(input(f'{Fore.GREEN}Amount of EQUITY{Style.RESET_ALL} of '
                             f'{Fore.BLUE}{list_of_co_debtors[index - 1]}{Style.RESET_ALL} '
                             f'for last year (in thousands BGN): '))
        assets = float(input(f'{Fore.GREEN}Total Assets{Style.RESET_ALL} of '
                             f'{Fore.BLUE}{list_of_co_debtors[index - 1]}{Style.RESET_ALL} '
                             f'for last year (in thousands BGN): '))
    total_equity += equity
    total_assets += assets
    total_revenue_of_group += current_revenue
    total_EBITDA_of_group += EBITDA
    total_financial_debt_of_group += financial_debt

if total_equity <= 0 or total_equity/total_assets <= 0.3:
    print(f'{Fore.RED}Not applicable.{Style.RESET_ALL} EQUITY is low.')
    exit()
if loan_amount_applying > total_revenue_of_group * 0.4:
    print(f'{Fore.RED}Not applicable.{Style.RESET_ALL} Loan amount must be under 40% from Revenue.')
    exit()
else:
    if total_financial_debt_of_group / total_EBITDA_of_group > 4:
        print(f'{Fore.RED}Not applicable.{Style.RESET_ALL}'
              f' Over leveraged company/group. DEBT/EBITDA must bu under 4.')
        exit()
    else:
        collateral_valuation = float(input(f'{Fore.GREEN}Liquidity value of collateral: '))
        if collateral_valuation / loan_amount_applying > 0.8:
            if num_of_companies_in_group == 1:
                print(
                    f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} is {Fore.GREEN}approved{Style.RESET_ALL} '
                    f'for the amount of {int(loan_amount_applying)} BGN')
            elif num_of_companies_in_group == 2:
                print(
                    f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} is {Fore.GREEN}approved{Style.RESET_ALL} for '
                    f'the amount of {int(loan_amount_applying)} BGN with Co-debtor {list_of_co_debtors}.')
            elif num_of_companies_in_group > 2:
                print(
                    f'{Fore.BLUE}{name_of_company}{Style.RESET_ALL} is {Fore.GREEN}approved{Style.RESET_ALL} '
                    f'for the amount of {int(loan_amount_applying)} BGN with Co-debtors: list(list_of_co_debtors).')
        else:
            print(f'{Fore.RED}Not enough collateral value.{Style.RESET_ALL} Minimum coverage must be 80%.')
            exit()