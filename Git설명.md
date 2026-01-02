# SVN → Git 용어 & 명령어 

---

## 1. SVN 용어 ↔ Git 용어

### 기본 개념 대응

| SVN 용어           | Git 용어          | 설명                               |
| ------------------ | ----------------- | ---------------------------------- |
| Repository         | Repository        | 저장소 (개념 동일)                 |
| Central Repository | Remote Repository | Git에서 서버는 공유용              |
| Working Copy       | Working Directory | 작업 중인 파일                     |
| Revision           | Commit            | Git은 숫자 대신 hash               |
| Checkout           | Clone / Checkout  | clone = 최초 복사, checkout = 이동 |
| Update             | Pull              | 최신 변경사항 가져오기             |
| Commit             | Commit            | Git은 로컬에만 반영                |
| Commit + Update    | Commit + Push     | push 해야 서버 반영                |
| Trunk              | main (or master)  | 기본 브랜치                        |
| Branch             | Branch            | Git 브랜치는 매우 가벼움           |
| Tag                | Tag               | 거의 동일                          |
| Lock               | 없음              | Git은 merge 중심                   |
| Diff               | Diff              | 동일                               |
| Log                | Log               | 동일                               |
| Revert             | Revert / Reset    | 상황에 따라 다름                   |

---

### SVN 과의 차이

| SVN 사고방식     | Git 사고방식            |
| ---------------- | ----------------------- |
| 커밋 = 서버 반영 | 커밋 = 로컬 저장        |
| 서버가 기준      | 로컬이 기준             |
| 브랜치는 무거움  | 브랜치는 포인터, 가벼움 |

---

## 2. Git 저장소 구조

```
Working Directory
        ↓ git add
Staging Area
        ↓ git commit
Local Repository
        ↓ git push
Remote Repository
```

---

## 3. Git 주요 명령어 정리

### 저장소 시작

```bash
git clone <repo-url>
```

### 상태 확인

```bash
git status
git log
git log --oneline
git diff
git diff --staged
```

### 파일 추가 (Staging)

```bash
git add 파일명
git add .
```

### 커밋 (로컬 저장)

```bash
git commit -m "커밋 메시지"
git commit --amend
```

### 원격 저장소와 동기화

```bash
git pull
git pull --rebase
git push
```

### 브랜치 관련

```bash
git branch
git branch 브랜치명
git checkout 브랜치명
git checkout -b 브랜치명
git branch -d 브랜치명
```

### 병합

```bash
git merge 브랜치명
git rebase main
git rebase -i HEAD~N
```

### 충돌 해결 후

```bash
git add .
git rebase --continue
```

### 작업 임시 저장

```bash
git stash
git stash pop
```

### 되돌리기

```bash
git revert <commit>
git reset --hard <commit>
```

### 원격 저장소 정보

```bash
git remote -v
git fetch
```

---

## 4. 최소 사용 명령어 세트

```bash
git clone
git status
git checkout -b
git add .
git commit -m
git pull --rebase
git push
```

---

## 5. Merge의 여러가지 방식

https://hudi.blog/git-merge-squash-rebase/
