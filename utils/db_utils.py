import pandas as pd
import os
from sqlalchemy import create_engine, text

#build connection to the database
bridge = create_engine(os.environ.get("NEON_DB_URL"), echo=True)

def fetch_db(query, query_dic=None):
    with bridge.connect() as conn:
        result = conn.execute(text(query), query_dic)
        return pd.DataFrame(result.mappings())

 def edit_db(query, query_dic=None):
    with bridge.begin() as conn:
        result = conn.execute(text(query), query_dic)
        return pd.DataFrame(result.mappings())   
