import pandas as pd

file_path = 'adult.data' #if its in the same directory or provide the full path

columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
              'marital-status', 'occupation', 'relationship', 'race', 'sex',
              'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']

df = pd.read_csv(file_path, header=None, names=columns,na_values=' ?', skipinitialspace=True)

race_count = df['race'].value_counts()

average_age_men = df[df['sex'] == 'Male']['age'].mean()

bachelor_percentage = (df['education'] == 'Bachelors').mean() * 100

advanced_edu = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
high_edu_rich = df[advanced_edu]['salary'].eq('>50K').mean() * 100

low_edu = ~advanced_edu
low_edu_rich = df[low_edu]['salary'].eq('>50K').mean() * 100

min_hours = df['hours-per-week'].min()

min_workers = df[df['hours-per-week'] ==min_hours]
rich_min_workers = (min_workers['salary'] == '>50K').mean() * 100

country_pct = df.groupby('native-country')
rich_country = (country_pct['salary'].apply(lambda x: (x == '>50K').mean()) * 100)
high_earning_country = rich_country.idxmax()
high_earning_country_pct = rich_country.max()

top_job_india = df[(df['native-country'] == 'India') & 
                   (df['salary'] == '>50K')]['occupation'].mode()[0]

print("Race count:\n", race_count)
print("\n2.Average age of men:", average_age_men)
print("\n3.Percentage with Bachelors degree:", bachelor_percentage)
print("\n4.Percentaage with high education that earn >50K:", high_edu_rich)
print("\n5.Percentage without high education that earn >50K:", low_edu_rich)
print("\n6.Minimum hours worked per week:", min_hours)
print("\n7.Percentage of rich among those who work minimum hours:", rich_min_workers)
print("\n8.Country with highest percentage of rich people:", high_earning_country)
print("  Percentage of rich people in that country:", high_earning_country_pct)
print("\n9.Top occupation in India for those earning >50K:", top_job_india)