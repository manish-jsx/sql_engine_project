class SimpleSQLEngine:
    def __init__(self):
        self.tables = {}

    def execute(self, query):
        tokens = query.split()
        if not tokens:
            return "Empty query"
        
        command = tokens[0].upper()
        try:
            if command == 'CREATE':
                if tokens[1].upper() == 'TABLE':
                    return self._create_table(tokens)
                elif tokens[1].upper() == 'INDEX':
                    return self._create_index(tokens)
                else:
                    return "Unknown CREATE command"
            elif command == 'INSERT':
                return self._insert_into_table(tokens)
            elif command == 'SELECT':
                return self._select_from_table(tokens)
            elif command == 'UPDATE':
                return self._update_table(tokens)
            elif command == 'DELETE':
                return self._delete_from_table(tokens)
            elif command == 'DROP':
                if tokens[1].upper() == 'TABLE':
                    return self._drop_table(tokens)
                elif tokens[1].upper() == 'INDEX':
                    return self._drop_index(tokens)
                else:
                    return "Unknown DROP command"
            elif command == 'ALTER':
                if tokens[1].upper() == 'TABLE':
                    return self._alter_table(tokens)
                else:
                    return "Unknown ALTER command"
            elif command == 'JOIN':
                return self._join_tables(tokens)
            elif command == 'UNION':
                return self._union_tables(tokens)
            elif command == 'UNION ALL':
                return self._union_all_tables(tokens)
            elif command == 'EXISTS':
                return self._exists_operator(tokens)
            elif command == 'CASE':
                return self._case_statement(tokens)
            else:
                return "Unknown command"
        except Exception as e:
            return str(e)

    def _create_table(self, tokens):
        if len(tokens) < 4:
            return "Invalid CREATE TABLE syntax"
        
        table_name = tokens[2]
        columns = tokens[3].strip('()').split(',')
        self.tables[table_name] = {'columns': columns, 'data': []}
        return f"Table {table_name} created."

    def _create_index(self, tokens):
        if len(tokens) < 4:
            return "Invalid CREATE INDEX syntax"
        
        index_name = tokens[2]
        table_name = tokens[4]
        # Implement index creation logic here
        return f"Index {index_name} created on table {table_name}."

    def _insert_into_table(self, tokens):
        if len(tokens) < 5:
            return "Invalid INSERT INTO syntax"
        
        table_name = tokens[2]
        values = tokens[4].strip('()').split(',')
        if table_name not in self.tables:
            return f"Table {table_name} does not exist."
        
        if len(values) != len(self.tables[table_name]['columns']):
            return "Column count doesn't match value count"
        
        self.tables[table_name]['data'].append(values)
        return f"Inserted into {table_name}."

    def _select_from_table(self, tokens):
        if len(tokens) < 4:
            return "Invalid SELECT syntax"
        
        columns = tokens[1].split(',')
        table_name = tokens[3]
        if table_name not in self.tables:
            return f"Table {table_name} does not exist."
        
        data = self.tables[table_name]['data']
        selected_data = []

        for row in data:
            selected_row = [row[self.tables[table_name]['columns'].index(col)] for col in columns if col in self.tables[table_name]['columns']]
            selected_data.append(selected_row)

        return selected_data

    def _update_table(self, tokens):
        if len(tokens) < 4:
            return "Invalid UPDATE syntax"
        
        table_name = tokens[1]
        set_clause_index = tokens.index('SET')
        where_clause_index = tokens.index('WHERE') if 'WHERE' in tokens else len(tokens)
        
        columns_to_update = tokens[set_clause_index+1:where_clause_index]
        if len(columns_to_update) % 2 != 0:
            return "Invalid UPDATE syntax"
        
        set_columns = columns_to_update[::2]
        set_values = columns_to_update[1::2]
        
        # Implement update logic here
        return f"Updated table {table_name}."

    def _delete_from_table(self, tokens):
        if len(tokens) < 4:
            return "Invalid DELETE syntax"
        
        table_name = tokens[2]
        where_clause_index = tokens.index('WHERE') if 'WHERE' in tokens else len(tokens)
        
        # Implement delete logic here
        return f"Deleted from table {table_name}."

    def _drop_table(self, tokens):
        if len(tokens) < 3:
            return "Invalid DROP TABLE syntax"
        
        table_name = tokens[2]
        if table_name not in self.tables:
            return f"Table {table_name} does not exist."
        
        del self.tables[table_name]
        return f"Dropped table {table_name}."

    def _drop_index(self, tokens):
        if len(tokens) < 3:
            return "Invalid DROP INDEX syntax"
        
        index_name = tokens[2]
        # Implement index drop logic here
        return f"Dropped index {index_name}."

    def _alter_table(self, tokens):
        if len(tokens) < 4:
            return "Invalid ALTER TABLE syntax"
        
        table_name = tokens[2]
        # Implement alter table logic here
        return f"Altered table {table_name}."

    def _join_tables(self, tokens):
        if len(tokens) < 5:
            return "Invalid JOIN syntax"
        
        # Implement join logic here
        return "Joined tables."

    def _union_tables(self, tokens):
        if len(tokens) < 3:
            return "Invalid UNION syntax"
        
        # Implement union logic here
        return "Unioned tables."

    def _union_all_tables(self, tokens):
        if len(tokens) < 4:
            return "Invalid UNION ALL syntax"
        
        # Implement union all logic here
        return "Unioned all tables."

    def _exists_operator(self, tokens):
        if len(tokens) < 3:
            return "Invalid EXISTS syntax"
        
        # Implement exists operator logic here
        return "Exists operator applied."

    def _case_statement(self, tokens):
        if len(tokens) < 4:
            return "Invalid CASE syntax"
        
        # Implement case statement logic here
        return "Case statement applied."

# Example Usage
engine = SimpleSQLEngine()
print(engine.execute("CREATE TABLE students (name, age)"))
# print(engine.execute("INSERT INTO students VALUES ('Alice', 21)"))
# print(engine.execute("INSERT INTO students VALUES ('Bob', 22)"))
# print(engine.execute("SELECT name FROM students"))
# print(engine.execute("UPDATE students SET age = 23 WHERE name = 'Alice'"))
# print(engine.execute("DELETE FROM students WHERE name = 'Bob'"))
# print(engine.execute("DROP TABLE students"))
# print(engine.execute("CREATE INDEX idx_name ON students (name)"))
# print(engine.execute("DROP INDEX idx_name"))
# print(engine.execute("ALTER TABLE students ADD COLUMN grade"))
# print(engine.execute("SELECT * FROM students JOIN grades ON students.id = grades.student_id"))
# print(engine.execute("SELECT * FROM students UNION SELECT * FROM alumni"))
# print(engine.execute("SELECT * FROM employees UNION ALL SELECT * FROM former_employees"))
# print(engine.execute("SELECT name FROM students WHERE EXISTS (SELECT * FROM grades WHERE students.id = grades.student_id AND grades.grade = 'A')"))
# print(engine.execute("SELECT CASE WHEN age >= 18 THEN 'Adult' ELSE 'Minor' END AS category FROM students"))
