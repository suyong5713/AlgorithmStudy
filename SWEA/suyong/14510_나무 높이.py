for tc in range(int(input())):
    N = int(input())
    tree_height = list(map(int,input().split()))
    max_height = max(tree_height)
    ans = 0
    odd, even = 0, 0
    # print(tree_height)
    for tree in tree_height:
      if tree == max_height: continue
      even += (max_height - tree) // 2
      odd += (max_height - tree) % 2
    if even == 0 and odd == 0: 
      print("#{} 0".format(tc+1))
      continue
    diff = max(even - odd, 0) // 3
    odd += 2 * diff
    even -= diff
    min_value = min(even,odd)
    ans = (min_value * 2) 
    #홀수 1당 2씩증가. 단, 처음은 1만 증가.
    ans += max((odd - min_value) * 2 - 1, 0)
    #짝수 
    ans += (even - min_value) // 2 * 3
    ans += (even - min_value) % 2 * 2
    print("#{} {}".format(tc+1, ans))