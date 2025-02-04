import os

repos = ["https://github.com/owais-shafi/Python-_automation_projects.git", 
         "https://github.com/m4milaad/Pyhton-Projects.git",
         "https://github.com/owais-shafi/order-of-north-platform.git"]

paths = ["~/Downloads/Python_projects", 
         "~/Downloads/miladProjects/Pyhton-Projects", 
         "~/Downloads/GeneralProjects/order-of-north-platform"]

if __name__ == "__main__":  
    for i in range(len(repos)):
        repo = repos[i]  
        path = paths[i]  
        
        print(f"\n>>> Pulling changes from repo: '{repo}'")
        os.system(f"git -C {path} pull --no-rebase {repo} main")
        print("\n")
else:
    print(">>> BYE BYE!")

