import re

# Valid SRN format, e.g. PES1UG23CS123
#   PES + campus digit + UG + 2-digit year + 2-letter dept + 3-digit roll no.
SRN_PATTERN = re.compile(r"PES[0-9]UG([0-9]{2})([A-Z]{2})[0-9]{3}")


def average_marks(marks_csv):
    """Return the average of comma-separated marks (0-100), rounded to 2 places.

    Returns None for invalid input (non-string, empty, non-numeric,
    empty elements, or marks outside 0-100).
    """
    if not isinstance(marks_csv, str):
        return None

    marks = []
    for part in marks_csv.split(','):
        part = part.strip()
        # Only plain ASCII digits; max 3 chars also avoids huge-int conversion errors
        if not re.fullmatch(r"[0-9]{1,3}", part):
            return None
        value = int(part)
        if not 0 <= value <= 100:
            return None
        marks.append(value)

    # marks is never empty here, so no ZeroDivisionError
    return round(sum(marks) / len(marks), 2)


def parse_srn(srn):
    """Return (campus, year, dept) from an SRN like PES1UG23CS123.

    Returns None for invalid input.
    """
    if not isinstance(srn, str):
        return None

    srn = srn.strip().upper()
    match = SRN_PATTERN.fullmatch(srn)
    if match is None:
        return None

    return srn[:4], int(match.group(1)), match.group(2)


def short_name(full_name):
    """Return 'R. Kumar' for 'ravi kumar'.

    With more than two words, uses the first and last word.
    Returns None for invalid input (non-string, or fewer than two words).
    """
    if not isinstance(full_name, str):
        return None

    parts = full_name.split()
    if len(parts) < 2:
        return None

    first, last = parts[0], parts[-1]
    return first[0].upper() + ". " + last.capitalize()


def main():
    print("==== Running average_marks ====")
    user_input = input("Enter marks as CSV (e.g. 78,85,92): ")
    result = average_marks(user_input)
    if result is None:
        print("Invalid input: enter whole-number marks between 0 and 100, separated by commas.")
    else:
        print("Average Marks:", result)

    print("\n==== Running parse_srn ====")
    user_input = input("Enter an SRN (e.g. PES1UG23CS123): ")
    result = parse_srn(user_input)
    if result is None:
        print("Invalid SRN: expected a format like PES1UG23CS123.")
    else:
        print("Campus, Year and Dept:", result)

    print("\n==== Running short_name ====")
    user_input = input("Enter first and last name (e.g. ravi kumar): ")
    result = short_name(user_input)
    if result is None:
        print("Invalid name: enter at least a first and a last name.")
    else:
        print("Short Name:", result)


if __name__ == "__main__":
    main()