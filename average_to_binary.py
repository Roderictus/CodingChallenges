def binary_average(binary):
    val = 0
    lenstr = len(binary)
    for i in range(0,lenstr) :
        if binary[i] == "0":
            pass
        elif binary[i] == "1":
            val = val + 2**(lenstr-i-1)
        elif binary[i] == "x":
            val = val + (2**(lenstr-i-1))/2
    return val



#temp = binary_average("xx")
#temp = binary_average('0')
# binary_average('1')
# binary_average('1x')

#temp = binary_average('x0')
temp = binary_average('xx')
# binary_average('1x0')
# temp =  binary_average('1x0x')
print(temp)
# binary_average('1xxx1xxx0xxx0xxx1xxx1xxx0xxx0xxx1xxx0')


#binary_average('x'), 0.5, .01, "Input 'x'")
#         test.assert_approx_equals(binary_average('0'), 0, .01, "Input '0'")
#         test.assert_approx_equals(binary_average('1'), 1, .01, "Input '1'")
#         test.assert_approx_equals(binary_average('1x'), 2.5, .01, "Input '1x'")
#         test.assert_approx_equals(binary_average('x0'), 2, .01, "Input 'x0'")
#         test.assert_approx_equals(binary_average('xx'), 2.5, .01, "Input 'xx'")
#         test.assert_approx_equals(binary_average('1x0'), 5, .01, "Input '1x0'")
#         test.assert_approx_equals(binary_average('1x0x'), 10.5, .01, "Input '1x0x'")
#         test.assert_approx_equals(binary_average('1xxx1xxx0xxx0xxx1xxx1xxx0xxx0xxx1xxx0'), 105084647303, .01, "Input '1xxx1xxx0xxx0xxx1xxx1xxx0xxx0xxx1xxx0'")