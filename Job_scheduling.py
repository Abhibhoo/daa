def printJobScheduling(arr, t):
    n = len(arr)
    print("Following is the job scheduling for the given time intervals:")
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    job = ['-1'] * t
    slots = [False] * t

    for i in range(len(arr)):
        # Find a slot for this job
        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
            if not slots[j]:  # If the slot is free
                slots[j] = True
                job[j] = arr[i][0]
                break

    print("Job sequence:", job)

if __name__ == "__main__":
    n = int(input("Enter the number of jobs: "))
    arr = []
    
    for i in range(n):
        job_id = input(f"Enter job ID for job {i + 1}: ")
        deadline = int(input(f"Enter deadline for job {i + 1}: "))
        profit = int(input(f"Enter profit for job {i + 1}: "))
        arr.append([job_id, deadline, profit])

    t = int(input("Enter the number of time slots: "))

    print("Following is the maximum profit sequence of jobs:")
    printJobScheduling(arr, t)
