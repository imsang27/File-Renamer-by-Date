# File Renamer by Date

지정한 경로에 있는 파일들을 **생성일 기준**으로 정렬하여 이름을 변경하는 파이썬 스크립트입니다.  
폴더는 자동으로 제외되며, 사용자가 원하는 파일은 제외 목록에 추가할 수 있습니다.  
각 파일은 `n. 원래이름.확장자` 형식으로 번호가 붙습니다.

---

## 주요 기능
- ✅ 파일을 **생성일 기준**으로 번호를 매겨 이름 변경  
- ✅ **폴더 자동 제외**  
- ✅ 사용자 정의 **제외 파일 목록** 지원  
- ✅ `n. 파일이름.확장자` 형식으로 일괄 적용  

---

## 요구 사항
- Python 3.7 이상  
- Windows, Linux, macOS 환경 지원 (Windows에서 테스트됨)  

---

## 설치 방법
레포지토리 클론:
```bash
git clone https://github.com/imsang27/file-renamer-by-date
cd File Renamer by Date
```

---

## 사용 방법
파이썬으로 스크립트 실행:

```bash
python rename_files_by_creation_date.py
```

### 실행 예시
대상 폴더에 다음 파일들이 있다고 가정:
```
report.docx
notes.txt
README.md
```

`README.md`를 제외 목록에 추가하면 실행 후 결과:
```
1. report.docx
2. notes.txt
README.md   <- 변경 안 됨
```

---

## 설정
스크립트 내부에서 다음을 수정할 수 있습니다:
- **대상 경로**: `base_path = Path(r"C:\Users\Example\Documents\TargetPath")`  
- **제외 파일 목록**: `exclude_files = {"README.md", "skip_this.txt"}`  

---

## 라이선스
이 프로젝트는 **MIT License**를 따릅니다.
