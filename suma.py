def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]


    #
    # @test.it("Sample tests")
    # def sample_tests():
    #     test.assert_equals(sorted(two_sum([1 ,2 ,3], 4)), [0 ,2])
    #     test.assert_equals(sorted(two_sum([1234 ,5678 ,9012], 14690)), [1 ,2])
    #     test.assert_equals(sorted(two_sum([2 ,2 ,3], 4)), [0 ,1])