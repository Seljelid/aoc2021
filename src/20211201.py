import pandas as pd


def depth():
    df = pd.read_csv("data/1.csv", names=["depth"])
    df["prev_depth"] = df["depth"].shift()
    n_deeper = sum(df["depth"] > df["prev_depth"])
    print(f"Star 1: {n_deeper}")

    # Star 2
    df["triag"] = df["depth"].rolling(window=3).sum()
    df["prev_triag"] = df["triag"].shift()
    n_deeper = sum(df["triag"] > df["prev_triag"])
    print(f"Star 2: {n_deeper}")


if __name__ == "__main__":
    depth()
