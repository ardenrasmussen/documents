def main():
    nums = [1, 1]
    while nums[-1] < 1000:
        nums.append(nums[-2] + nums[-1])
    nums = nums[:-1]
    print(nums)

if __name__ == "__main__":
    main()
