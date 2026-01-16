import os


def add(num1, num2):
    return num1 + num2


def substraction(num1, num2):
    return num1 - num2


def divide(num1, num2):
    if num2 == 0:
        raise ValueError("can't divide by 0")
    return num1 / num2


def secure_add(num1, num2):
    token = os.getenv("TOKEN")

    if token != "ALLOW":
        raise PermissionError("Missing/Invalid token")
    return num1 + num2
