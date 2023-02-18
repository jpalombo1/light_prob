import math
import time


def switch_states(switches: int) -> list[int]:
    """Find switch states for switches switches after switches iterations. Return switches that are on."""
    switch_states_arr: list[bool] = [False] * switches
    for idx in range(1, switches + 1):
        multiple = 1
        while True:
            idx_next = idx * multiple
            if idx_next > switches:
                break
            switch_states_arr[idx_next - 1] = not switch_states_arr[idx_next - 1]
            multiple += 1
        # print(f"Num: {idx}, On switches {switches_on(switch_states_arr)}")

    return switches_on(switch_states_arr)


def switches_on(switch_states_arr: list[bool]) -> list[int]:
    """Given switch state array of on/off, return array of numbered switches on based on index."""
    return [idx + 1 for idx, state in enumerate(switch_states_arr) if state]


def prime_factors(number: int) -> list[int]:
    """Recursive function to find prime factors of number.

    Number has factor when int(number/num) * factor = num so exact divide.
    Get next factors of larger number factor recursively using same function, until that larger factor has no more factors except [1, itself]
    """
    for num in range(2, int(math.sqrt(number)) + 1):
        factor = int(number / num)
        if factor * num == number:
            next_factors = prime_factors(factor)
            return [num] + next_factors
    return [1, number]


def num_factors(number: int) -> int:
    """Number of unique factors for number. Get prime factors, then counts of each prime factor for power.

    Finally number of factors for n = p1^c1k * p2^c2k... = (c1+1)(c2+1)...  or prime power + 1 multiply together.
    """
    counts = {}
    factors = prime_factors(number)
    # print(f"Prime factorization: {factors}")
    for factor in set(factors):
        if factor == 1:
            continue
        counts[factor] = factors.count(factor) + 1
    # print(f"Number of each prime {counts}")
    num_factors = 1
    for num in counts.values():
        num_factors *= num
    return num_factors


def will_switch(number: int) -> int:
    """Determine if switch on or off by end by number of factors. If even  will be off, if odd will be on."""
    return num_factors(number) % 2 != 0


def proof_switch(switches: int) -> list[int]:
    """Using prime factors, check for every number, which will stay switched on."""
    switch_states_arr = [will_switch(num) for num in range(1, switches + 1)]
    return switches_on(switch_states_arr)


def print_building(number: int, on_switches: list[int]) -> str:
    """Show building. Make nxn grid where n is or 1 above sqrt of switches. All padded by 3.

    Row number getten by dim * row_num + col_num+1 sicne start at 1.
    """
    cols_max = 16
    num_cols = int(math.sqrt(number))
    if num_cols > cols_max:
        num_cols = cols_max
    approx_rows = number / num_cols
    num_rows = (
        int(approx_rows) if approx_rows == int(approx_rows) else int(approx_rows) + 1
    )
    for row in range(num_rows):
        print(
            "| ".join(
                [
                    f"{row * num_cols + (col + 1):<5}"
                    if row * num_cols + (col + 1) in on_switches
                    else f"{'':<5}"
                    for col in range(num_cols)
                ]
            )
        )
    print(f"Rows: {num_rows}, Cols: {num_cols}")


def main():
    """Main."""
    SWITCHES: int = 1000
    t0 = time.perf_counter()
    experiment = switch_states(SWITCHES)
    t1e = time.perf_counter() - t0
    t0 = time.perf_counter()
    theory = proof_switch(SWITCHES)
    t1t = time.perf_counter() - t0
    print_building(SWITCHES, theory)
    print(f"Experimental {experiment}")
    print(f"Time Exec: {t1e} s")
    print(f"Theoretical: {theory}")
    print(f"Time Exec: {t1t} s")


if __name__ == "__main__":
    main()
