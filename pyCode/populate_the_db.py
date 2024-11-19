import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from swims_db import FreestyleMenNCAA  


df = pd.read_excel("top16_100free.xlsx", sheet_name="100 freestyle NCAA men", usecols="A:D")

#
engine = create_engine('sqlite:///swims.db?check_same_thread=False')
Session = sessionmaker(bind=engine)
session = Session()


for index, row in df.iterrows():
    swim = FreestyleMenNCAA(
        Place=row['Place'],
        Time=row['Time'],
        Year=row['Year'],
        School=row['School']
    )
    
    session.add(swim)
session.commit()
session.close()

print("Data has been successfully inserted into the database!")