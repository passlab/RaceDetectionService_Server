from subprocess import PIPE, run
# list1 = sys.argv[1]
# print(list1)
# list2 = sys.argv[2]
# print(list2)
def tsan(file_name):
    cmd_list = ["pwd", "ls -l " + file_name]
    for cmd in cmd_list:
        arr = cmd.split()
        result = run(arr, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        if(result.returncode == 1):
            str = result.stderr
        else:
            str = result.stdout
    return str