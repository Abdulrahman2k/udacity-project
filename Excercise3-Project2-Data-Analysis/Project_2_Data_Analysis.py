
# coding: utf-8

# # Data set used : Titanic Dataset

# Import Data using Pandas and check out the Datastructure by using .head(3) 3 for the number of records

# In[128]:

import pandas as pd
df = pd.read_csv('titanic_data.csv')
df.head(3)


# # Quality of Analysis

# Query: How does Age, Class of Travel, Sex affect the survivability of passengers in Titanic mishap?

# # Data Wrangling Phase

# Data Wrangling Step, fill up blank value with 0 for easier analysis using .fillna(0) Method

# In[129]:

df_na=df.fillna(0)


# In[130]:

df_na.head(3)


# Procedure to take the column value of Sex and based on the value make another column with output 0 or 1

# In[131]:

def return_sex_to_Number(column):
    if column =='female':
        return 1
    else:
        return 0
    


# Test the procedure

# In[132]:

return_sex_to_Number('female')


# Create new field (column) called Sexn, with numeric values, 1 for Women and 0 for men

# In[133]:

df_na['Sexn']= df_na.applymap(return_sex_to_Number)['Sex']


# In[134]:

df_na.head()


# # Exploration Phase

# we use correlation procedure to find out the statistical correlation between different Attributes like Age Sex  and Fare

# In[135]:

def correlation(x, y):
    x_int= (x-x.mean())/x.std(ddof=0) 
    y_int = (y-y.mean())/y.std(ddof=0)
    
    correlation =  x_int * y_int
    print correlation.mean()
    return correlation.mean()

    

Survived = df_na['Survived']
Sex = df_na['Sexn']
Age = df_na['Age'] [df_na.Age<>0]
Fare = df_na['Fare']



# Procedure to Convert Age in bins of 10 each for Age o to 10 will fall in bin 1 and so on and so forth

# In[136]:

def convert_age_in_bins(exam_grades):
    import pandas as pd
    value=0
    if exam_grades>=0 and exam_grades<=10:
        value = 1
    elif exam_grades>=11 and exam_grades<=20:
        value = 2
    elif exam_grades>=21 and exam_grades<=30:
        value = 3
    elif exam_grades>=31 and exam_grades<=40:
        value = 4
    elif exam_grades>=41 and exam_grades<=50:
        value = 5
    elif exam_grades>=51 and exam_grades<=60:
        value = 6
    elif exam_grades>=61 and exam_grades<=70:
        value = 7
    elif exam_grades>=71 and exam_grades<=80:
        value = 8
    elif exam_grades>=81 and exam_grades<=90:
        value = 9
    elif exam_grades>=91 :
        value = 10
        
    return value
#pd.qcut(exam_grades,
#                       [ 0.1, 0.2, 0.5, 0.8, 1],
#                       labels=['F', 'D', 'C', 'B', 'A'])
    
        # Pandas has a bult-in function that will perform this calculation
        # This will give the bottom 0% to 10% of students the grade 'F',
        # 10% to 20% the grade 'D', and so on. You can read more about
        # the qcut() function here:
        # http://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
        


# Test Script to test procedure

# In[137]:

convert_age_in_bins(99)


# process to create a new field with value of Bin based on Age Value and check the data frame rendered

# In[138]:

df_na['Agebin']=df_na.applymap(convert_age_in_bins)['Age'] [df_na.Age<>0]
df_na.head(3)


# # Exploration Phase 2

# In[139]:

df_na.groupby(['Survived','Sex','Agebin']).count()['PassengerId']


# In[140]:

df_na.groupby(['Survived','Embarked']).count()['PassengerId']


# Building dataframe for visual analysis 

# In[141]:

df_na_survived = df_na [(df_na.Survived == 1)]


# In[142]:

df_na_not_survived = df_na [(df_na.Survived == 0)]


# In[143]:

df_na_survived_female =df_na_survived [(df_na_survived.Sexn==1)]


# In[144]:

df_na_survived_male =df_na_survived [(df_na_survived.Sexn==0)]


# In[145]:

df_na_not_survived_female =df_na_not_survived [(df_na_not_survived.Sexn==1)]


# In[146]:

df_na_not_survived_male =df_na_not_survived [(df_na_not_survived.Sexn==0)]


# In[147]:

df_na_survived_male.head(3)


# In[148]:

df_na_survived_female.head(3)


# In[149]:

df_na_survived_female.groupby(['Survived','Agebin']).count()['PassengerId'].index.get_level_values('Agebin').tolist()


# In[150]:

df_na_survived_female.groupby(['Survived','Agebin']).count()['PassengerId'].values


# In[151]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().magic(u'pylab inline')
plt.plot(df_na_survived_female.groupby(['Survived','Agebin']).count()['PassengerId'].index.get_level_values('Agebin').tolist(), df_na_survived_female.groupby(['Survived','Agebin']).count()['PassengerId'].values) 
plt.plot(df_na_survived_male.groupby(['Survived','Agebin']).count()['PassengerId'].index.get_level_values('Agebin').tolist(), df_na_survived_male.groupby(['Survived','Agebin']).count()['PassengerId'].values) 

plt.xlabel("Age in Bins of 10 Years Each") 
plt.ylabel("Survival Frequency")
plt.title("Survival Frequency with Age in Bin of 10 Years (for Blue for Female and Green for Male)")


plt.show()


# In[152]:

plt.plot(df_na_not_survived_male.groupby(['Survived','Agebin']).count()['PassengerId'].index.get_level_values('Agebin').tolist(), df_na_not_survived_male.groupby(['Survived','Agebin']).count()['PassengerId'].values) 
plt.plot(df_na_not_survived_female.groupby(['Survived','Agebin']).count()['PassengerId'].index.get_level_values('Agebin').tolist(), df_na_not_survived_female.groupby(['Survived','Agebin']).count()['PassengerId'].values) 

plt.xlabel("Age in Bins of 10 Years Each") 
plt.ylabel("Victim Frequency")
plt.title("Victim Frequency with Age in Bin of 10 Years (for Blue for Male and Green for Female)")


# In[153]:

len((df_na.groupby(['Survived','Sex','Agebin']).count()['PassengerId']).index.get_level_values('Agebin'))


# In[154]:

len((df_na.groupby(['Survived','Sex','Agebin']).count()['PassengerId']).values)


# In[155]:

df_na.groupby(['Survived','Sex'] ).count()['PassengerId'].plot()

plt.xlabel("0 Means Victim, 1 Means Survivor ") 
plt.ylabel("Count of Passengers")
plt.title("Count of Passengers  for Male and Female, Victims and Survivors ")
plt.show()


# Finding out the Average Survival Ratio
# 

# In[156]:

Survival_ratio = round((float((df_na [(df_na.Survived==1)]).count()['Survived'])/ float(df_na.count()['Survived'])),3)
Survival_ratio


# In[157]:

field_column='Sexn'


# Function which returns Survival Ration Based on supplying parameters of Data Frame, Field and distinct Value
# 
# we will compare how the Average Survival Ratio are Statistically Related, Significant or Insignificant to each Field and Values.

# In[158]:

def survial_ratio_parameters(df, field, value):
    survival_ratio =0
    dividend = float((df[(df[field]==value) & (df.Survived==1)]).count()['Survived'])
    divisor  = float(df[(df[field]==value)].count()['Survived'])
    survival_ratio = round((dividend/divisor),3)
    return  survival_ratio  


# Survival Ratio of Field called Embarked with value of C

# In[159]:

survial_ratio_parameters(df_na,'Embarked','C')


# Find out unique values in Embarked Column

# In[160]:

list(set(df_na.Embarked))


# Procedure to return Character Zero for 0 number for easier comparision and removing a bug

# In[161]:

def classify_zero_to_charachter(char):
    if char ==0:
        return '0'
    else :
        return char


# In[167]:

classify_zero_to_charachter(0)


# This Command Ensure we are not Adding the Field Embarkedc Again

# In[168]:

df_na.drop('Embarkedc', axis=1, inplace=True)  


# Command to add Embarkedc Column with feature to convert 0 to '0'

# In[169]:

df_na['Embarkedc'] = df['Embarked'].map(classify_zero_to_charachter)


# In[170]:

list(set(df_na.Embarkedc))


# .fillna procedure fills up the blank value with '0'

# In[171]:

df_na.Embarkedc.fillna('0', inplace=True)


# list out unique values of Field Embarkedc

# In[172]:

list(set(df_na.Embarkedc))


# Survival Ratio of Women 

# In[173]:

survial_ratio_parameters(df_na,field_column,1)


# Survival Ratio of Men 

# In[174]:

survial_ratio_parameters(df_na,field_column,0)


# Survival Ratio of Pclass 1

# In[175]:

field_column='Pclass'


# In[176]:

survial_ratio_parameters(df_na,field_column,1)


# Survival Ratio of Pclass 2

# In[177]:

survial_ratio_parameters(df_na,field_column,2)


# Survival Ratio of Pclass 3

# In[178]:

survial_ratio_parameters(df_na,field_column,3)


# Survival Ratio of Age Bin 1 Range 0 to 10 Years

# In[179]:

field_column='Agebin'


# In[180]:

survial_ratio_parameters(df_na,field_column,1)


# Survival Ratio of Age Bin 2 Range 11 to 20 Years

# In[181]:

survial_ratio_parameters(df_na,field_column,2)


# Survival Ratio of Age Bin 3 Range 21 to 30 Years

# In[182]:

survial_ratio_parameters(df_na,field_column,3)


# Survival Ratio of Age Bin 4 Range 31 to 40 Years

# In[183]:

survial_ratio_parameters(df_na,field_column,4)


# Survival Ratio of Age Bin 5 Range 41 to 50 Years

# In[184]:

survial_ratio_parameters(df_na,field_column,5)


# Survival Ratio of Age Bin 6 Range 51 to 60 Years

# In[185]:

survial_ratio_parameters(df_na,field_column,6)


# Survival Ratio of Age Bin 7 Range 61 to 70 Years

# In[186]:

survial_ratio_parameters(df_na,field_column,7)


# In[187]:

survial_ratio_parameters(df_na,field_column,7)


# Survival Ratio of Age Bin 8 Range 71 to 80 Years

# In[188]:

survial_ratio_parameters(df_na,field_column,8)


# Survival Ratio of Siblings 0

# In[189]:

field_column='SibSp'


# In[190]:

survial_ratio_parameters(df_na,field_column,0)


# Survival Ratio of Siblings 1

# In[191]:

survial_ratio_parameters(df_na,field_column,1)


# Survival Ratio of Siblings 2

# In[192]:

survial_ratio_parameters(df_na,field_column,2)


# Survival Ratio of Siblings 3

# In[193]:

survial_ratio_parameters(df_na,field_column,3)


# Survival Ratio of Siblings 4

# In[194]:

survial_ratio_parameters(df_na,field_column,4)


# Survival Ratio of Siblings 5

# In[195]:

survial_ratio_parameters(df_na,field_column,5)


# Survival Ratio of Siblings 6

# In[196]:

survial_ratio_parameters(df_na,field_column,6)


# Survival Ratio of Siblings 7

# In[197]:

survial_ratio_parameters(df_na,field_column,7)


# Survival Ratio of Siblings 8

# In[198]:

survial_ratio_parameters(df_na,field_column,8)


# Survival Ratio based on Embarked Station Q

# In[199]:

field_column='Embarkedc'


# In[200]:

survial_ratio_parameters(df_na,field_column,'Q')


# Survival Ratio based on Embarked Station S

# In[201]:

survial_ratio_parameters(df_na,field_column,'S')


# Survival Ratio based on Embarked Station C

# In[202]:

survial_ratio_parameters(df_na,field_column,'C')


# This program will create a list and mark the fields and value with p value less than P critical value of .025, so that we can get a list of attribute which had survival ratio statistically significant than the population.

# In[203]:


def welch_T_test_result_param(key_field, df, field, value):
    import scipy.stats
    
    result = scipy.stats.ttest_ind(  df[key_field],df[key_field][df[field]==value] , equal_var=False)
    print result
    if result[1]<=.025:
        return(field, value,False,result[0],result[1])
    else:
        return(field, value,True,result[0],result[1])


# Creating a list final_result for appending all the columns and values, so that we can get a final list of Attributes and values which are statistically significant

# In[204]:

final_result=[]
# getting result for Embarked Station 'C'
final_result.append(welch_T_test_result_param ('Survived',df_na, 'Embarkedc', 'C'))
final_result


# In[205]:

# getting result for Embarked Station 'Q'
final_result.append(welch_T_test_result_param ('Survived',df_na, 'Embarkedc', 'Q'))
final_result


# In[206]:

# getting result for Embarked Station 'S'
final_result.append(welch_T_test_result_param ('Survived',df_na, 'Embarkedc', 'S'))
final_result


# In[207]:

# getting result for Siblings column Sibsp with bins 1 to 8
field_column='SibSp'
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 1))
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 2))
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 3))
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 4))
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 5))
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 8))
final_result


# In[208]:

# getting result for Siblings column Sibsp with bins 1 to 8
field_column='Pclass'
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 1))
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 2))
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 3))
final_result


# In[209]:

# getting result for Sex 1 for Female, 0 for Male
field_column='Sexn'
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 1)) # Female
final_result.append(welch_T_test_result_param ('Survived',df_na, field_column, 0)) # Male
final_result


# In[210]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().magic(u'pylab inline')
list = []
list = (df_na['Age']  [isnan(df_na.Age)==False]  [df_na.Age<>0]  )
plt.hist(list.values  , bins=10) 
plt.title("Age Histogram")
plt.xlabel("Age in 10 Years Bin")
plt.ylabel("Frequency")
plt.show()


# In[211]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

get_ipython().magic(u'pylab inline')
list = []
list = (df_na['Age'] [df_na.Survived==0]  [isnan(df_na.Age)==False]  [df_na.Age<>0] )
plt.hist(list.values  , bins=10) 
plt.title("Victim Age Histogram")
plt.xlabel("Age in 10 Years Bin")
plt.ylabel("Frequency")
plt.show()


# In[212]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

get_ipython().magic(u'pylab inline')
list = []
population = (df_na['Age'] [isnan(df_na.Age)==False]  [df_na.Age<>0] )
list = (df_na['Age'] [df_na.Survived==1] [isnan(df_na.Age)==False]  [df_na.Age<>0] )
list_victim = (df_na['Age'] [df_na.Survived==0] [isnan(df_na.Age)==False]  [df_na.Age<>0] )
plt.hist(population.values  , bins=10, color='y',alpha =0.5, label='Population')
plt.hist(list_victim.values  , bins=10, color='c',alpha =0.5, label='Victim' ,linestyle=':')
plt.hist(list.values  , bins=10, color='m', label='Survivor' ,linestyle='-.')

plt.title("Survivors/Victims Age Histogram")
plt.xlabel("Age in 10 Years Bin")
plt.ylabel("Frequency")
plt.legend()
plt.show()


# In[213]:

import scipy
from scipy.stats import pearsonr


r_row, p_value = pearsonr(df_na['Age'], df_na['Survived'])

print r_row
print p_value
if p_value <.05 :
    print 'Statistically Significant'


# Pearson coefficient aims to quantify the relationship that might exist between two variables Age and Survivability on a scatter plot.-1.0 is a strong inverse relationship, 0 indicates no relationship, +1.0 is a strong direct relationship, as per above calculation of pearsons R value  0.0105392158713  is low direct relationship 
# 
# If the p-value is low (generally less than 0.05), then our correlation is statistically significant, and you can use the calculated Pearson coefficient.
# 
# If the p-value is not low (generally higher than 0.05), then our correlation is not statistically significant (it might have happened just by chance) and we should not rely upon your Pearson coefficient.
# 
# as per p value of 0.75340049694 is greater than .05, hence this is not statistically significant

# In[214]:

import scipy
from scipy.stats import pearsonr


r_row, p_value = pearsonr(df_na['Sexn'], df_na['Survived'])
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

get_ipython().magic(u'pylab inline')
plt.scatter(df_na['Sexn'].values, df_na['Survived'].values)
plt.show()
print r_row
print p_value
if p_value <.05 :
    print 'Statistically Significant'


# calculation of pearsons R value  0.543351380658  is High direct relationship
# 
# Since P Value is less than .05, the Pearsons Coefficient is Statistically Significant

# In[215]:

import scipy
from scipy.stats import pearsonr


r_row, p_value = pearsonr(df_na['Pclass'], df_na['Survived'])

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

get_ipython().magic(u'pylab inline')
plt.scatter(df_na['Pclass'].values, df_na['Survived'].values)
plt.show()
print r_row
print p_value
if p_value <.05 :
    print 'Statistically Significant'


# calculation of pearsons R value  -0.338481035961  is strong inverse relationship
# 
# Since P Value is less than .05, the Pearsons Coefficient is Statistically Significant

# In[216]:

import scipy
from scipy.stats import pearsonr


r_row, p_value = pearsonr(df_na['SibSp'], df_na['Survived'])

print r_row
print p_value
if p_value <.05 :
    print 'Statistically Significant'


# calculation of pearsons R value  -0.338481035961  is Weak inverse relationship
# 
# Since P Value is less than .05, the Pearsons Coefficient is Not Statistically Significant

# In[217]:

# Printing Attributes and Values whose probability is 
for i in final_result:
    if i[4]<=.025:
        print 'The Attribute ', i[0], ' is Statistically Significant  with column value ', i[1], '  at P value of ',round(i[4],3)


# # Conclusion

#  As per our Analysis, the population mean survival ratio is 0.384, and  the passengers who embarked on the Station C had a less Survival ratio Mean of 0.554 , to confirm the significance level, we did a Welch T test and confirmed that this attribute is statistically significant.
#  
#  with P critical value of 0.025
# 
# Similary our Analysis has concluded that Following Attributes Survival ration were Statistically Signficant 
# 
# Passengers with 1 Sibiling
# Passengers with 5 Sibiling
# Passengers with 8 Sibiling
# 
# 
#  with P critical value of 0.025
# 
# Similary our Analysis has concluded that Following Attributes Survival ratios were Statistically Signficant 
# 
# Passengers with Class 1 
# Passengers with Class 3 
# 
# our Analysis has concluded that Following Attributes Survival ration were Statistically Signficant
# 

# As per Analysis Using Pearsons R
# 
# Age and Survival were does Not have a Strong Relationship as per Pearsons Coefficeint 0.0105392158713 and as per P value 0.75340049694 is not Statistically Significant
# 
# Sex and Survival were does have a Strong Relationship as per Pearsons Coefficeint 0.543351380658 and as per P value 1.40606613088e-69 is Statistically Significant
# 
# 
# PClass and Survival were does have a Strong Relationship as per Pearsons Coefficeint -0.338481035961 and as per P value 2.53704738798e-25 is Statistically Significant
# 
# SibSp (Number of Siblings) and Survival were does Not have a Strong Inverse Relationship as per Pearsons Coefficeint 0.0353224988857 and as per P value 0.292243928698 is Not Statistically Significant
# 
# 
# 

# # Data Wrangling Risk Introduced through Fillna method

# For Easier Analysis we have filled up missing values of Age with 0, this is a misstep and on realization, we are compensating our analysis by ensuring that our analysis is not assuming Age with values 0, using clause [df_na.Age<>0] to essentially ignore missing information and continue processing
