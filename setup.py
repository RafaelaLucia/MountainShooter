from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="LuckyTheShooter",
    version="1.0",
    description="Lucky The Shooter app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables

)