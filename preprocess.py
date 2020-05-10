def prep_data(df):

    df = df.assign(hw=df["Height"] * df["Width"])

    X = df[["Height", "Width", "hw"]].values
    y = df["Weight"].values

    return X, y