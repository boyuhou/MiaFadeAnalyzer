import pandas as pd


@pd.api.extensions.register_dataframe_accessor("mia")
class Mia:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._df = pandas_obj

    @staticmethod
    def _validate(obj: pd.DataFrame):
        """Validate the pandas dataframe to ensure it has the right column etc.

        Args:
            obj: pandas dataframe.
        """
        pass

    def init(self, start_date: str):
        self._df = self._df.rename(columns={"SignalTime": "Date"}).set_index("Date")
        self._df.index = pd.to_datetime(self._df.index)
        return self._df.loc[start_date:].sort_index()

    def normalize(self):
        for tf in ["Bg", "Ft"]:
            for column in [f"{tf}Green", f"{tf}GreenPrior", f"{tf}Yellow"]:
                self._df[f"r{column}"] = self._df[column] / self._df[f"{tf}Atr"]

            r_sign = self._df["Direction"].apply(lambda x: 1 if x == "UP" else -1)

            for column in [
                f"{tf}P1Close",
                f"{tf}P2Close",
                f"{tf}P3Close",
                f"{tf}P4Close",
                f"{tf}P5Close",
                f"{tf}P1MAE",
                f"{tf}P2MAE",
                f"{tf}P3MAE",
                f"{tf}P4MAE",
                f"{tf}P5MAE",
                f"{tf}P1MFE",
                f"{tf}P2MFE",
                f"{tf}P3MFE",
                f"{tf}P4MFE",
                f"{tf}P5MFE",
            ]:
                if column in self._df.columns:
                    self._df[f"r{column}"] = (
                        r_sign
                        * (self._df[column] - self._df["SignalPrice"])
                        / self._df[f"{tf}Atr"]
                    )

    def show(self, drop_duplicates: bool = True):
        de_columns = [
            "BgBarNumber",
            "BgGreen",
            "BgGreenPrior",
            "BgYellow",
            "BgValueAreaHigh",
            "BgValueAreaLow",
            "BgP1Close",
            "BgP2Close",
            "BgP3Close",
            "BgP4Close",
            "BgP5Close",
            "BgP1MAE",
            "BgP2MAE",
            "BgP3MAE",
            "BgP4MAE",
            "BgP5MAE",
            "BgP1MFE",
            "BgP2MFE",
            "BgP3MFE",
            "BgP4MFE",
            "BgP5MFE",
            "FtBarNumber",
            "FtGreen",
            "FtGreenPrior",
            "FtYellow",
            "FtValueAreaHigh",
            "FtValueAreaLow",
            "FtP1Close",
            "FtP2Close",
            "FtP3Close",
            "FtP4Close",
            "FtP5Close",
            "FtP1MAE",
            "FtP2MAE",
            "FtP3MAE",
            "FtP4MAE",
            "FtP5MAE",
            "FtP1MFE",
            "FtP2MFE",
            "FtP3MFE",
            "FtP4MFE",
            "FtP5MFE",
            "BgSignalOpen",
            "BgSignalHigh",
            "BgSignalLow",
            "BgSignalClose",
            "FtSignalOpen",
            "FtSignalHigh",
            "FtSignalLow",
            "FtSignalClose",
        ]

        columns = [column for column in self._df.columns if column not in de_columns]
        df = self._df.copy(deep=True)
        if drop_duplicates:
            df = df.drop_duplicates(subset=["Ticker", "BgBarNumber"])
        return df.loc[:, columns]
