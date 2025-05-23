n = int(input("Enter number of exercises: "))
for ex_no in range(n):
    print(f"Operation for ex_{ex_no + 1}")
    for step_no in range(3):
        if step_no == 0:
            print(f"\tstep_{step_no + 1}: create a folder ex_{ex_no + 1}")
        if step_no == 1:
            print(f"\tstep_{step_no + 1}: look at all the files and click on ex_{ex_no + 1}.py")
        if step_no == 2:
            print(f"\tstep_{step_no + 1}: cut ex_{ex_no + 1}.py and paste it to ex_{ex_no + 1} folder")