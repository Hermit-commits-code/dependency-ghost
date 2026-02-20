import json
import sqlite3
from datetime import datetime, timedelta, timezone
from pathlib import Path


class CacheManager:
    def __init__(self, db_path="~/.skopos/audit_cache.db"):
        self.db_path = Path(db_path).expanduser()
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS audits (
                    package_name TEXT,
                    version TEXT,
                    score INTEGER,
                    meta_json TEXT,
                    timestamp DATETIME,
                    PRIMARY KEY (package_name, version)
                )
            """)

    def get_cached_audit(self, package_name, version):
        """Retrieves a result only if it's less than 24 hours old."""
        query = "SELECT score, meta_json, timestamp FROM audits WHERE package_name = ? AND version = ?"
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(query, (package_name, version)).fetchone()

        if row:
            score, meta_json, ts_str = row
            ts = datetime.fromisoformat(ts_str)
            if datetime.now(timezone.utc) - ts < timedelta(hours=24):
                return score, json.loads(meta_json)
        return None

    def save_audit(self, package_name, version, score, meta):
        """Upserts a forensic audit result into the local cache."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO audits (package_name, version, score, meta_json, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    package_name,
                    version,
                    score,
                    json.dumps(meta),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )
