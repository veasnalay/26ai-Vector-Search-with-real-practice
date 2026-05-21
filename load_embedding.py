import oracledb
import array
from sentence_transformers import SentenceTransformer

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Connect (Thin mode - no Oracle client needed)
conn = oracledb.connect(
    user="hr",
    password="hr",
    dsn="10.10.1.2:1521/PDB23AI"
)

cursor = conn.cursor()

# Query data
cursor.execute("""
SELECT employee_id,
       first_name || ' ' || last_name || ', ' ||
       job_id || ', salary ' || salary || ', dept ' || department_id AS text_data
FROM hr.employees
""")

rows = cursor.fetchall()

# Prepare batch
ids = [r[0] for r in rows]
texts = [r[1] for r in rows]

# Generate embeddings (FAST)
embeddings = model.encode(texts, batch_size=32)

# Update back to Oracle
update_sql = """
UPDATE hr.employees
SET embedding = :1
WHERE employee_id = :2
"""

for i in range(len(ids)):
    vec = array.array("f", embeddings[i])
    cursor.execute(update_sql, [vec, ids[i]])

conn.commit()

print("✅ Embeddings stored successfully")
