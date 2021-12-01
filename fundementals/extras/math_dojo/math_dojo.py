class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        for i in range(len(nums)):
            self.result += nums[i]
        self.result += num
        return self

    	# your code here
    def subtract(self, num, *nums):
        for i in range(len(nums)):
            self.result -= nums[i]
        self.result -= num
        return self
    	# your code here
# create an instance:
md = MathDojo()
# to test:
# print(md.subtract(3,2).result)
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!

