class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
    int l = gas.length;
    int allTankTotal = 0,currT = 0, initialStation = 0;
    for (int i = 0; i < l; i++) {
        allTankTotal = allTankTotal + (gas[i] - cost[i]);
        currT = currT + (gas[i] - cost[i]);
        if (currT < 0) {
            currT = 0;
            initialStation = i + 1;
        }
    }
    return allTankTotal >= 0 ? initialStation : -1;
}
}