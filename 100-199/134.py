"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to
its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.

Constraints:
    gas.length == n
    cost.length == n
    1 <= n <= 10**4
    0 <= gas[i], cost[i] <= 10**4
"""
from typing import List


def can_complete_circuit(gas: List[int], cost: List[int]) -> int:
    station_idx: int = 0
    fuel_tank: int = 0
    total_fuel: int = 0

    for station in range(len(gas)):
        balance: int = gas[station] - cost[station]
        fuel_tank += balance
        total_fuel += balance

        if fuel_tank < 0:
            station_idx = station + 1
            fuel_tank = 0

    return -1 if total_fuel < 0 else station_idx


if __name__ == '__main__':
    assert can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert can_complete_circuit([2, 3, 4], [3, 4, 3]) == -1
