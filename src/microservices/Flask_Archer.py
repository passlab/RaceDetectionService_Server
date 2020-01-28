from subprocess import PIPE, run
# list1 = sys.argv[1]
# print(list1)
# cmd_list = ["clang-archer DRB104-nowait-barrier-orig-no.c -o myApp -larcher","./myApp "]


def archer(file_name):
    print(file_name)
    cmd_list = ["pwd", "ls -l " + file_name]
    for cmd in cmd_list:
        arr = cmd.split()
        result = run(arr, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        if(result.returncode == 1):
            str = result.stderr
        else:
            str = result.stdout
    return str
