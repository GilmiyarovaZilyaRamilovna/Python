sep = ')('
res_lis = []
while True:
    row = input('-> ')
    if not sep in row:
        break
    nums = [ int(x) for x in row.split(sep) ]
    last_dig = nums[-1]%10
    get_des  = lambda x: x%100//10
    des      = get_des( nums[0] )
    nums.pop()
    nums.pop(0)
    res = [ x for x in nums if x%last_dig == 0 and get_des(x) > des ]
    res_lis.append(res)
[ print(*x) for x in res_lis ]