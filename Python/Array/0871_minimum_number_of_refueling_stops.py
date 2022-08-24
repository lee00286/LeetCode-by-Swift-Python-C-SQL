class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        Testcases:
        1, 1, []
        100, 1, [[10, 100]]
        100, 10, [[10,60],[20,30],[30,30],[60,40]]
        1000000000, 145267354, [[5510987,84329695],[10682248,76273791],[56227783,136858069],[91710087,18854476],[111148380,127134059],[165982642,122930004],[184216180,124802819],[217578071,7123113],[233719001,95862544],[339631786,7676497],[349762649,136128214],[403119403,21487501],[423890164,61095325],[424072629,50415446],[572994480,13561367],[609623597,69207102],[662818314,84432133],[678679727,20403175],[682325369,14288077],[702137485,6426204],[716318901,47662322],[738137702,129579140],[761962118,23765733],[820353983,70497719],[895811889,75533360]]
        """
        
        # Can reach the target without refueling
        if (target <= startFuel):
            return 0
        
        # Otherwise, need to refuel at least once
        if (len(stations) == 0):
            return -1
        
        """
        100, 10, [[10,60],[20,30],[30,30],[60,40]]
        dp = [10] + [0] * 4 = [10] + [0, 0, 0, 0] = [10, 0, 0, 0, 0]
        i = 0, position = 10, fuel = 60
            t = 0
                dp[0] = 10 >= position = 10
                    dp[1] = max(dp[1] = 0, dp[0] + 60 = 70) = 70
        dp = [10, 70, 0, 0, 0]
        i = 1, position = 20, fuel = 30
            t = 1
                dp[1] = 70 > position = 20
                    dp[2] = max(dp[2] = 0, dp[1] + 30 = 90) = 90
            t = 0
                dp[0] = 10 < position = 20
        dp = [10, 70, 90, 0, 0]
        i = 2, position = 30, fuel = 30
            t = 2
                dp[2] = 90 > position = 30
                    dp[3] = max(dp[3] = 0, dp[2] + 30 = 120) = 120
            t = 1
                dp[1] = 70 > position = 30
                    dp[2] = max(dp[2] = 90, dp[1] + 30 = 100) = 100
            t = 0
                dp[0] = 10 < position = 30
        dp = [10, 70, 100, 120, 0]
        i = 3, position = 60, fuel = 40
            t = 3
                dp[3] = 120 > position = 60
                    dp[4] = max(dp[4] = 0, dp[3] + 40 = 160) = 160
            t = 2
                dp[2] = 100 > position = 60
                    dp[3] = max(dp[3] = 120, dp[2] + 40 = 140) = 140
            t = 1
                dp[1] = 70 > position = 60
                    dp[2] = max(dp[2] = 100, dp[1] + 40 = 110) = 110
            t = 0
                dp[0] = 10 < position = 60
        dp = [10, 70, 110, 140, 160]
        
        i = 0, d = 10
            d = 10 < target = 100
        i = 1, d = 70
            d = 70 < target = 100
        i = 2, d = 110
            d = 110 > target = 100
                return 2
        """
        
        # ========= Dynamic Programming
        dp = [startFuel] + [0] * len(stations)
        for i, (position, fuel) in enumerate(stations):
            # Stop and refuel t times
            for t in range(i, -1, -1):
                # If fuel is enough to the next station
                if dp[t] >= position:
                    # Maximum fuel that can be refueled visiting t-th station
                    dp[t + 1] = max(dp[t + 1], dp[t] + fuel)
        # Minmum number of refueling stops
        for i, d in enumerate(dp):
            if d >= target:
                return i
        return -1
        
        """
        # ========= DFS
        minRefuelStops = -1
        for i in range(len(stations)):
            position = stations[i][0]
            fuel = stations[i][1]
            if (position > startFuel):
                break
            if (i + 1 < len(stations)):
                refuelStops = self.minRefuelStops(target, startFuel + fuel, stations[i + 1:])
                if (refuelStops >= 0):
                    if (refuelStops == 0):
                        return 1
                    elif (minRefuelStops < 0 or minRefuelStops > refuelStops + 1):
                        minRefuelStops = refuelStops + 1
            elif (target <= startFuel + fuel):
                return 1
        return minRefuelStops
        """
