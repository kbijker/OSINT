import os, time
from datetime import datetime

dateTimeObj = datetime.now()


def github():
    print("Files will be pushed to Github.")

    os.system("git remote add origin https://github.com:kbijker/OSINT.git")
    os.system('git config --global user.name "kbijker"')
    os.system('git config --global user.email "k.e.bijker@pl.hanze.nl" ')
    os.system("git config --global --unset proxy.server.com")
    os.system("git config --global --unset http.proxy")
    os.system("git add *")
    os.system("git status")

    comm = f"Update programs by kbijker {dateTimeObj}"
    os.system(f'git commit -m "{comm}"')
    os.system("git push -f origin main")

github()
