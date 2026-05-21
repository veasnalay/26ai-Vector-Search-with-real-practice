import oracledb
import array
from sentence_transformers import SentenceTransformer

# ✅ STEP 1: load model FIRST
model = SentenceTransformer('all-MiniLM-L6-v2')

# ✅ STEP 2: connect DB
conn = oracledb.connect(
    user="hr",
    password="hr",
    dsn="10.10.1.2:1521/PDB23AI"
)

cursor = conn.cursor()

# ✅ STEP 3: query text
query_text = input("Search Employees :  ")

# ✅ STEP 4: create embedding AFTER model exists
query_vec = model.encode(query_text)

vec = array.array("f", query_vec)

# ✅ STEP 5: vector search
cursor.execute("""
SELECT employee_id, first_name, last_name
FROM hr.employees
ORDER BY embedding <-> :1
FETCH FIRST 5 ROWS ONLY
""", [vec])

for row in cursor:
    print(row)

conn.close()
