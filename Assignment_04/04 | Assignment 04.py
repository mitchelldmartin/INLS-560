# Requirements for Stock Trader position
MIN_YEARS_TRADING = 5
MIN_PORTFOLIO_VALUE = 100000  # Minimum portfolio value in dollars

# User data:
years_trading = int(input('Enter your years of experience trading stocks: '))
portfolio_value = int(input('Enter the highest portfolio value you have managed (in dollars): '))

# Evaluate UI
if years_trading >= MIN_YEARS_TRADING and portfolio_value >= MIN_PORTFOLIO_VALUE:
    print('You are eligible for the Stock Trader position.')
else:
    print(f'''
    You do not meet the requirements for the Stock Trader position.
    
    Minimum required years of experience: {MIN_YEARS_TRADING} years
    Your experience: {years_trading} years

    Minimum portfolio value managed: ${MIN_PORTFOLIO_VALUE}
    Your portfolio value: ${portfolio_value}
    ''')
