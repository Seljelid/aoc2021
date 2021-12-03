from collections import Counter, defaultdict


def power_consumption():
    with open("data/3.csv") as f:
        lines = f.readlines()
        input = [line.strip() for line in lines]

    transposed_codes = _get_transposed_codes(input)

    gamma_rate = ""
    epsilon_rate = ""
    for _, code in transposed_codes.items():
        gamma_rate += _common(code, most=True)
        epsilon_rate += _common(code, most=False)

    gamma_rate_int = int(gamma_rate, 2)
    epsilon_rate_int = int(epsilon_rate, 2)
    print(f"Star 1: {gamma_rate_int * epsilon_rate_int}")

    # Star 2
    oxygen_generator_rating = int(_get_rating_code(input, 0, most=True), 2)
    co2_scrubber_rating = int(_get_rating_code(input, 0, most=False), 2)
    print(f"Star2 : {oxygen_generator_rating * co2_scrubber_rating}")


def _get_rating_code(codes, idx, most=True):
    while len(codes) > 1:
        transposed_codes = _get_transposed_codes(codes)
        keep = _common(transposed_codes[idx], most=most)
        codes = [code for code in codes if code[idx] == keep]
        idx += 1
        _get_rating_code(codes, idx, most=most)
    return codes[0]


def _get_transposed_codes(codes):
    transposed_codes = defaultdict(list)
    for code in codes:
        for idx, bit in enumerate(code):
            transposed_codes[idx].append(bit)
    return transposed_codes


def _common(code, most=True):
    cnt = Counter(code)
    if most:
        if cnt.most_common()[0][1] == cnt.most_common()[-1][1]:
            return "1"
        try:
            return cnt.most_common()[0][0]
        except:
            breakpoint()
    else:
        if cnt.most_common()[0][1] == cnt.most_common()[-1][1]:
            return "0"
        return cnt.most_common()[-1][0]


if __name__ == "__main__":
    power_consumption()
