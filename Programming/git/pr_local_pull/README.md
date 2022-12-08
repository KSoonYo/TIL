# github PR을 로컬로 가져오는 방법

`.gitconfig` 전역 설정 파일에 alias로 명령어 커스텀

```
[alias]
  pr  = "!f() { git fetch -fu ${2:-origin} refs/pull/$1/head:pr/$1 && git checkout pr/$1; }; f"
  pr-clean = "!git for-each-ref refs/heads/pr/* --format='%(refname)' | while read ref ; do branch=${ref#refs/heads/} ; git branch -D $branch ; done"
```

```bash
# pr 번호 pull 후 브렌치 변경
git pr [pr 번호] 

# pr 브렌치 clean
git pr-clean [pr 번호]
```



# 참고

https://blog.outsider.ne.kr/1204 (.gitconfig 전역 설정 방법과 .git/config 로컬 저장소 설정 방법 모두 포함)