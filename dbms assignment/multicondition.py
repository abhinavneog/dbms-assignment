import re

def nl_to_sql_v2(query):
    query = query.lower()
    sql = "SELECT * FROM students"

    conditions = []

    # Check for age conditions
    if "older than" in query:
        number = re.findall(r'\d+', query)[0]
        conditions.append(f"age > {number}")
    if "younger than" in query:
        number = re.findall(r'\d+', query)[0]
        conditions.append(f"age < {number}")

    # Check for grade conditions
    if "grade" in query:
        match = re.search(r'grade\s+([a-z])', query)
        if match:
            grade = match.group(1).upper()
            conditions.append(f"grade = '{grade}'")

    # Combine conditions
    if "and" in query:
        sql += " WHERE " + " AND ".join(conditions)
    elif "or" in query:
        sql += " WHERE " + " OR ".join(conditions)

    sql += ";"
    return sql

# Example
print(nl_to_sql_v2("List students older than 20 and with grade A"))