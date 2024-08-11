import pandas as pd


present_df = pd.read_csv('present.csv')
main_df = pd.read_csv('main.csv')


present_set = set(present_df['Number'])
main_set = set(main_df['Number'])


numbers_not_in_present = main_set - present_set


result_df = pd.DataFrame(numbers_not_in_present, columns=['Number'])

result_df.to_csv('numbers_not_in_present.csv', index=False)

print("Numbers in 'main' but not in 'present' have been saved to 'numbers_not_in_present.csv'.")
