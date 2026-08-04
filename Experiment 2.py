def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()  # Convert result to uppercase
    return wrapper


class Report:
    def __init__(self, title):
        self.title = title

    @classmethod
    def from_template(cls, template):
        return cls(template)  # Create object from a template string

    def __str__(self):
        return f"Report Title: {self.title}"

    @uppercase_decorator
    def generate(self):
        return f"This is the report: {self.title}"


# Create object using class method
report = Report.from_template("Annual Sales Report")

# Print object (calls __str__)
print(report)

# Generate report (decorator converts output to uppercase)
print(report.generate())
