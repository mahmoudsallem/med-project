# Security Scan Report (Trivy)

**Image:** salem7ouda/backend:v1.0.22
**Scan Date:** 2026-01-04 10:00:47
**Severity Levels:** CRITICAL, HIGH, MEDIUM, LOW

```

Report Summary

┌──────────────────────────────────────────────────────────────────────────────────┬────────────┬─────────────────┬─────────┐
│                                      Target                                      │    Type    │ Vulnerabilities │ Secrets │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ salem7ouda/backend:v1.0.22 (debian 13.2)                                         │   debian   │       61        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/blinker-1.9.0.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/click-8.3.1.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/flask-3.1.2.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/flask_cors-6.0.2.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/itsdangerous-2.2.0.dist-info/METADATA     │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/jinja2-3.1.6.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/markupsafe-3.0.3.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/pip-25.3.dist-info/METADATA               │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/psycopg2_binary-2.9.11.dist-info/METADATA │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/redis-7.1.0.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.13/site-packages/werkzeug-3.1.4.dist-info/METADATA         │ python-pkg │        0        │    -    │
└──────────────────────────────────────────────────────────────────────────────────┴────────────┴─────────────────┴─────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


For OSS Maintainers: VEX Notice
--------------------------------
If you're an OSS maintainer and Trivy has detected vulnerabilities in your project that you believe are not actually exploitable, consider issuing a VEX (Vulnerability Exploitability eXchange) statement.
VEX allows you to communicate the actual status of vulnerabilities in your project, improving security transparency and reducing false positives for your users.
Learn more and start using VEX: https://trivy.dev/docs/v0.68/guide/supply-chain/vex/repo#publishing-vex-documents

To disable this notice, set the TRIVY_DISABLE_VEX_NOTICE environment variable.


salem7ouda/backend:v1.0.22 (debian 13.2)
========================================
Total: 61 (LOW: 51, MEDIUM: 10, HIGH: 0, CRITICAL: 0)

┌────────────────┬─────────────────────┬──────────┬──────────┬─────────────────────────┬───────────────┬──────────────────────────────────────────────────────────────┐
│    Library     │    Vulnerability    │ Severity │  Status  │    Installed Version    │ Fixed Version │                            Title                             │
├────────────────┼─────────────────────┼──────────┼──────────┼─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ apt            │ CVE-2011-3374       │ LOW      │ affected │ 3.0.3                   │               │ It was found that apt-key in apt, all versions, do not       │
│                │                     │          │          │                         │               │ correctly...                                                 │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2011-3374                    │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ bash           │ TEMP-0841856-B18BAF │          │          │ 5.2.37-2+b5             │               │ [Privilege escalation possible to other user than root]      │
│                │                     │          │          │                         │               │ https://security-tracker.debian.org/tracker/TEMP-0841856-B1- │
│                │                     │          │          │                         │               │ 8BAF                                                         │
├────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ bsdutils       │ CVE-2025-14104      │ MEDIUM   │          │ 1:2.41-5                │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ coreutils      │ CVE-2017-18018      │          │          │ 9.7-3                   │               │ coreutils: race condition vulnerability in chown and chgrp   │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2017-18018                   │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2025-5278       │          │          │                         │               │ coreutils: Heap Buffer Under-Read in GNU Coreutils sort via  │
│                │                     │          │          │                         │               │ Key Specification                                            │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-5278                    │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libapt-pkg7.0  │ CVE-2011-3374       │          │          │ 3.0.3                   │               │ It was found that apt-key in apt, all versions, do not       │
│                │                     │          │          │                         │               │ correctly...                                                 │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2011-3374                    │
├────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libblkid1      │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libc-bin       │ CVE-2010-4756       │          │          │ 2.41-12                 │               │ glibc: glob implementation can cause excessive CPU and       │
│                │                     │          │          │                         │               │ memory consumption due to...                                 │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2010-4756                    │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2018-20796      │          │          │                         │               │ glibc: uncontrolled recursion in function                    │
│                │                     │          │          │                         │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20796                   │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2019-1010022    │          │          │                         │               │ glibc: stack guard protection bypass                         │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010022                 │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2019-1010023    │          │          │                         │               │ glibc: running ldd on malicious ELF leads to code execution  │
│                │                     │          │          │                         │               │ because of...                                                │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010023                 │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2019-1010024    │          │          │                         │               │ glibc: ASLR bypass using cache of thread stack and heap      │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010024                 │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2019-1010025    │          │          │                         │               │ glibc: information disclosure of heap addresses of           │
│                │                     │          │          │                         │               │ pthread_created thread                                       │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010025                 │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2019-9192       │          │          │                         │               │ glibc: uncontrolled recursion in function                    │
│                │                     │          │          │                         │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-9192                    │
├────────────────┼─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libc6          │ CVE-2010-4756       │          │          │                         │               │ glibc: glob implementation can cause excessive CPU and       │
│                │                     │          │          │                         │               │ memory consumption due to...                                 │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2010-4756                    │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2018-20796      │          │          │                         │               │ glibc: uncontrolled recursion in function                    │
│                │                     │          │          │                         │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2018-20796                   │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2019-1010022    │          │          │                         │               │ glibc: stack guard protection bypass                         │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010022                 │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2019-1010023    │          │          │                         │               │ glibc: running ldd on malicious ELF leads to code execution  │
│                │                     │          │          │                         │               │ because of...                                                │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010023                 │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2019-1010024    │          │          │                         │               │ glibc: ASLR bypass using cache of thread stack and heap      │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010024                 │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2019-1010025    │          │          │                         │               │ glibc: information disclosure of heap addresses of           │
│                │                     │          │          │                         │               │ pthread_created thread                                       │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-1010025                 │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2019-9192       │          │          │                         │               │ glibc: uncontrolled recursion in function                    │
│                │                     │          │          │                         │               │ check_dst_limits_calc_pos_1 in posix/regexec.c               │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2019-9192                    │
├────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ liblastlog2-2  │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────┼─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│ libmount1      │ CVE-2025-14104      │ MEDIUM   │          │                         │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libncursesw6   │ CVE-2025-6141       │          │          │ 6.5+20250216-2          │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsmartcols1  │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsqlite3-0   │ CVE-2025-7709       │ MEDIUM   │          │ 3.46.1-7                │               │ An integer overflow exists in the FTS5                       │
│                │                     │          │          │                         │               │ https://sqlite.org/fts5.html e ...                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-7709                    │
│                ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2021-45346      │ LOW      │          │                         │               │ sqlite: crafted SQL query allows a malicious user to obtain  │
│                │                     │          │          │                         │               │ sensitive information...                                     │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2021-45346                   │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libsystemd0    │ CVE-2013-4392       │          │          │ 257.9-1~deb13u1         │               │ systemd: TOCTOU race condition when updating file            │
│                │                     │          │          │                         │               │ permissions and SELinux security contexts...                 │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2013-4392                    │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2023-31437      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                │                     │          │          │                         │               │ modify a...                                                  │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31437                   │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2023-31438      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                │                     │          │          │                         │               │ truncate a...                                                │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31438                   │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2023-31439      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                │                     │          │          │                         │               │ modify the...                                                │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31439                   │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libtinfo6      │ CVE-2025-6141       │          │          │ 6.5+20250216-2          │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libudev1       │ CVE-2013-4392       │          │          │ 257.9-1~deb13u1         │               │ systemd: TOCTOU race condition when updating file            │
│                │                     │          │          │                         │               │ permissions and SELinux security contexts...                 │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2013-4392                    │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2023-31437      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                │                     │          │          │                         │               │ modify a...                                                  │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31437                   │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2023-31438      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                │                     │          │          │                         │               │ truncate a...                                                │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31438                   │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2023-31439      │          │          │                         │               │ An issue was discovered in systemd 253. An attacker can      │
│                │                     │          │          │                         │               │ modify the...                                                │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2023-31439                   │
├────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ libuuid1       │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ login          │ CVE-2025-14104      │ MEDIUM   │          │ 1:4.16.0-2+really2.41-5 │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ login.defs     │ CVE-2007-5686       │          │          │ 1:4.17.4-2              │               │ initscripts in rPath Linux 1 sets insecure permissions for   │
│                │                     │          │          │                         │               │ the /var/lo ......                                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2007-5686                    │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2024-56433      │          │          │                         │               │ shadow-utils: Default subordinate ID configuration in        │
│                │                     │          │          │                         │               │ /etc/login.defs could lead to compromise                     │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2024-56433                   │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ TEMP-0628843-DBAD28 │          │          │                         │               │ [more related to CVE-2005-4890]                              │
│                │                     │          │          │                         │               │ https://security-tracker.debian.org/tracker/TEMP-0628843-DB- │
│                │                     │          │          │                         │               │ AD28                                                         │
├────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ mount          │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ ncurses-base   │ CVE-2025-6141       │          │          │ 6.5+20250216-2          │               │ gnu-ncurses: ncurses Stack Buffer Overflow                   │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-6141                    │
├────────────────┤                     │          │          │                         ├───────────────┤                                                              │
│ ncurses-bin    │                     │          │          │                         │               │                                                              │
│                │                     │          │          │                         │               │                                                              │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ passwd         │ CVE-2007-5686       │          │          │ 1:4.17.4-2              │               │ initscripts in rPath Linux 1 sets insecure permissions for   │
│                │                     │          │          │                         │               │ the /var/lo ......                                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2007-5686                    │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2024-56433      │          │          │                         │               │ shadow-utils: Default subordinate ID configuration in        │
│                │                     │          │          │                         │               │ /etc/login.defs could lead to compromise                     │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2024-56433                   │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ TEMP-0628843-DBAD28 │          │          │                         │               │ [more related to CVE-2005-4890]                              │
│                │                     │          │          │                         │               │ https://security-tracker.debian.org/tracker/TEMP-0628843-DB- │
│                │                     │          │          │                         │               │ AD28                                                         │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ perl-base      │ CVE-2011-4116       │          │          │ 5.40.1-6                │               │ perl: File:: Temp insecure temporary file handling           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2011-4116                    │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ sysvinit-utils │ TEMP-0517018-A83CE6 │          │          │ 3.14-4                  │               │ [sysvinit: no-root option in expert installer exposes        │
│                │                     │          │          │                         │               │ locally exploitable security flaw]                           │
│                │                     │          │          │                         │               │ https://security-tracker.debian.org/tracker/TEMP-0517018-A8- │
│                │                     │          │          │                         │               │ 3CE6                                                         │
├────────────────┼─────────────────────┤          │          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ tar            │ CVE-2005-2541       │          │          │ 1.35+dfsg-3.1           │               │ tar: does not properly warn the user when extracting setuid  │
│                │                     │          │          │                         │               │ or setgid...                                                 │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2005-2541                    │
│                ├─────────────────────┤          │          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ TEMP-0290435-0B57B5 │          │          │                         │               │ [tar's rmt command may have undesired side effects]          │
│                │                     │          │          │                         │               │ https://security-tracker.debian.org/tracker/TEMP-0290435-0B- │
│                │                     │          │          │                         │               │ 57B5                                                         │
├────────────────┼─────────────────────┼──────────┤          ├─────────────────────────┼───────────────┼──────────────────────────────────────────────────────────────┤
│ util-linux     │ CVE-2025-14104      │ MEDIUM   │          │ 2.41-5                  │               │ util-linux: util-linux: Heap buffer overread in setpwnam()   │
│                │                     │          │          │                         │               │ when processing 256-byte usernames                           │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2025-14104                   │
│                ├─────────────────────┼──────────┤          │                         ├───────────────┼──────────────────────────────────────────────────────────────┤
│                │ CVE-2022-0563       │ LOW      │          │                         │               │ util-linux: partial disclosure of arbitrary files in chfn    │
│                │                     │          │          │                         │               │ and chsh when compiled...                                    │
│                │                     │          │          │                         │               │ https://avd.aquasec.com/nvd/cve-2022-0563                    │
└────────────────┴─────────────────────┴──────────┴──────────┴─────────────────────────┴───────────────┴──────────────────────────────────────────────────────────────┘
```
