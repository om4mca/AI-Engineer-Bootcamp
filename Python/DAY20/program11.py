import time
import random
import logging
from contextlib import contextmanager

# Configure logging to mimic standard database server outputs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)


class ConnectionPool:
    """Simulates a database connection pool with limited sockets."""
    
    def __init__(self, max_connections: int = 3):
        self.max_connections = max_connections
        self.active_connections = 0

    def acquire(self, client_id: str) -> str:
        if self.active_connections >= self.max_connections:
            raise RuntimeError(f"Connection pool exhausted! (Active: {self.active_connections}/{self.max_connections})")
        self.active_connections += 1
        conn_id = f"CONN-{random.randint(1000, 9999)}"
        logging.info("POOL: Connection granted to [%s] -> Allocated [%s] (Active: %d/%d)", 
                     client_id, conn_id, self.active_connections, self.max_connections)
        return conn_id

    def release(self, conn_id: str, client_id: str):
        if self.active_connections > 0:
            self.active_connections -= 1
        logging.info("POOL: Connection [%s] returned by [%s] -> (Active: %d/%d)", 
                     conn_id, client_id, self.active_connections, self.max_connections)


# Instantiate a shared connection pool
db_pool = ConnectionPool(max_connections=2)


class DatabaseSession:
    """Represents an active database connection interface."""
    
    def __init__(self, conn_id: str):
        self.conn_id = conn_id
        self.in_transaction = False

    def execute(self, sql_query: str):
        if not self.in_transaction:
            raise RuntimeError("Cannot execute query without an active transaction!")
        logging.info("[%s] EXECUTING: %s", self.conn_id, sql_query)
        
        # Simulate query execution speed
        time.sleep(0.1)

    def commit(self):
        logging.info("[%s] TRANSACTION COMMIT -> Changes saved permanently.", self.conn_id)
        self.in_transaction = False

    def rollback(self):
        logging.warning("[%s] TRANSACTION ROLLBACK -> Undoing changes!", self.conn_id)
        self.in_transaction = False


@contextmanager
def db_connection(client_id: str, auto_commit: bool = True):
    """
    Context Manager to simulate acquiring/releasing database connections.
    Guarantees rollback on failure and release on exit.
    """
    # 1. Acquire resource
    conn_id = db_pool.acquire(client_id)
    session = DatabaseSession(conn_id)
    session.in_transaction = True
    logging.info("[%s] BEGIN TRANSACTION", conn_id)

    try:
        # 2. Hand session control to the 'with' block
        yield session

        # 3. Success behavior
        if auto_commit and session.in_transaction:
            session.commit()

    except Exception as error:
        # 4. Exception handling behavior
        logging.error("[%s] ERROR DETECTED: %s", conn_id, error)
        if session.in_transaction:
            session.rollback()
        raise  # Re-raise so calling code is aware of failure

    finally:
        # 5. Guaranteed cleanup (releases connection back to pool)
        db_pool.release(conn_id, client_id)


# ==========================================
# Running the Simulator
# ==========================================
if __name__ == "__main__":
    print("\n--- TEST 1: Successful Transaction ---")
    with db_connection(client_id="Service-A") as db:
        db.execute("INSERT INTO patients (id, name) VALUES (1, 'Aarav')")
        db.execute("UPDATE hospital_beds SET available = available - 1")

    print("\n--- TEST 2: Failed Transaction (Automatic Rollback) ---")
    try:
        with db_connection(client_id="Service-B") as db:
            db.execute("INSERT INTO billing (id, amount) VALUES (101, 5000)")
            # Simulating a system crash midway through transaction
            raise ValueError("Payment Gateway Failure!")
            db.execute("UPDATE status SET paid = True")
    except ValueError:
        print(">> Caught exception outside 'with' block safely.")

    print("\n--- TEST 3: Pool Exhaustion Error ---")
    try:
        # Acquiring 2 connections simultaneously fills the pool
        with db_connection(client_id="Task-1") as conn1:
            with db_connection(client_id="Task-2") as conn2:
                # Trying to acquire a 3rd connection fails safely
                with db_connection(client_id="Task-3") as conn3:
                    pass
    except RuntimeError as e:
        print(f">> Pool limit caught: {e}")