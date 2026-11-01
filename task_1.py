def total_salary(path: str) -> tuple[int, float]:
    """
    Calculate the total and average salaries from a text file.

    Each non-empty line must contain a developer's name and salary,
    separated by a comma.

    Args:
        path (str): Path to the UTF-8 encoded salary file.

    Returns:
        tuple[int, float]: Total and average salary.
            Returns (0, 0.0) if the file is empty or an error occurs.
    """
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) != 2 or not parts[0].strip():
                    raise ValueError("Invalid file format.")

                salary = int(parts[1].strip())

                if salary < 0:
                    raise ValueError("Salary cannot be negative.")

                total += salary
                count += 1

    except OSError as error:
        print(f"Error reading salary file: {error}")
        return (0, 0.0)

    except (ValueError, UnicodeError) as error:
        print(f"Error: Invalid salary file data. {error}")
        return (0, 0.0)

    average = total / count if count > 0 else 0.0

    return (total, average)
