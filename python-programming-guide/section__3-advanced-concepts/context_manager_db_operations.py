class PostgreSQLTransaction:
    """
    A context manager for managing PostgreSQL transactions.

    This class handles opening and closing connections, managing transactions,
    and providing a cursor for database operations. It can also optionally reuse
    an existing database connection.

    Attributes:
        connection_params (dict): Parameters required to establish a PostgreSQL connection.
        conn (psycopg2.extensions.connection): A psycopg2 connection object.
        owns_connection (bool): Indicates whether the class owns the connection (i.e., created it).

    Usage example:
        connection_params = {
            'dbname': 'mydatabase',
            'user': 'myusername',
            'password': 'mypassword',
            'host': 'server_ip',
            'port': 5432
        }

        with PostgreSQLTransaction(**connection_params) as transaction:
            transaction.set_search_path('tenant')
            with transaction.cursor() as cursor:
                cursor.execute("SELECT * FROM my_table;")
                for row in cursor.fetchall():
                    print(row)
    """

    def __init__(self, dbname, user, password, host, port=5432, connection=None):
        """
        Initializes the PostgreSQLTransaction context manager.

        Parameters:
            dbname (str): The name of the database.
            user (str): The username used to authenticate.
            password (str): The password used to authenticate.
            host (str): The host address of the database server.
            port (int, optional): The port number of the database server. Defaults to 5432.
            connection (psycopg2.extensions.connection, optional): An existing psycopg2 connection object.
        """
        self.connection_params = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port
        }
        self.conn = connection
        self.owns_connection = connection is None

    def __enter__(self):
        """
        Enter the runtime context for the PostgreSQLTransaction object.

        Establishes a new database connection if one wasn't provided, and starts a new transaction.

        Returns:
            PostgreSQLTransaction: The instance itself.
        """
        if self.owns_connection:
            # Establish a new database connection if one wasn't provided
            self.conn = psycopg2.connect(**self.connection_params)
        # Start a new transaction
        self.conn.autocommit = False
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Exit the runtime context for the PostgreSQLTransaction object.

        Commits the transaction if no exceptions occurred, otherwise rolls back.
        Closes the connection if it was created by this class.

        Parameters:
            exc_type: The type of the exception.
            exc_value: The value of the exception.
            traceback: The traceback object.
        """
        try:
            if exc_type is not None:
                # If there's an exception, roll back any changes
                self.conn.rollback()
                logging.error("Transaction rolled back due to an exception", exc_info=(exc_type, exc_value, traceback))
            else:
                # If everything went well, commit the changes
                self.conn.commit()
        finally:
            if self.owns_connection:
                # Close the connection only if it was created by this class
                self.conn.close()
                if self.conn.closed:
                    logging.info(f"Connection to the database is closed.")
                else:
                    logging.warning("Connection was not closed.")

    def cursor(self):
        """
        Create a new cursor object using the current connection.

        The cursor is used to perform database operations. It should be used within a 'with' statement
        to ensure that it is closed properly after use.

        Returns:
            psycopg2.extensions.cursor: A new cursor object for the current connection.
        """
        return self.conn.cursor()

    def set_search_path(self, schema):
        """
        Set the search path to a specific schema for the current connection.

        Parameters:
            schema (str): The name of the schema to set as the search path.
        """
        with self.cursor() as cur:
            cur.execute(f"SET search_path TO {schema};")
