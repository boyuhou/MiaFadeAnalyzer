"""This module handles different functions to import reports.
"""

import typing
import pandas as pd
import os
from docxtpl import DocxTemplate


REPORT_IBD_MONTHLY = "ibd_monthly"
REPORT_IBD_WEEKLY = "ibd_weekly"
REPORT_MARKET = "market"
REPORT_WAM_RS = "WAM_RS"
REPORT_WAM_RSCHANGE = "RS_Change"
REPORT_WAM_MAX20 = "RS_MAX20"
REPORT_WAM_MIN20 = "RS_MIN20"

DATE_NAME = "Date"
TICKER_NAME = "Ticker"
IBD_LOW_NAME = "IBD_LOW"
IBD_HIGH_NAME = "IBD_HIGH"

AUD_NAME = "AUD"
CAD_NAME = "CAD"
CHF_NAME = "CHF"
EUR_NAME = "EUR"
GBP_NAME = "GBP"
INDEX_NAME = "INDEX"
JPY_NAME = "JPY"
NZD_NAME = "NZD"
USD_NAME = "USD"


def load_daily_debrief_data(root_path: str) -> dict:
    dict_result = {
        REPORT_IBD_MONTHLY: read_csv_from_folder(os.path.join(root_path, "ibd", "monthly"), [DATE_NAME, TICKER_NAME, IBD_LOW_NAME, IBD_HIGH_NAME]),
        REPORT_IBD_WEEKLY: read_csv_from_folder(os.path.join(root_path, "ibd", "weekly"), [DATE_NAME, TICKER_NAME, IBD_LOW_NAME, IBD_HIGH_NAME]),
        REPORT_MARKET: read_csv_from_folder(os.path.join(root_path, "market")),
        REPORT_WAM_RS: {
            AUD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS", AUD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            CAD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS", CAD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            CHF_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS", CHF_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            EUR_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS", EUR_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            GBP_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS", GBP_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            INDEX_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS", INDEX_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            JPY_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS", JPY_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            NZD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS", NZD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            USD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS", USD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
        },
        REPORT_WAM_RSCHANGE: {
            AUD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS_CHANGE", AUD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            CAD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS_CHANGE", CAD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            CHF_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS_CHANGE", CHF_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            EUR_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS_CHANGE", EUR_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            GBP_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS_CHANGE", GBP_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            INDEX_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS_CHANGE", INDEX_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            JPY_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS_CHANGE", JPY_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            NZD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS_CHANGE", NZD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            USD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "RS_CHANGE", USD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
        },
        REPORT_WAM_MAX20: {
            AUD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MAX20", AUD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            CAD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MAX20", CAD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            CHF_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MAX20", CHF_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            EUR_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MAX20", EUR_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            GBP_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MAX20", GBP_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            INDEX_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MAX20", INDEX_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            JPY_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MAX20", JPY_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            NZD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MAX20", NZD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            USD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MAX20", USD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
        },
        REPORT_WAM_MIN20: {
            AUD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MIN20", AUD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            CAD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MIN20", CAD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            CHF_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MIN20", CHF_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            EUR_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MIN20", EUR_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            GBP_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MIN20", GBP_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            INDEX_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MIN20", INDEX_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            JPY_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MIN20", JPY_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            NZD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MIN20", NZD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
            USD_NAME: read_csv_from_folder(os.path.join(root_path, "wam_rs", "MIN20", USD_NAME), [DATE_NAME, TICKER_NAME, "VALUE"]),
        }
    }
    return dict_result
    

def read_csv_from_folder(folder_path: str, header: list = None) -> pd.DataFrame:
    list_of_dfs = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)

        if header is not None:
            df = pd.read_csv(file_path, names=header, parse_dates=[DATE_NAME])
        else:
            df = pd.read_csv(file_path, parse_dates=[DATE_NAME])
        
        list_of_dfs.append(df)
    
    df = pd.concat(list_of_dfs, axis=0).set_index([DATE_NAME, TICKER_NAME])
    return df


def generate_report(dict_dfs: dict, * , ticker: str, process_date: str, template_folder: str = r"template") -> None:
    if ticker not in [
        "AUDUSD",
        "EURUSD",
        "GBPUSD",
        "NZDUSD",
        "USDCAD",
        "USDCHF",
        "USDJPY",
        "DX ##-##",
        "ES ##-##",
        "CL ##-##",
        "DX ##-##",
        "6A ##-##",
        "6B ##-##",
        "6C ##-##",
        "6S ##-##",
        "6E ##-##",
        "6N ##-##",
        "6J ##-##"
    ]:
        raise ValueError("Not supported ticker!")

    tpl = DocxTemplate(os.path.join(template_folder, f"{ticker}.docx"))

    data_market = dict_dfs[REPORT_MARKET].xs(process_date, level=DATE_NAME).loc[ticker]

    context = {
        "current_date": process_date,
        "ticker": ticker,
        "market_env_htf2": data_market["Htf2MarketEnv"],
        "bar_count_htf2": data_market["Htf2BarState"],
        "inner_sell_low_htf2": format_str(data_market["Htf2InnerSellZoneLow"]),
        "inner_sell_high_htf2": format_str(data_market["Htf2InnerSellZoneHigh"]),
        "inner_buy_low_htf2": format_str(data_market["Htf2InnerBuyZoneLow"]),
        "inner_buy_high_htf2": format_str(data_market["Htf2InnerBuyZoneHigh"]),
        "vol_htf2": get_vol_condition(data_market["Htf2TwoPeriodAtr"], data_market["Htf2ATR"]),
        "atr_htf2": format_str(data_market['Htf2ATR']),
        "atr_delta_htf2": format_str(data_market['Htf2ATR'] - data_market['Htf2ATRPrior']),
        "green_htf2": format_str(data_market['Htf2Green']),
        "green_prior_htf2": format_str(data_market['Htf2GreenPrior']),
        "yellow_htf2": format_str(data_market['Htf2Yellow']),
        "market_env_ft": data_market["FtMarketEnv"],
        "bar_count_ft": data_market["FtBarState"],
        "inner_sell_low_ft": format_str(data_market["FtInnerSellZoneLow"]),
        "inner_sell_high_ft": format_str(data_market["FtInnerSellZoneHigh"]),
        "inner_buy_low_ft": format_str(data_market["FtInnerBuyZoneLow"]),
        "inner_buy_high_ft": format_str(data_market["FtInnerBuyZoneHigh"]),
        "vol_ft": get_vol_condition(data_market["FtTwoPeriodAtr"], data_market["FtATR"]),
        "atr_ft": format_str(data_market['FtATR']),
        "atr_delta_ft": format_str(data_market['FtATR'] - data_market['FtATRPrior']),
        "green_ft": format_str(data_market['FtGreen']),
        "green_prior_ft": format_str(data_market['FtGreenPrior']),
        "yellow_ft": format_str(data_market['FtYellow']),
        "market_env_bg": data_market["BgMarketEnv"],
        "bar_count_bg": data_market["BgBarState"],
        "inner_sell_low_bg": format_str(data_market["BgInnerSellZoneLow"]),
        "inner_sell_high_bg": format_str(data_market["BgInnerSellZoneHigh"]),
        "inner_buy_low_bg": format_str(data_market["BgInnerBuyZoneLow"]),
        "inner_buy_high_bg": format_str(data_market["BgInnerBuyZoneHigh"]),
        "vol_bg": get_vol_condition(data_market["BgTwoPeriodAtr"], data_market["BgATR"]),
        "atr_bg": format_str(data_market['BgATR']),
        "atr_delta_bg": format_str(data_market['BgATR'] - data_market['BgATRPrior']),
        "green_bg": format_str(data_market['BgGreen']),
        "green_prior_bg": format_str(data_market['BgGreenPrior']),
        "yellow_bg": format_str(data_market['BgYellow']),
    }

    df_rs = get_rs_value(dict_dfs, ticker, process_date)
    rs_context = {
        "col_labels": df_rs.columns.tolist(),
    }
    list_result = []
    dict_rs = df_rs.T.to_dict(orient="list")

    for key in dict_rs.keys():
        list_result.append({
            'label': key,
            'cols': dict_rs[key]
    })
    rs_context["tbl_contents"] = list_result

    tpl.render({**context, **rs_context})
    tpl.save(f"output/{ticker}_{process_date}.docx")


def get_vol_condition(data: float, atr: float):
    if data > 2 * atr:
        return "Volatile"
    elif data < atr:
        return "Quiet"
    else:
        return "Normal"

    
def format_str(data: typing.Union[str, float]) -> str:
    return f"{float(data):.4f}"


def get_rs_value(dict_dfs: dict, ticker: str, process_date: str) -> pd.DataFrame:
    ticker_map = {
        "AUDUSD": "AUD",
        "NZDUSD": "NZD",
        "USDCAD": "CAD",
        "USDCHF": "CHF",
        "EURUSD": "EUR",
        "GBPUSD": "GBP",
        "USDJPY": "JPY",
        "DX ##-##": "USD",
        "6A ##-##": "AUD",
        "6B ##-##": "GBP",
        "6C ##-##": "CAD",
        "6S ##-##": "CHF",
        "6E ##-##": "EUR",
        "6N ##-##": "NZD",
        "6J ##-##": "JPY"
    }

    folder_name = ticker_map[ticker]

    try:
        df_rs = dict_dfs[REPORT_WAM_RS][folder_name].xs(process_date).iloc[:,0].to_frame(REPORT_WAM_RS)
    except KeyError:
        process_date = (pd.to_datetime(process_date) + pd.tseries.offsets.BDay(1) - pd.tseries.offsets.BDay(1)).strftime("%Y-%m-%d")

    df_rs = dict_dfs[REPORT_WAM_RS][folder_name].xs(process_date).iloc[:,0].to_frame(REPORT_WAM_RS)
    df_rs_change = dict_dfs[REPORT_WAM_RSCHANGE][folder_name].xs(process_date).iloc[:,0].to_frame(REPORT_WAM_RSCHANGE)
    df_rs_max20 = dict_dfs[REPORT_WAM_MAX20][folder_name].xs(process_date).iloc[:,0].to_frame(REPORT_WAM_MAX20)
    df_rs_min20 = dict_dfs[REPORT_WAM_MIN20][folder_name].xs(process_date).iloc[:,0].to_frame(REPORT_WAM_MIN20)

    df_result = pd.concat([df_rs, df_rs_change, df_rs_max20, df_rs_min20], axis=1)
    return df_result
