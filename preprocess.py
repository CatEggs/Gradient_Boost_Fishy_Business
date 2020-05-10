def prep_data(df):

    X = df[["Length1", "Length2", "Length3", "Height", "Width"]].values
    y = df["Weight"].values

    return X, y
