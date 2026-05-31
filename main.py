import pandas as pd
# create the analysis var which will be represented as a markdown code
analysis=""
data=pd.read_csv("school-enrolment/share-of-children-enrolled-in-pre-primary-school.csv")
# a function to see the groath
def Groath(value):
    if value > 0:
        return f"increased by {value:.2f}%"
    elif value < 0:
        return f"decreased by {abs(value):.2f}%"
    else:
        return "no change"
# see how many countries encluded
countryiesNumber=data["Entity"].nunique()
FromYear=data["Year"].min()
ToYear=data["Year"].max()
analysis+=f"""# Overview

This dataset represents the pre-primary school enrollment percentage in about {countryiesNumber} countries from {FromYear} to {ToYear}
## Methodology

- Enrollment rates were analyzed using available records.
- Changes were calculated between consecutive observations.

"""
# get all countries
Countries=data["Entity"].unique()
# get the countries information and put them in the file.
countriesMD=""
ranking=[]
for country in Countries:
    # define the country's index
    indexes=data[data["Entity"]==country].copy()
    indexes=indexes.sort_values("Year")
    enrollment_percentage =indexes["Pre-primary education"]
    # get the average 
    average=enrollment_percentage.mean()
    ranking.append({"average":average,"country":country})
    state=""
    if average>=85:
        state="very high"
    elif average>=70:
        state="high"
    elif average>=50:
        state="medium"
    elif average>=30:
        state="low"
    else:
        state="verry low"
    countriesMD+=f"## {country}\n### summary\nThe average pre-primary school enrollment rate was {average:.2f}% {state}\n\n"
    
    # get the change
    indexes["change"]=enrollment_percentage.diff()
    # get the difrent btween the first and last year
    FirstYear=indexes["Pre-primary education"].iloc[0]
    lastYear=indexes["Pre-primary education"].iloc[-1]
    change=lastYear-FirstYear
    countriesMD+=f'the enrollment rate from {str(indexes["Year"].iloc[0])} to {str(indexes["Year"].iloc[-1])} is {Groath(change)} \n### Country Report\n\n'
    for I in range(1,len(indexes)):
        Year1=indexes["Year"].iloc[I-1]
        year2=indexes["Year"].iloc[I]
        change=indexes["change"].iloc[I]
        if pd.isna(change):
            change=0
        countriesMD+=f"- {str(Year1)}/{str(year2)} enrollment rate has been {Groath(change)}\n"
    countriesMD+="\n"
# put the 5highest and 5lowest countries
rankingArray=pd.DataFrame(ranking)
Top5=rankingArray.sort_values("average",ascending=False).head(5)
bottem5=rankingArray.sort_values("average").head(5)
analysis+="## top 5 countries\n\n"
for _,rowl in Top5.iterrows():
    analysis+=f'- {rowl["country"]} : {rowl["average"]:.2f}%\n'
analysis+="## bottem5 countries\n\n"
for _,rowl in bottem5.iterrows():
    analysis+=f"- {rowl['country']} : {rowl['average']:.2f}%\n"
# get the highest and the lowest
highest = rankingArray.loc[rankingArray["average"].idxmax()]
lowest = rankingArray.loc[rankingArray["average"].idxmin()]

analysis += f"""# Summary
- {highest['country']} has the highest enrollment with {highest['average']:.2f}%
- {lowest['country']} has the lowest enrollment with {lowest['average']:.2f}%
# Full report

"""
analysis+=countriesMD
# save the markdown file
with open("analysis.md","w",encoding="utf-8") as file:
    file.write(analysis)
    print("Done!")
