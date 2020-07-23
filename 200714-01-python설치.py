#e
> python 3.7.8 설치
> 소스 https://www.python.org/ftp/python/3.7.8/Python-3.7.8.tgz
> 환경 SunOS 5.10 sun4v sparc SUNW
> bash-3.00$ /usr/sfw/bin/gcc --version /// gcc (GCC) 3.4.3 
#e

# /usr/include/iso/math_c99.h 수정 후 설치 됨

ln -s /usr/sfw/bin/gar /usr/sfw/bin/ar
PATH=/usr/sfw/bin:$PATH
./configure --prefix=/opt/python3
make
make test
make install
unlink /usr/sfw/bin/ar

-------설치 중 발생했던 에러
===컴파일 중 에러
Objects/floatobject.c:790: error: invalid operands to binary ==
Objects/floatobject.c:790: error: wrong type argument to unary minus

complexobject.c  complexobject   Py_NAN, HUGE_VAL 문제 발생

-D"Py_HUGE_VAL=HUGE_VAL()"  추가 후 진행 <-- 링크에서 문제가 발생 의미 없었음.
 
=== 링크 중 에러
gcc      -o python Programs/python.o libpython3.7m.a -lsocket -lnsl -lintl -lrt -ldl -lsendfile   -lm  
Undefined                       first referenced
 symbol                             in file
__builtin_isnan                     libpython3.7m.a(floatobject.o)
ld: fatal: Symbol referencing errors. No output written to python
collect2: ld returned 1 exit status



https://gcc.gnu.org/bugzilla/show_bug.cgi?id=19933
---sun gcc 환경에 뭔가 문제가 있다고 판단 함

/usr/include/iso/math_c99.h 수정

------------ org
#if defined(_STDC_C99) || _XOPEN_SOURCE - 0 >= 600 || defined(__C99FEATURES__)
#undef  HUGE_VAL
#define HUGE_VAL        __builtin_huge_val
#undef  HUGE_VALF
#define HUGE_VALF       __builtin_huge_valf
#undef  HUGE_VALL
#define HUGE_VALL       __builtin_huge_vall
#undef  INFINITY
#define INFINITY        __builtin_infinity
#undef  NAN
#define NAN             __builtin_nan


------------ 수정
#if defined(_STDC_C99) || _XOPEN_SOURCE - 0 >= 600 || defined(__C99FEATURES__)
#undef  HUGE_VAL
#define HUGE_VAL        __builtin_huge_val() 
#undef  HUGE_VALF
#define HUGE_VALF       __builtin_huge_valf
#undef  HUGE_VALL
#define HUGE_VALL       __builtin_huge_vall
#undef  INFINITY
#define INFINITY        __builtin_infinity
#undef  NAN
#define NAN             __builtin_isnan()


https://community.oracle.com/thread/4277048?start=0&tstart=0
https://it.toolbox.com/question/installing-python-on-solaris-011809
https://github.com/redis/redis/issues/1120


------------- 설치 후 시험
# ./python3
Python 3.7.8 (default, Jul 14 2020, 13:37:01) 
[GCC 3.4.3 (csl-sol210-3_4-branch+sol_rpath)] on sunos5
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.version
'3.7.8 (default, Jul 14 2020, 13:37:01) \n[GCC 3.4.3 (csl-sol210-3_4-branch+sol_rpath)]'


------------ 동작이 잘 되려나 모르겠네요.
369 tests OK.

21 tests failed:
    test_asyncio test_builtin test_concurrent_futures
    test_configparser test_difflib test_dtrace test_float test_format
    test_fstring test_hashlib test_openpty test_optparse test_os
    test_posix test_socket test_stat test_statistics test_time
    test_types test_unicode test_urllib2net

26 tests skipped:
    test_ctypes test_dbm_gnu test_epoll test_gdb test_idle test_ioctl
    test_kqueue test_lzma test_msilib test_ossaudiodev test_readline
    test_smtpnet test_sqlite test_ssl test_startfile test_strtod
    test_tcl test_tix test_tk test_ttk_guionly test_ttk_textonly
    test_turtle test_winconsoleio test_winreg test_winsound
    test_zipfile64

========= 


