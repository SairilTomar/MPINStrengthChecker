# mpin.py

def commonly_used_mpin4():
    common = set()

    for d in range(10):
        common.add(str(d) * 4)

    for start in range(0, 10):
        seq = "".join(str((start + i) % 10) for i in range(4))
        common.add(seq)

    for start in range(9, 2, -1):
        seq = "".join(str((start - i) % 10) for i in range(4))
        common.add(seq)

    for a in range(10):
        for b in range(10):
            if a != b:
                common.add(f"{a}{a}{b}{b}")
                common.add(f"{a}{b}{a}{b}")
                common.add(f"{b}{a}{b}{a}")
                common.add(f"{a}{b}{b}{a}")

    return sorted(common)


def commonly_used_mpin6():
    common = set()

    for d in range(10):
        common.add(str(d) * 6)

    for start in range(0, 10):
        seq = "".join(str((start + i) % 10) for i in range(6))
        common.add(seq)

    for start in range(9, 4, -1):
        seq = "".join(str(start - i) for i in range(6))
        common.add(seq)

    for a in range(10):
        for b in range(10):
            if a != b:
                common.add(f"{a}{a}{b}{b}{a}{a}")
                common.add(f"{a}{b}{a}{b}{a}{b}")
                common.add(f"{a}{b}{b}{a}{a}{b}")

    return sorted(common)


COMMON_MPINS_4 = commonly_used_mpin4()
COMMON_MPINS_6 = commonly_used_mpin6()


def is_common_mpin(mpin):
    if len(mpin) == 4:
        return mpin in COMMON_MPINS_4
    elif len(mpin) == 6:
        return mpin in COMMON_MPINS_6
    else:
        return False


def all_possible_dates(date_string):
    variants = set()

    if len(date_string) == 6:
        dd = date_string[0:2]
        mm = date_string[2:4]
        yy = date_string[4:6]

        variants.update([
            dd + mm, mm + dd, yy + mm, mm + yy, dd + yy, yy + dd,
            dd + mm + yy, yy + mm + dd, mm + dd + yy
        ])

    elif len(date_string) == 4:
        dd = date_string[0:2]
        mm = date_string[2:4]
        variants.update([dd + mm, mm + dd])

    return variants


def check_demographic(mpin, dates):
    reasons = []

    for key, date_str in dates.items():
        if date_str:
            variants = all_possible_dates(date_str)
            if mpin in variants:
                if key == 'DOB_SELF':
                    reasons.append("Your MPIN matches your own birth date.")
                elif key == 'DOB_SPOUSE':
                    reasons.append("Your MPIN is similar to your spouse’s birth date.")
                elif key == 'ANNIVERSARY':
                    reasons.append("Your MPIN matches your anniversary date.")

    return reasons


def check_mpin(mpin, dates):
    reasons = []

    if is_common_mpin(mpin):
        reasons.append("MPIN is too common or predictable.")

    reasons.extend(check_demographic(mpin, dates))

    if reasons:
        return "Weak MPIN:\n- " + "\n- ".join(reasons)
    else:
        return "Strong MPIN."
