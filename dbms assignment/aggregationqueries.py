def nl_to_sql_v3(query):
    query = query.lower()

    if "average marks" in query:
        return "SELECT AVG(marks) FROM students;"
    elif "maximum marks" in query or "highest marks" in query:
        return "SELECT MAX(marks) FROM students;"
    elif "minimum marks" in query or "lowest marks" in query:
        return "SELECT MIN(marks) FROM students;"
    elif "count students" in query:
        return "SELECT COUNT(*) FROM students;"
    else:
        return "Unsupported aggregation query."

# Examples
print(nl_to_sql_v3("Find the average marks of students"))
print(nl_to_sql_v3("Find the maximum marks of students"))
print(nl_to_sql_v3("Count students"))