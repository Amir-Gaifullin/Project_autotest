import subprocess
#with open(file_path, 'r') as test_file:
usertext = b"1"
#    code_text = test_file.read().strip()
#a = subprocess.run(['/c/Project_autotest/plus_ten.py'],input = "1")
with open("c:/Project_autotest/plus_ten.py", 'r') as test_file:
    stdin1 = test_file.read().strip()
    input_code_bytes = stdin1.encode('utf-8')
    p = subprocess.run(["python"], input = input_code_bytes, stdout = subprocess.PIPE, universal_newlines = True)
#p = subprocess.check_output(["python", "c:/Project_autotest/plus_ten.py"], input=b"3", stderr=subprocess.STDOUT)
    out_str = p.decode('utf-8')
    out = p.out_str.strip()
    print(out)
#
#   p = subprocess.run(usertext, stdin=stdin, stdout=None, stderr=None, shell=False, timeout=None)
#    out, err = p.communicate(usertext)
#    print(stdin)
