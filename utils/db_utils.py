import pandas as pd
import os
from sqlalchemy import create_engine, text

#build connection to the database
bridge = create_engine(os.environ.get("NEON_DB_URL"), echo=True)

def db_fetch(query, var_dic=None):
    with bridge.connect() as conn:
        result = conn.execute(text(query), var_dic)
        return pd.DataFrame(result.mappings())
    
