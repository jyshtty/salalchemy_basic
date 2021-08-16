import sqlalchemy as db

engine = db.create_engine("sqllite3:///movies.db")

connection = engine.connect()

metadata = db.Metadata()

movies = db.Table('movies', metadata, autoload = True, autoload_with = engine)

query = db.select([movies])

result_proxy = result_proxy.fetchall()

print(result_set[0])

query = db.select([movies]).where(movies.columns.Director == 'Marthin Scorsese'

connection.execute(query)

result_proxy = result_proxy.fetchall()

print(result_set[0])



