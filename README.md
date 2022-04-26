# knapsack
        
    1. Dynamic programming

    # pseudocode
        1.
        C[i][k]: item 1~i且負重k下的最大獲利
        for k = 0 ~ w
            C[0,k] = 0
        for i = 1 ~ n
            C[i,0] = 0
            for k = 1 ~ W
            if(W[i] <= k): #拿得動item i
                if(V[i] + C[i-1,k-w[i]] >= C[i-1,k])
                C[i,k] = V[i]  C[i-1,k-w[i]] #取物品i 用剩下的k-Wi重量 拿1~i-1的item
            else:
                C[i,k] = C[i-1,k] #不取物品i
                else:
                C[i,k] = C[i-1,k] #拿不動item i  

        2.
        is_selects: 各物品是否取的list (從結果倒回來推)
        for item i ~ item 1:
            if C[i][k] == C[i-1][k]
                代表item i不用取
            else
                res - item i價值
                w - item i重量
           
        3. 
        check result is correct or not

    2. Hill climbing

    # pseudocode
  
        def hc(f,x):
          x = 隨意設定一個解
          while(x有鄰居y比x更高):
             x = y
          return x

    # process

        1. 隨機一個重量<=capacity的解
        2. 將此解輸出成01 bitstring, 0:物品有拿 1:物品沒拿

                ex: 10個物品,只有物品3有拿
                bitstring 為 0010000000
        3. 執行500次迭代

               隨機改變一個物品狀態從0->1
               if 重量<=capacity:
                 紀錄是否是最大值
               else:
                 改回來
                 if 所有物品都不能再拿:
                   迭代結束

    3. Simulate climbing

    # pseudocode

        while(T > T_min):
           x = 隨意設定一個取法
           loop:
             任意找一個鄰居y (可能高可能低)
             if y 較高 or random(0,1) < exp(-diff/k*T)
           return max of values

    # process

        1. 隨機一個重量<=capacity的解
        2. 將此解輸出成01 bitstring, 0:物品有拿 1:物品沒拿

                ex: 10個物品,只有物品3有拿
                bitstring 為 0010000000
        3. 溫度下降
                初始溫度: 1000
                最終溫度: 1
                時間衰減率: 0.99
                
                while(溫度還沒下降到指定溫度):
                  隨機改變一個物品狀態從0->1 or 1->0
                  if 新價值較高 or 機率符合條件:
                     允許改變
                     紀錄是否為最大價值
                  溫度下降(t = t*eta)
