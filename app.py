import streamlit as st

# Calculator class
class Calculator:
    def add(self, a=1, b=1, *args):
        result = a + b
        for num in args:
            result += num
        return result

    def subtraction(self, a=1, b=1, *args):
        result = a - b
        for num in args:
            result -= num
        return result

    def multiply(self, a=1, b=1, *args):
        result = a * b
        for num in args:
            result *= num
        return result

    def divide(self, a=1, b=1, *args):
        if b == 0:
            return "Cannot divide by zero"
        result = a / b
        for num in args:
            if num == 0:
                return "Cannot divide by zero"
            result /= num
        return result


calc = Calculator()

# Streamlit UI
st.title("🧮 Simple Calculator")

operation = st.selectbox(
    "Choose Operation",
    ("Add", "Subtract", "Multiply", "Divide")
)

numbers = st.text_input(
    "Enter numbers separated by comma (example: 10, 5, 2)"
)

if st.button("Calculate"):
    try:
        nums = list(map(float, numbers.split(",")))

        if len(nums) < 2:
            st.warning("Please enter at least two numbers")
        else:
            a, b, *rest = nums

            if operation == "Add":
                result = calc.add(a, b, *rest)

            elif operation == "Subtract":
                result = calc.subtraction(a, b, *rest)

            elif operation == "Multiply":
                result = calc.multiply(a, b, *rest)

            elif operation == "Divide":
                result = calc.divide(a, b, *rest)

            st.success(f"Result: {result}")

    except ValueError:
        st.error("Please enter valid numbers only")
