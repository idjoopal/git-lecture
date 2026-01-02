📘 기본 개념 대응
| SVN 용어             | Git에서의 개념         | 설명                               |
| ------------------ | ----------------- | -------------------------------- |
| Repository         | Repository        | 저장소 (개념은 동일)                     |
| Central Repository | Remote Repository | Git에서는 서버는 “공유용”                 |
| Working Copy       | Working Directory | 작업 중인 파일들                        |
| Revision           | Commit            | Git은 revision 번호가 아닌 hash        |
| Checkout           | Clone / Checkout  | clone = 최초 복사, checkout = 브랜치 이동 |
| Update             | Pull              | 최신 변경사항 가져오기                     |
| Commit             | Commit            | Git은 **로컬에만** 반영                 |
| Commit + Update    | Commit + Push     | push를 해야 서버 반영                   |
| Trunk              | main (or master)  | 기본 브랜치                           |
| Branch             | Branch            | Git 브랜치는 매우 가벼움                  |
| Tag                | Tag               | 개념 거의 동일                         |
| Lock               | (거의 없음)           | Git은 lock보다 merge 중심             |
| Diff               | Diff              | 거의 동일                            |
| Log                | Log               | 거의 동일                            |
| Revert             | Revert / Reset    | Git은 경우에 따라 다름                   |

⚠️ SVN 사용자들이 헷갈리는 포인트
| SVN 사고방식       | Git 사고방식     |
| -------------- | ------------ |
| 커밋 = 서버 반영     | 커밋 = 로컬 저장   |
| 서버가 기준         | 로컬이 기준       |
| 브랜치는 무거움       | 브랜치는 그냥 포인터  |
| update 안 하면 위험 | pull 안 하면 위험 |

2️⃣ Git 저장소 구조 (개념 정리)
[Working Directory]
        ↓ git add
[Staging Area]
        ↓ git commit
[Local Repository]
        ↓ git push
[Remote Repository]
SVN에는 Staging Area 개념이 없음

Git은 항상 add → commit 단계가 있음

3️⃣ Git 주요 명령어 전체 정리
🔹 저장소 시작
git clone <repo-url>
SVN의 checkout 역할
원격 저장소를 로컬로 복사

🔹 상태 확인
git status
수정된 파일
add 여부
현재 브랜치 확인

git log
git log --oneline
커밋 히스토리 확인

git diff
git diff --staged
변경 내용 비교

🔹 파일 추가 (SVN에는 없는 단계)
git add 파일명
git add .
커밋할 파일을 “선택”하는 단계

🔹 커밋 (로컬에만 반영됨)
git commit -m "커밋 메시지"

git commit --amend
직전 커밋 수정 (메시지/파일)

🔹 원격 저장소와 동기화
git pull
원격 변경사항 가져오기 (fetch + merge)

git pull --rebase
히스토리를 깔끔하게 유지 (권장)

git push
로컬 커밋을 서버에 반영

🔹 브랜치 관련 (Git 핵심)
git branch
브랜치 목록 확인

git branch 브랜치명
브랜치 생성

git checkout 브랜치명
브랜치 이동

git checkout -b 브랜치명
생성 + 이동 동시에

git branch -d 브랜치명
브랜치 삭제

🔹 병합 (merge / rebase)
git merge 브랜치명
브랜치 병합 (merge commit 생성 가능)

git rebase main
기준 브랜치 위로 다시 쌓기

git rebase -i HEAD~N
커밋 정리 (squash, reword 등)

🔹 충돌 해결 후
git add .
git rebase --continue

또는 merge 중이면:
git commit

🔹 작업 임시 저장 (stash)
git stash

git stash pop
작업 중이던 변경사항 임시 보관

🔹 되돌리기 (주의해서 사용)
git revert <commit>

안전하게 되돌림 (추천)
git reset --hard <commit>
히스토리 자체를 되돌림 (주의!)

🔹 원격 저장소 정보
git remote -v
git fetch

변경사항만 가져오고 병합은 안 함


4️⃣ SVN 사용자 기준 “이렇게만 쓰면 됨” 최소 세트
git clone
git status
git checkout -b
git add .
git commit -m
git pull --rebase
git push
