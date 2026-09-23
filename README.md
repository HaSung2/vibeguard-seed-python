# vibeguard-seed-python

VibeGuard 파이프라인 확인용 시드 리포.

- `requirements.txt`에 취약한 버전(`urllib3==1.24.1`)을 일부러 고정했다.
- 테스트 4개는 패치 전에도 전부 통과한다. 버전을 올린 뒤에도 통과해야 "안 깨졌다"가 증명된다.
- lock 파일은 두지 않는다(완전 지원 대상 형태).
