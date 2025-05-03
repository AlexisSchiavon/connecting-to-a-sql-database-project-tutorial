import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# 1) Connect to the database with SQLAlchemy
conexion = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
engine = create_engine(conexion, isolation_level="AUTOCOMMIT")
engine.connect()

# 2) Create the tables
with open('./src/sql/create.sql', 'r') as file:
    crear_script = file.read()
with engine.connect() as con:
    con.execute(text(crear_script))
    con.commit()  # Añadido commit después de crear tablas
print("Tablas creadas correctamente")

# 3) Insert data
with open('./src/sql/insert.sql', 'r') as file:
    insertar_script = file.read()
        
with engine.connect() as con:
    con.execute(text(insertar_script))
    con.commit()

# 4) Use Pandas to read and display a table
query = "SELECT * FROM books"
df = pd.read_sql_query(query, engine)
print("Tabla books:")
print(df)