import psycopg2


class SQLQueryBuilder:
    def __init__(self):
        self._is_insert: bool = False

        self._is_select: bool = False

        self._is_updated: bool = False

        self._is_delete: bool = False

        self._from_table: str = ""

        self._fields: list[list[str]] = []

        self._where_list: list[str] = []

        self._values: list[list[str]] = []

        self._returnings: list[list[str]] = []

        self._raw_query: str = ""

        self._query = {
            "statement": "",
            "fields": self._fields,
            "from": self._from_table,
            "where_list": self._where_list,
            "values": self._values,
            "returnings": self._returnings,
        }

    def reset(self):
        self._is_insert = False

        self._is_select = False

        self._is_updated = False

        self._is_delete = False

        self._fields = []

        self._values = []

        self._returnings = []

        self._raw_query = ""

        self._query = {
            "statement": "",
            "fields": self._fields,
            "values": self._values,
            "returnings": self._returnings,
        }

    def insert_into(self, column: str):
        self.reset()

        self._is_insert = True

        statement = f"insert into {column}"

        self._query["statement"] = statement
        return self

    def select(self, fields: list[str]):
        self.reset()

        self._is_select = True

        self._query["statement"] = "select"
        self.fields(fields)
        return self

    def from_table(self, table: str):
        self._from_table = table
        return self

    def where(self, statement: str):
        self._where_list.append(statement)
        return self

    def fields(self, fields: list[str]):
        self._fields.append(fields)
        return self

    def get_fields(self) -> list[str]:
        fields = []

        for i in range(len(self._query["fields"])):
            for j in range(len(self._query["fields"][i])):
                field = self._query["fields"][i][j]

                fields.append(field)

        return fields

    def values(self, values: list[str]):
        self._values.append(values)
        return self

    def get_values(self) -> list[str]:
        values = []

        for i in range(len(self._query["values"])):
            for j in range(len(self._query["values"][i])):
                value = self._query["values"][i][j]

                values.append(value)

        return values

    def returning(self, fields: list[str]):
        self._returnings.append(fields)
        return self

    def get_returning_fields(self) -> list[str]:
        returnings = []

        for i in range(len(self._query["returnings"])):
            for j in range(len(self._query["returnings"][i])):
                returning = self._query["returnings"][i][j]

                returnings.append(returning)

        return returnings

    def data_type_format(self, value, quote_strings=True) -> str:
        if type(value) == str and quote_strings:
            return f"'{value}'"

        else:
            return f"{value}"

    def flat_matrix_to_string(self, matrix, quote_strings=False, separator=",") -> str:
        matrix_string = ""

        for i in range(len(matrix)):
            matrix_string += self.data_type_format(matrix[i], quote_strings)

            if i != (len(matrix) - 1):
                matrix_string += f"{separator} "

        return matrix_string

    def mount_query(self) -> None:
        self._raw_query = self._query["statement"] + " "

        if len(self._query["fields"]) > 0:
            if self._is_insert:
                self._raw_query += "( "

            
            self._raw_query += self.flat_matrix_to_string(self.get_fields())

            if self._is_insert:
                self._raw_query += " )"

        if self._is_select:
            self._raw_query += f" from {self._from_table}"

        if len(self._query["values"]) > 0:
            self._raw_query += f" values ( {self.flat_matrix_to_string(self.get_values(), quote_strings=True)} )"

        if len(self._where_list) > 0:
            for i in range(len(self._where_list)):
                if i == 0:
                    self._raw_query += f" where {self._where_list[i]}"
                else:
                    self._raw_query += f" and {self._where_list[i]}"

        if not self._is_select and len(self._query["returnings"]) > 0:
            self._raw_query += (
                f" returning {self.flat_matrix_to_string(self.get_returning_fields())}"
            )

        self._raw_query += ";"

    def get_query(self):
        return self._query

    def get_raw_query(self) -> str:
        self.mount_query()

        return self._raw_query

    def execute(self):
        executionResults = []

        self.mount_query()

        connection = psycopg2.connect(
            host="127.0.0.1",
            dbname="secret_db",
            user="secret_user",
            password="secret_password",
            port=5432,
        )

        cursor = connection.cursor()

        cursor.execute(self._raw_query)

        rows = cursor.fetchall()

        for row in rows:
            executionResult = {}

            fields_to_iterate = (
                self.get_fields() if self._is_select else self.get_returning_fields()
            )

            for j in range(len(fields_to_iterate)):
                executionResult[f"{fields_to_iterate[j]}"] = row[j]

            executionResults.append(executionResult)

        cursor.close()

        connection.commit()

        return executionResults[0] if len(executionResults) == 1 else executionResults
