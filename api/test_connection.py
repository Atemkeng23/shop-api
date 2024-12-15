from api.database import SessionLocal

def test_connection():
    try:
        db = SessionLocal()
        result = db.execute("SELECT name FROM sys.databases")
        print("Bases de données accessibles :", [row[0] for row in result])
    except Exception as e:
        print("Erreur de connexion :", str(e))
    finally:
        db.close()

test_connection()
