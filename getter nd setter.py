
class disance:
    def __init__(self,a,b):
        self.feet=a
        self.inch=b
    def __add__(self,other):
        final_feet=self.feet+other.feet
        final_inch=self.inch+other.inch
        return disance (final_feet,final_inch)

    def __str__(self):
        return "distance is"+str(self.feet)+"feet"+str(self.inch)+"inch"
