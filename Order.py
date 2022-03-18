from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
from sqlalchemy import MetaData, Table, select
metadata = MetaData()
census = Table('census', metadata,autoload=True, autoload_with=engine)
stmt = select([census.columns.state])
results = connection.execute(stmt).fetchall()
print(results[:10])
"""selanjutnya adalah mengurutkan secara ascending"""
stmt = select([census.columns.state])
stmt = stmt.order_by(census.columns.state)
results = connection.execute(stmt).fetchall()
print(results[:10])

"""descending"""
from sqlalchemy import desc
stmt = select([census.columns.state])
stmt = stmt.order_by(desc(census.columns.state))
print(stmt)
results = connection.execute(stmt).fetchall()
print(results[:10])

"""multiple order"""
stmt = select([census.columns.state, census.columns.sex])
stmt = stmt.order_by(census.columns.state, census.columns.sex)
results = connection.execute(stmt).first()
print(results)
print(stmt)
