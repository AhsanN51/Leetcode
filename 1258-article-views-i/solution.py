import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    """views=views[views["author_id"] == (views["viewer_id"])][["author_id"]]
   
    views.drop_duplicates(inplace=True)
  
    views.sort_values(by="author_id",inplace=True)

    views.rename(columns={"author_id":"id"},inplace=True)"""

    return views[views["author_id"] == (views["viewer_id"])][["author_id"]].drop_duplicates().sort_values(by="author_id").rename(columns={"author_id":"id"})
