import os
from pathlib import Path

# 기준 경로
base_path = Path(r"C:\Users\Example\Target\Path")

# 제외할 파일명 (리스트로 관리)
exclude_files = {"exclude1.txt", "skip_this.docx"}

# 파일만 가져오기 (폴더 제외)
files = [f for f in base_path.iterdir() if f.is_file() and f.name not in exclude_files]

# 생성일 기준 정렬
files.sort(key=lambda x: x.stat().st_ctime)

# 번호 매겨 이름 변경
for idx, file in enumerate(files, start=1):
    new_name = f"{idx}. {file.name}"
    new_path = file.with_name(new_name)
    os.rename(file, new_path)
    print(f"Renamed: {file.name} -> {new_name}")
