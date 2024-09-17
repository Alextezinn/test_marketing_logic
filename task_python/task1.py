import pandas as pd
from pathlib import Path


def main():
    path_matrix = Path("../matrix (задача 1).csv")
    matrix = pd.read_csv(path_matrix, header=None)

    print(matrix.shape)
    print(matrix)

    path_source = Path("../source__300 (задача 1).csv")
    source = pd.read_csv(path_source, header=None, delimiter="|")
    print(source.shape)
    print(source)

    df = pd.DataFrame(0, index=range(300), columns=range(300))

    for index, row in source.iterrows():
        id_cell = int(row[0])
        value = int(row[1])
        row_num = (id_cell - 1) // 300
        col_num = (id_cell - 1) % 300
        df.at[row_num, col_num] = value

    print(df.shape)
    print(df)


if __name__ == "__main__":
    main()
