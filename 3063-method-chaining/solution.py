import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    """ animals2=animals[:][animals["weight"]>100]
    print(animals2)
    animals2.sort_values(by= ["weight"],ascending=False,inplace=True)
    print(f"sorted :\n{animals2}")"""
    return animals[animals["weight"]>100].sort_values(by= ["weight"],ascending=False)[["name"]]
