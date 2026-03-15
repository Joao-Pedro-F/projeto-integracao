import os
import psycopg

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_m0ZpALNQ5Rct@ep-quiet-king-ac16a4rs-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

def conectar():
    return psycopg.connect(DATABASE_URL)