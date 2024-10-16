def is_pronic(n: int) -> bool:
    for i in range(n):
        if i * (i + 1) == n:
            return True
    return False


def main() -> None:
    print(is_pronic(6))
    print(is_pronic(7))


if __name__ == '__main__':
    main()

# isPronic(6) => true, isPronic(7) => false
