import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset('tips')
tips.describe()
tips.head()
sns.displot(tips.total_bill)
sns.displot(tips.total_bill,kde=True)

#the distribution is right skewed
##positive skewed-> meaning most total bills are on lower side(left)
#but there are few large bills that stretch distribution to right.
#This is typical in restaurant or service data,
#where most meals fall within avg range, but few parties may spend much more.
sns.displot(tips.tip,kde=True)
#The plot is right skewed-> meaning having higher distributions to lower values for tips present at right side of a plot
sns.jointplot(x=tips.tip,y=tips.total_bill)
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='reg')
'''
scatter plot(center):
Each point represents one observation
(a customers bill and correspondings tip)
there's positive correlation: as total bill increases, tip trend increase as well.
However, increase is not perfectly linaer some variation exisits, especially for higher bills.

Histogram on x-axis(top):
shows distributin of tio amount. Most tips fall between $2 and $4, with fewer tips at higher end.

Histogram on y-axis(right):
shows distribution of total bill. the majority of bill are in $10-$20 range
'''
sns.jointplot(x=tips.tip,y=tips.total_bill,kind='hex')
sns.pairplot(tips,kind='reg')

'''
total_bill vs tip
positive correlation: as total bill increases, tip amount increases.
The point are fairly spread, but there's visible upward trend.

total_bill vs size
weak positive correlationn: larger group sizes trend to have hgigher total bills.

still, there's a lot of overlap-small groups can also have high bills.
tip vs size
weak: correlation: bigger groups don't always give higher tips.
most tips, even in larger groups, still hover around $2-$5.
'''

#most of customers are coming for dinner and 50% are coming lunch
sns.pairplot(tips,hue='time')
'''
variable-wise insight:
    1. total_bill distribution(top_left):
        dinner bills are generally higher than lunch bills(peak shift right).
        
    dinner has wider spread in total bill amount (some>$40),
    while lunch is concertrated below $20.
    
    2.tip distribution:
        dinner tips also trnd to be higher than lunch tips.
        There's greater variance in tips given during dinner.
        
    3. size distribution:
        dinner groups are larger on average- more size values >=3.
        lunch groups tend to smaller (mostly 2 people).
        
Realtionship between variable:
total_bill vs tip:
positive correlation for both lunch and dinner
Dinner tips show greater variablility, especially at higher bill.

total_bill vs size:
slights upward trend: larger groups trnd to have higher bills, more so during dinner.
some large dinner partiesm(size 5-6) have high bills.            
'''

sns.pairplot(tips,hue='day')

'''
total bill distribution:
    sat (green) shows wider spread and higher peak in total bills - more people spreading higher amount
    fri (orange) shows lower density, suggests fewer transactions.
tip distribution:
    sat and sun have more high tips than thus and fri.
    fri again has smaller range and volume of tips.
size districution:
    most groups are 2 and 3 people across all days.
    
saturday has higher peak at 2 people, indicating more frequents small
'''
sns.heatmap(tips.corr(numeric_only=True),annot=True)
'''
Understanding Correlation Coefficients
Ranges from -1 to +1.
+1 → perfect positive correlation (both increase together).
0 no correlation.
-1 → perfect negative correlation (one increases, the other decreases).
total_bill & tip 0.68 Strong positive correlation higher bills generally lead to higher tips. Makes intuitive sense: Larger orders → more tipping.
total_bill & size 0.60 Moderate positive correlation Larger groups usually order more, resulting in bigger bills.
tip & size 0.49 Moderate correlation bigger groups tend to leave Larger tips, but not as tightly related as bill amount.
Possibly affected by splitting behavior.
'''
sns.boxenplot(tips.total_bill)
#there are outliers in total_bills
sns.boxplot(tips.tip)
#there is outlier
sns.countplot(tips.day)
tips.time.value_counts()

#
sns.countplot(tips.sex)
#more male customers are coming compared to female
tips.sex.value_counts().plot(kind='pie')
tips.sex.value_counts().plot(kind='bar')
sns.countplot(data=tips[tips.time=='Dinner'],x='day')
#for dinner, most of customers are coming on sat and sun
#very few customers are coming for dinner on thu and fri
sns.countplot(data=tips[tips.time=='Lunch'],x='day')
#most of customers are coming for lunch on thu and fri and there are no customers coming sat and sun
fg=sns.FacetGrid(tips,row='smoker',col='time')
fg.map(sns.histplot,'total_bill')

'''
This is a facet grid of histograms showing the distribution of total bills across different smoking statuses and time of day (Lunch vs Dinner).
Top-Left: Smokers during Lunch
Top-right: Smokers during Dinner
Bottom-Left: Non-smokers during Lunch
Bottom-right: Non-smokers during Dinner
Smokers vs. Non-Smokers
Dinner (Top-right vs Bottom-right):
Both smokers and non-smokers show similar bill
patterns, with peaks between $15-$25.
Smokers have a slightly more spread-out distribution, indicating more variability.
'''




