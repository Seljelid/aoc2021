import pandas as pd


def horizontal_position():
    df = pd.read_csv("data/2.csv", sep=" ", names=["dir", "steps"])
    x_pos = df[df["dir"] == "forward"]["steps"].sum()
    y_pos = (
        df[df["dir"] == "down"]["steps"].sum() - df[df["dir"] == "up"]["steps"].sum()
    )
    print(f"Star 1: {x_pos * y_pos}")

    # Star 2
    x_pos = 0
    y_pos = 0
    aim = 0
    for _, row in df.iterrows():
        action = row["dir"]
        steps = row["steps"]
        if action == "down":
            aim += steps
        elif action == "up":
            aim -= steps
        elif action == "forward":
            x_pos += steps
            y_pos += aim * steps

    print(f"Star 2: {x_pos * y_pos}")


if __name__ == "__main__":
    horizontal_position()
