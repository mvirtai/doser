"""JSON database connection and basic operations."""

import json
from pathlib import Path
from typing import Dict, List, Any


class JSONDatabase:
    def __init__(self, db_dir: str = "database"):
        self.db_dir = Path(db_dir)
        self.db_dir.mkdir(exist_ok=True)
        self.drugs_file = self.db_dir / "drugs.json"
        self.history_file = self.db_dir / "history.json"

        self._init_files()

    
    def _init_files(self):
        """Initialize JSON files if they don't exist."""
        if not self.drugs_file.exists():
            self._write_json(self.drugs_file, {"drugs": []})
        if not self.history_file.exists():
            self._write_json(self.history_file, {"history": []})
    
    def _read_json(self, file_path: Path) -> Dict[str, Any]:
        """Read JSON file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def _write_json(self, file_path: Path, data: Dict[str, Any]):
        """Write JSON file."""
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    
    # Perusoperaatiot - EI liiketoimintalogiikkaa
    def read_drugs(self) -> List[Dict[str, Any]]:
        """Read all drugs from database."""
        return self._read_json(self.drugs_file)["drugs"]
    
    def write_drugs(self, drugs: List[Dict[str, Any]]):
        """Write drugs to database."""
        self._write_json(self.drugs_file, {"drugs": drugs})
    
    def read_history(self) -> List[Dict[str, Any]]:
        """Read all history from database."""
        return self._read_json(self.history_file)["history"]
    
    def write_history(self, history: List[Dict[str, Any]]):
        """Write history to database."""
        self._write_json(self.history_file, {"history": history})
        