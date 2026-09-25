"""Celsius    Fahrenheit
0          32.0
10         50.0
20         68.0
30         86.0
40         104.0
50         122.0
60         140.0
70         158.0
80         176.0
90         194.0
100        212.0"""

print(f"{'Celsius':<10} {'Fahrenheit'}")


for celsius in range(0, 101, 10):
   
    fahrenheit = celsius * 9 / 5 + 32
    
   
    print(f"{celsius:<10} {fahrenheit:.1f}")
