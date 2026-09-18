@REM run as Administrator
@echo off

set DOWNLOADS_DIR=%USERPROFILE%\Downloads

@REM set PREFIX=D:\Softwares
set PREFIX=%DOWNLOADS_DIR%

set PYTHON_DIR=%PREFIX%\python-3.13.9-amd64-portable

set PATH=^
%PYTHON_DIR%;^
%PYTHON_DIR%\Scripts;^
%DOWNLOADS_DIR%\PortableGit\bin;^
%DOWNLOADS_DIR%\PortableGit\usr\bin;

@REM export DRJIT_LIBLLVM_PATH='/path/to/libLLVM.so'  # Might be: '/usr/lib/llvm-13/lib/libLLVM.so'
@REM python3 -m jupyterlab .

set DRJIT_LIBLLVM_PATH=%PREFIX%\clang+llvm-23.1.0-x86_64-pc-windows-msvc.tar\clang+llvm-23.1.0-x86_64-pc-windows-msvc\bin\LLVM-C.dll

echo %DRJIT_LIBLLVM_PATH%
python -c "import sys; print(f""Does this python have GIL: {hasattr(sys, '_is_gil_enabled') and sys._is_gil_enabled()}"")"
@REM python -m main
python .\ray-tracing\main_1.py

pause
