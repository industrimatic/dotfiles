import subprocess

project_name = "test"
linkers = ["cmsis-dap", "stlink", "jlink"]
mcus = ["stm32f1x", "stm32f4x"]

subprocess.run(
    [
        "openocd",
        "-f",
        f"interface/{linkers[0]}.cfg",
        "-f",
        f"target/{mcus[0]}.cfg",
        "-c",
        f"program ./build/Debug/{project_name}.elf verify reset exit",
    ]
)
