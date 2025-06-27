
def fibonacci_loop(n):
    """
    반복문을 사용하여 피보나치 수열을 생성하는 함수입니다.

    Args:
        n: 생성할 피보나치 수열의 길이입니다.

    Returns:
        길이가 n인 피보나치 수열 리스트입니다.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        a, b = 1, 1
        result = [1, 1]
        for _ in range(2, n):
            a, b = b, a + b
            result.append(b)
        return result

print(fibonacci_loop(10))

