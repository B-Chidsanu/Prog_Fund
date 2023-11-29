class Car:
    def __init__(self, license, brand, color):
        self.license = license
        self.brand = brand
        self.color = color
        self.report = []

    def __str__(self):
        return f"{self.license}-{self.brand}{self.color}"

    def __lt__(self,  rhs):
        return self.license < rhs.license

    def add_report(self, new_report):
        self.report.append(new_report)

    def total_payment(self):
        total = 0
        for payment in self.report:
            total += payment[2]
        return total

    def max_payment(self):
        if len(self.report) <= 0:
            return self.report
        else:
            for max in range(0, len(self.report)):
                if max + 2 > len(self.report):
                    break
                elif (self.report[max][2]) < (self.report[max+1][2]):
                    compare = self.report[max+1]
                elif (self.report[max][2]) > (self.report[max+1][2]):
                    compare = self.report[max]
            return compare


c = Car('AA1234', 'Honda', 'White')
c1 = Car('AA1234', 'BMW', 'Black')
print(c)
c.add_report(('20 May 2017', 'chang tires', 1500))
c.add_report(('23 May 2017', 'chang tires', 3000))
c.add_report(('25 May 2017', 'chang tires', 4500))
c.add_report(('26 May 2017', 'chang tires', 5500))
print(c < c1)
print(c.report)
print(c.total_payment())
print(c.max_payment())
