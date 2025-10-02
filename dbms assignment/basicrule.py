import re

def nl_to_sql(query):
    query = query.lower()
    sql = "SELECT * FROM students"

    if "above" in query:
        number = re.findall(r'\d+', query)[0]
        sql += f" WHERE marks > {number};"
    elif "below" in query:
        number = re.findall(r'\d+', query)[0]
        sql += f" WHERE marks < {number};"
    elif "equal" in query:
        number = re.findall(r'\d+', query)[0]
        sql += f" WHERE marks = {number};"
    return sql


# Example queries
queries = [
    "Show all students with marks above 80",
    "List all students with marks below 50",
    "Find students with marks equal to 90"
]

for q in queries:
    print("Input (Natural Language):", q)
    print("Output (SQL):", nl_to_sql(q))
    print()