import pytest
from student_grades import letter_grade, final_marks, exam_eligibility


# ---------- letter_grade: every grade boundary ----------
@pytest.mark.parametrize("marks, expected", [
    (100, "S"), (90, "S"),
    (89, "A"), (80, "A"),
    (79, "B"), (70, "B"),
    (69, "C"), (60, "C"),
    (59, "D"), (50, "D"),
    (49, "E"), (40, "E"),
    (39, "F"), (0, "F"),
])
def test_letter_grade_boundaries(marks, expected):
    assert letter_grade(marks) == expected


@pytest.mark.parametrize("marks", [-1, 101])
def test_letter_grade_invalid_both_sides(marks):
    with pytest.raises(ValueError):
        letter_grade(marks)


# ---------- final_marks: both sides of each decision ----------
@pytest.mark.parametrize("internal, external, project, expected", [
    (40, 60, False, 100),   # max marks, no project
    (30, 50, False, 80),    # no project branch
    (30, 50, True, 85),     # project bonus, no cap needed
    (35, 60, True, 100),    # lands exactly on 100, not capped
    (40, 60, True, 100),    # 105 gets capped to 100
])
def test_final_marks_valid(internal, external, project, expected):
    assert final_marks(internal, external, project) == expected


@pytest.mark.parametrize("internal, external", [(41, 0), (0, 61)])
def test_final_marks_out_of_range(internal, external):
    with pytest.raises(ValueError):
        final_marks(internal, external, False)


# ---------- exam_eligibility: every path ----------
@pytest.mark.parametrize("attendance, fees, medical, expected", [
    (100, False, True, "blocked"),    # fees unpaid always blocks
    (0, False, False, "blocked"),
    (75, True, False, "eligible"),    # exactly at 75
    (74, True, False, "detained"),    # just below 75, no medical
    (74, True, True, "eligible"),     # medical rescues it
    (65, True, True, "eligible"),     # exactly at 65 with medical
    (64, True, True, "detained"),     # just below 65, even with medical
    (65, True, False, "detained"),    # 65 but no medical
])
def test_exam_eligibility(attendance, fees, medical, expected):
    assert exam_eligibility(attendance, fees, medical) == expected