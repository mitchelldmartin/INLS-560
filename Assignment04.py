# Constants for Stock Options Trader
MIN_YEARS_TRADING = 3
MIN_STARTING_CAPITAL = 25000

# User input
years_trading = int(input('Enter your years of trading experience: '))
starting_capital = int(input('Enter your available starting capital: '))

# Eligibility
if years_trading >= MIN_YEARS_TRADING and starting_capital >= MIN_STARTING_CAPITAL:
    print(f'\nCongratulations! You are able to trade options!')
else:
    print(f'''
    Unfortunately, you do not meet the requirements to trade options.
    
    Required Minimums:
    - Years of trading experience: {MIN_YEARS_TRADING}
    - Starting capital: {MIN_STARTING_CAPITAL}
    
    Your Input:
    - Years of trading experience: {years_trading}
    - Starting capital: {starting_capital}
    
    Please review the requirements and try again when eligible.
    ''')