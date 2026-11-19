import string

from hypothesis import given, strategies as st
from student_grades import average_marks, parse_srn, short_name


# ---------------------------------------------------------------
# Part 1: robustness - no function may crash on ANY input
# ---------------------------------------------------------------
@given(st.text() | st.none())
def test_average_marks_no_crash(s):
    try:
        average_marks(s)
    except Exception as e:
        assert False, f"average_marks crashed with {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_parse_srn_no_crash(s):
    try:
        parse_srn(s)
    except Exception as e:
        assert False, f"parse_srn crashed with {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_short_name_no_crash(s):
    try:
        short_name(s)
    except Exception as e:
        assert False, f"short_name crashed with {type(e).__name__}: {e}"


# ---------------------------------------------------------------
# Part 2: correctness - properties that must hold for valid input
# ---------------------------------------------------------------
@given(st.lists(st.integers(min_value=0, max_value=100), min_size=1))
def test_average_marks_within_min_and_max(marks):
    result = average_marks(",".join(str(m) for m in marks))
    assert result is not None
    assert min(marks) <= result <= max(marks)


@given(st.one_of(st.integers(max_value=-1), st.integers(min_value=101)))
def test_average_marks_rejects_out_of_range(m):
    assert average_marks(str(m)) is None


valid_srn = st.builds(
    lambda campus, year, dept, roll: f"PES{campus}UG{year:02d}{dept}{roll:03d}",
    st.integers(min_value=0, max_value=9),
    st.integers(min_value=0, max_value=99),
    st.text(alphabet=string.ascii_uppercase, min_size=2, max_size=2),
    st.integers(min_value=0, max_value=999),
)


@given(valid_srn)
def test_parse_srn_valid_roundtrip(srn):
    campus, year, dept = parse_srn(srn)
    assert campus == srn[:4]
    assert year == int(srn[6:8])
    assert dept == srn[8:10]


@given(st.text(alphabet=string.ascii_letters, min_size=1),
       st.text(alphabet=string.ascii_letters, min_size=1))
def test_short_name_format(first, last):
    result = short_name(f"{first} {last}")
    assert result == first[0].upper() + ". " + last.capitalize()


@given(st.text(alphabet=string.ascii_letters, min_size=1))
def test_short_name_rejects_single_word(word):
    assert short_name(word) is None
